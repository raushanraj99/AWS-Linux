
import boto3

bucketName = "mybukt12"
S3 = boto3.client('s3')

response = S3.create_bucket( 
    ACL = 'private',
    Bucket= bucketName,
     CreateBucketConfiguration={
          "LocationConstraint":"ap-south-1"
     }
)

value = f"S3 Bucket Launched of {bucketName} name"
print(value)