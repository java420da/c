# main

sudo apt update
sudo apt install rsync openssh-server net-tools -y

sudo systemctl enable --now ssh
sudo systemctl status ssh

hostname -I
whoami

# backup

sudo apt update
sudo apt install rsync openssh-server -y

sudo systemctl enable --now ssh

hostname -I
whoami

mkdir -p ~/backup

# main

mkdir -p ~/source
nano ~/source/temp.txt

rsync -av ~/source/ backup_username@BACKUP_IP:~/backup/

# backup

cat ~/backup/temp.txt