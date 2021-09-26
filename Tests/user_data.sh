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
