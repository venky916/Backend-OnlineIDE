import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
REGION_NAME='ap-soth-1'

def upload_to_s3():
    # session=boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
    #                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #                       region_name=REGION_NAME)
    
    # s3=session.client('s3')
    # object=s3.Object("images-appscreenshots","admin.png")
    # file=open("./a.txt","rb+")
    s3 = boto3.client('s3')
    result=s3.upload_file('./a.txt','images-appscreenshots','a.txt')
    print(result)
    
def get_url_object():
    bucket_name = "images-appscreenshots"
    key = "a2.txt"
    # session=boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
    #                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #                       region_name=REGION_NAME)
    
    # s3=session.client('s3')
    # s3 = boto3.resource('s3')
    s3 = boto3.client("s3", 
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    # bucket = s3.Bucket(bucket_name)
    s3.upload_file("a2.txt",bucket_name, key)
    location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
    print(url)
    return url
