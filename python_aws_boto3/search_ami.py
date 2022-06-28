import boto3
import conn_aws

#AMI_ID預先用Packer產出
#將Packer產出的tag (Name:Value) Value值給該class作為Filters用

class SEARCH_AMI :
    def list_ami(self,tags):
    #顯示出AMI的描述、篩選
        response = conn_aws.CONN_AWS().conn_client().describe_images(Owners=["self"],
                            Filters=[
                                {
                                'Name': 'name',
                                'Values': [tags]
                                }
                            ]
                            )                        
    #回傳AMI ID (從AWS格式分解出)
        response=response['Images'][0]['ImageId'] 
        return response

if __name__ == '__main__' :
    aa=SEARCH_AMI('BaseOS-Centos7.9 1656050819')
    print ("使用AMI_ID: " , aa.list_ami())