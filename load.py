#vm1 and vm2
from turtle import update


sudo hostnamectl set-hostname vm1/vm2

sudo apt update
sudo apt install apache2 -y
sudo apt install net-tools -y

sudo systemctl enable --now apache2
sudo systemctl status apache2

sudo nano /var/www/html/index.html

ifconfig

# main vm
ping -c 4 192.168.94.128
ping -c 4 192.168.94.129

sudo hostnamectl set-hostname loadbalancer

sudo apt update
sudo apt install haproxy -y
sudo apt install net-tools -y

sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.backup
sudo nano /etc/haproxy/haproxy.cfg

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin/leastconn
    server vm1 192.168.94.128:80 check
    server vm2 192.168.94.129:80 check

listen stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 5s

sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo systemctl enable haproxy
sudo systemctl restart haproxy
sudo systemctl status haproxy

ifconfig

http://192.168.94.130:8404/stats
