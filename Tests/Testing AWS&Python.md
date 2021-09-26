
region - US East (Ohio)us-east-2

====================================================================

В рамках задания были созданы следующие компоненты AWS:

#### 1. VPC and EC2:

**aws-vpc-1**

1. VPC1-subnet-private-1: **EC2** - private-host2-vpc1, **SG** - private-host-vpc1, **RT** - VPC1-route-table-private-1

2. VPC1-subnet-private-2: **EC2** - private-host1-vpc1, **SG** - private-host-vpc1, **RT** - VPC1-route-table-private-2

3. VPC1-subnet-public-1: **EC2** - bastion-host, **SG**: bastion SG, **RT** - VPC1-route-table-public-1, **IGW** - aws-vpc-1-IGW

4. VPC1-subnet-public-2: нет **EC2**, **SG** - VPC1-route-table-public-2 **IGW** - aws-vpc-1-IGW

5. Endpoint для доступа к S3, для установки nginx из amazon-linux-extras пакета без доступа в интернет

6. pc1(Peering connection) между VPC1 и VPC2, для того, чтобы бастион хост(VPC1) мог подключаться к приватным хоcтам из VPC2

**aws-vpc-2**

1. VPC2-subnet-public-1: нет **EC2**, **RT** - VPC2-route-table-public, **IGW** - aws-vpc-2-IGW

2. VPC2-subnet-private-1: **EC2** - private-host1-vpc2, **SG** - private-host-vpc1, **RT** - VPC2-route-table-private

3. Endpoint для доступа к S3, для установки nginx из amazon-linux-extras пакета без доступа в интернет

4. pc1(Peering connection) между VPC1 и VPC2, для того, чтобы бастион хост(VPC1) мог подключаться к приватным хоcтам из VPC2

#### Load Balancer and Autoscaling

1. ELB1(Load Balancer): **RT** - ELB-route-table, **SG** - ELB SG - балансировка в VPC1, между приватными сетями. Доступен из публичных подсетей.

2. ELB DNS name: ELB1-1942376519.us-east-2.elb.amazonaws.com

3. Target Group - ELB-target-group

4. Launch template - launch-template-1 (5 version - latest)

5. Autoscale Group - autoscale-group-1 (5 version of template)

#### Policy and Roles

1. lambda_autoscale_dns_policy - для lambda функции 
2. lambda_ebs_volume_policy - для lambda функции
3. restrict_ec2_ebs_launch_policy - запрет на запуск ec2/ebs
4. S3_read_only - EC2 доступ только на чтение

#### S3

1. aws-bucket-dev

#### DNS Internal Zone

1. devops.internal

#### Lambda functions with Cloud Watch  triggers

1. lambda_ebs_check_func
[lambda_ebs_check_func](https://github.com/NastyaP1/quantori-devops-school/blob/master/Tests/lambda_ebs_check_func.py)

3. lambda_autoscale_ddns_func
[lambda_autoscale_ddns_func](https://github.com/NastyaP1/quantori-devops-school/blob/master/Tests/lambda_autoscale_ddns_func.py)

**Template's user data section to launch instances**

[user_data_template](https://github.com/NastyaP1/quantori-devops-school/blob/master/Tests/user_data.sh)
