sudo hostnamectl set-hostname vm1

sudo apt update
sudo apt install apache2 -y
sudo apt install net-tools -y

sudo systemctl enable --now apache2
sudo systemctl status apache2

sudo nano /var/www/html/index.html

ifconfig
ping -c 4 192.168.94.128
ping -c 4 192.168.94.129

sudo apt install haproxy -y

sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.backup
sudo nano /etc/haproxy/haproxy.cfg

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server vm1 192.168.94.128:80 check
    server vm2 192.168.94.129:80 check

sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo systemctl enable haproxy
sudo systemctl restart haproxy
sudo systemctl status haproxy

ifconfig