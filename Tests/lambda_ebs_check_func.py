import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instances = ec2.instances.all()
    for instance in instances:
        for r in instance['Reservations']:
            for instance in r['Instances']:
                ec2_tags=instance['Tags']
                for item in instance.volumes.all():
                    ebs_id = item.id
                    vol = ec2.Volume(id=ebs_id)
                    ebs_tags=vol.tags
                    if ebs_tags == []:
                        for tag in ec2_tags:
                            add_tag(ebs_id, tag.key, tag.name)
                    if set(ebs_tags) == set(ec2_tags):
                        continue
                    else:
                        for tag in ec2_tags:
                            add_tag(ebs_id, tag.key, tag.name)
                        for ebs_tag in ebs_tags:
                            if ebs_tag not in ec2_tags:
                                delete_tag(ebs_id, tag.key, tag.name)
                            


def add_tag(ebs_id, key, name):
    response = ec2.create_tags(
        Resources=[
            ebs_id
        ],
        Tags=[
            {
                'Key': key,
                'Value': name,
            },
        ],
    )
    return response
    
def delete_tag(ebs_id, key, name):
    response = ec2.delete_tags(
        Resources=[
            ebs_id
        ],
        Tags=[
            {
                'Key': key,
                'Value': name,
            },
        ],
    )
    return response
