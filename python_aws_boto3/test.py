#coding=UTF-8
import boto3
import conn_aws
import search_ami
import creat_ec2

#測試創建EC2，從AMI_ID

#取得AMI的ID，從AWS上的Tag Name而來
ami_id=search_ami.SEARCH_AMI().list_ami('BaseOS-Centos7.9 1656050819')
#創建EC2主機，自訂數量、機器規格、AWS上的憑證名稱
create_instance=creat_ec2.CREAT_EC2().creat(ami_id,1,1,'t3.micro','it')

#顯示出EC2的instance id
print (create_instance)