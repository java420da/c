# main vm
sudo apt update
sudo apt install apache2 openssh-server rsync htop -y

sudo systemctl enable --now ssh
sudo systemctl enable --now apache2

hostname -I
whoami

# vm1 ans vm2
sudo apt update
sudo apt install apache2 rsync openssh-client -y

echo "Application from VM1" | sudo tee /var/www/html/index.html

sudo systemctl start apache2

rsync -av /var/www/html/ username@192.168.1.100:~/vm1/

# main vm
ls ~/vm1
ls ~/vm2

sudo mkdir -p /var/www/html/vm1
sudo mkdir -p /var/www/html/vm2

sudo rsync -av ~/vm1/ /var/www/html/vm1/
sudo rsync -av ~/vm2/ /var/www/html/vm2/

sudo systemctl restart apache2

http://192.168.1.100/vm1/
http://192.168.1.100/vm2/

sudo apt install htop -y
htop

free -h
