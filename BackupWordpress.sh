#! /bin/bash
#author: fakir
#email: ishaofeng@foxmail.com
#descp: 备份wordpress个人博客

script='
echo "Start Backup Wordpress"
rm -rf backup
mkdir backup
echo "1.Backup Database"
mysqldump -uroot -p wordpress | gzip > wordpress.sql.gz
mv wordpress.sql.gz backup/
echo "2.Backup website"
cp -r wordpress backup/
echo "3.Compress Backup"
tar -zc -f smalllv.tar.gz backup
'

ssh server "$script"

echo "4.Download Backup"
scp server:/home/ubuntu/smalllv.tar.gz /home/shao/work/Cloud/smalllv/`date +%Y%m%d`.tar.gz

echo "5.Finish"
