import boto3
import conn_aws
import search_ami

class CREAT_EC2:
    def creat(slef,imageid=None,min=1,max=1,instancetype='t3.micro',keyname='it'):
        instances = conn_aws.CONN_AWS().conn_resource().create_instances(
            #使用上方取得的AMI_ID
            ImageId= imageid,
            #最小數量
            MinCount= min,
            #最大數量
            MaxCount= max,
            #機器規格
            InstanceType= instancetype,
            #使用憑證
            KeyName= keyname,
            SubnetId= 'subnet-09dd39cf733b90c53',
            SecurityGroupIds=[
                            'sg-01663515f0b8205ad',
                            ],
            TagSpecifications=[
                                {
                                'ResourceType': 'instance',
                                'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': 'TEST-543'
                                },
                                ]
                                }
                            ],
            )
        return instances
