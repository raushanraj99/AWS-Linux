import boto3 as bt
myec2 = bt.client("ec2")


response = myec2.run_instances(
    ImageId = "ami-0ded8326293d3201b",
    InstanceType = "t2.micro",
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': "MypythonOs" # mypythoOs is the InstanceName
                    },
                ]
            },
        ]

)
print("instanceLaunched")