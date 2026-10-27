echo $HOME
# output: /home/ubuntu

nano /home/ubuntu/script.sh

#!/bin/bash
for i in {1..6}; do
    echo "Hello Selcia" >> /home/ubuntu/output.log
    sleep 10
done

chmod +x /home/ubuntu/script.sh

touch /home/ubuntu/output.log

crontab -e

* * * * * /home/ubuntu/script.sh

tail -f /home/ubuntu/output.log

cat /home/ubuntu/output.log