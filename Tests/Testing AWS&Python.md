Для входа в AWS под пользователем с парвами доступа read-only:

Username: read_only_person

Password: Devopstest010

ID: 466616955433

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
2. lambda_autoscale_ddns_func

**Template's user data section to launch instances**

```
#!/bin/bash
useradd -s /bin/bash -d /home/teacher -m teacher
mkdir /home/teacher/.ssh
sudo chown -R teacher:teacher /home/teacher/.ssh
sudo chown -R root:root /home/teacher/.ssh
sudo usermod -aG sudo teacher
sudo usermod -aG root teacher
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCkBIEsfJD6d0J4tqTnVq4z3Ve0bop71b+27j75gncRsLdAHLVg/InhJdrtnVszNGzPIPTXM8jsb/cc0e0JDD7Teoqz0YxJH+ZhY5Y6iy5n8Vx+CCWr5Rra5IpfJclvDPbH+okiUqGyt1fmvS+VkoBWxOFiAOsfdSdTwJWyGs0kplZouOh93cRc/9mp16mNcR5B86+ORLrMZCq3ZGVj2F3YjlhXb1/aUz7Mi1E6Ze9UQQe2oKqf4w8wXIiSejCcrsZ9CT6SX28Kqw2Ilb+7cr84vXIQDKxZySupztn8qMFlDvtoeK4b+RvEtpRmJaC/no9yjTeDTnBYVsV+vQvxiaaeLzkbPRhd0Ovlayoz/gXqI4DOCaQTfISHxG7X+NLfpW6Hmvgf+2i9OStUMJatDx6y1BAj5cjBKo1JRS73U2o5wYYTAlq6jaDAUzWE8Ili7cZ2Qx2dz5uFq6S8NteIt9yR6LsfaHYKG/5WmaA3LOnYAqV+S7nq2WQVQ2Z5bzpJC9s= andrey@MBP-Andrey" > /home/teacher/.ssh/authorized_keys

chmod 700 /home/teacher/.ssh

chmod 600 /home/teacher/.ssh/authorized_keys

sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

sudo amazon-linux-extras install -y nginx1

EC2_AVAIL_ZONE=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
EC2_REGION=`echo \"$EC2_AVAIL_ZONE\" |  grep -Po "(us|sa|eu|ap)-(north|south|central)?(east|west)?-[0-9]+"`
EC2_IP=`curl -s http://169.254.169.254/latest/meta-data/local-ipv4`

sleep 10

sudo systemctl enable nginx.service

sleep 10

sudo sed -i 's/80/8888/' /etc/nginx/nginx.conf

echo "" > /usr/share/nginx/html/index.html
echo "<title>Welcome to nginx!</title>" >> /usr/share/nginx/html/index.html 
echo "<style>" >> /usr/share/nginx/html/index.html
echo "    body {" >> /usr/share/nginx/html/index.html
echo "        width: 35em;" >> /usr/share/nginx/html/index.html
echo "        margin: 0 auto;" >> /usr/share/nginx/html/index.html
echo "        font-family: Tahoma, Verdana, Arial, sans-serif;" >> echo /usr/share/nginx/html/index.html
echo "    }" >> /usr/share/nginx/html/index.html
echo "</style>" >> /usr/share/nginx/html/index.html
echo "</head>" >> /usr/share/nginx/html/index.html
echo "<html>" >> /usr/share/nginx/html/index.html
echo "    <head>" >> /usr/share/nginx/html/index.html
echo "        <title>Welcome!</title>" >> /usr/share/nginx/html/index.html
echo "    </head>" >> /usr/share/nginx/html/index.html
echo "    <body>" >> /usr/share/nginx/html/index.html
echo "        <p>Instance IP: $EC2_IP</p>" >> /usr/share/nginx/html/index.html
echo "        <p>Region: $EC2_REGION </p>" >> /usr/share/nginx/html/index.html
echo "        <p>Availability zone: $EC2_AVAIL_ZONE</p>" >> /usr/share/nginx/html/index.html
echo "    </body>" >> /usr/share/nginx/html/index.html
echo "</html>" >> /usr/share/nginx/html/index.html

sudo systemctl restart nginx
```
