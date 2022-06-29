#coding=UTF-8
import boto3

#連接AWS
#※前提：C:\Users\User\.aws\credentials\
#先將aws_access_key_id、aws_secret_access_key定義好為環境變數內
#無先定義，需要將access key + secret key加入到變數中

class CONN_AWS:
    def __init__(self,aws_service="ec2",region="ap-northeast-1"):
        self.aws_service=aws_service
        self.region = region
    def conn_client(self):
        aws_client=boto3.client(self.aws_service,self.region)
        return aws_client
    def conn_resource(self):
        aws_resource=boto3.resource(self.aws_service,self.region)
        return aws_resource



if __name__ == '__main__':
    print (CONN_AWS().conn_client())
    print (CONN_AWS().conn_resource())

