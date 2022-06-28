語言：Python v3.10.4  
套件：boto3  
目的：控制AWS  

流程：接入AWS資源→找尋指定AMI ID的Tag Name:Value，產出AMI ID→使用AMI ID創建EC2機器並給予指定的規格數量  

檔案結構：  
python_aws_boto3  --- conn_aws (接入AWS)  
                  --- search_ami (產出AWS的AMI ID)  
                  --- creat_ec2 (使用自己指定的ami創建EC2機器)  
test (操作用)

備註：  
裡面未含AWS的Acess key id、Secret key 
可自行綁在OS的環境變數上 或 CLASS CONN_AWS 的兩個方法給額外變數


