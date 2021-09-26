
import boto3
import sys
import time
import logging
import os

ec2_client = boto3.client('ec2')
asg_client = boto3.client('autoscaling')
r53_client = boto3.client('route53')

logger = logging.getLogger(name=__name__)
env_level = os.environ.get("LOG_LEVEL")
log_level = logging.INFO if not env_level else env_level
logger.setLevel(log_level)

domain = "devops.internal"
ttl = 60


def lambda_handler(event, context):
    asg_name = "autoscale-group-1"
    record_set_name = asg_name + "." + domain
    event_region = "us-east-2"
    sn_all = ec2_client.describe_subnets()
    for subnet in sn_all['Subnets']:
        event_vpc_id = subnet['VpcId']

    hosted_zone_id = "Z060048835EL9G1Q9FN0F"
#    hosted_zone_id = get_hosted_zone_id(domain, event_vpc_id)
#    if not hosted_zone_id:
#        hosted_zone_id = create_hosted_zone(domain, event_region, event_vpc_id)
        
    servers = get_asg_private_ips(asg_name)
    if servers:
        update_hosted_zone_records(hosted_zone_id, record_set_name, ttl, servers)
    else:
        delete_hosted_zone_records(hosted_zone_id, record_set_name)


def get_hosted_zone_id(domain, event_vpc_id):
    for hosted_zone in r53_client.list_hosted_zones()['HostedZones']:
        if hosted_zone['Name'] == domain and hosted_zone['Config']['PrivateZone'] == True:
            for vpc in r53_client.get_hosted_zone(Id = hosted_zone['Id'])['VPCs']:
                if vpc['VPCId'] == event_vpc_id:
                    return hosted_zone['Id']
    else:
        return False


def create_hosted_zone(domain, event_region, event_vpc_id):
    try:    
        response = r53_client.create_hosted_zone(
            Name = domain,
            VPC = {
                'VPCRegion': str(event_region),
                'VPCId': event_vpc_id
            },
            CallerReference = str(time.time()),
            HostedZoneConfig = {
                'Comment': "Created by Radware lambda fucntion for VPC {} in region {}".format(event_vpc_id, event_region),
                'PrivateZone': True
            }
        )
        return response['HostedZone']['Id']
    except:
        return False


def get_asg_private_ips(asg_name):
    for asg in asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])['AutoScalingGroups']:
        instance_ids = []
        for instance in asg['Instances']:
            if instance['LifecycleState'] == 'InService':
                instance_ids.append(instance['InstanceId'])
        if instance_ids:
            servers = []
            for reservation in ec2_client.describe_instances(InstanceIds = instance_ids)['Reservations']:
                for instance in reservation['Instances']:
                    if instance['State']['Name'] == 'running':
                        servers.append({'Value': instance['PrivateIpAddress']})
            return servers


def update_hosted_zone_records(hosted_zone_id, record_set_name, ttl, servers):
    r53_client.change_resource_record_sets(
    HostedZoneId = hosted_zone_id,
    ChangeBatch = {
        'Changes': [
            {
            'Action': 'UPSERT',
            'ResourceRecordSet': {
                'Name': record_set_name,
                'Type': 'A',
                'TTL': ttl,
                'ResourceRecords': sorted(servers)[:28]
            }
        }]
    })
    return


def delete_hosted_zone_records(hosted_zone_id, record_set_name):
    for record_set in r53_client.list_resource_record_sets(HostedZoneId = hosted_zone_id)['ResourceRecordSets']:
        if record_set['Name'] == record_set_name:
            try:
                r53_client.change_resource_record_sets(
                HostedZoneId = hosted_zone_id,
                ChangeBatch = {
                    'Changes': [
                        {
                        'Action': 'DELETE',
                        'ResourceRecordSet': record_set
                    }]
                })
                print("Record set {} removed successfully".format(record_set_name))
            except:
                print("Record set {} was already removed by other instance of the lambda function".format(record_set_name))
            break
    else:
        print("Record set {} was already removed by other instance of the lambda function".format(record_set_name))
