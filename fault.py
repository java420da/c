sudo apt update
sudo apt install rsync openssh-server -y

sudo systemctl enable --now ssh
mkdir -p ~/backup
ifconfig
whoami

mkdir -p ~/source
nano ~/source/temp.txt
rsync -av ~/source/ backup_username@BACKUP_IP:~/backup/

cat ~/backup/temp.txt