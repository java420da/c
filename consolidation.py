free -h
top

sudo apt update
sudo apt install apache2 -y
sudo apt install net-tools -y

sudo systemctl enable --now apache2
sudo systemctl status apache2

sudo mkdir -p /var/www/html/vm2
sudo cp /var/www/html/index.html /var/www/html/vm2/index.html
sudo nano /var/www/html/vm2/index.html

sudo systemctl restart apache2
sudo systemctl status apache2

ifconfig