import json
import boto3
from datetime import datetime
def lambda_handler(event,context)
now = datetime.now()
client = boto3.client("sqs")
#input Queue URL the URL that provided when you created the SQS queue
response = client.send_message(QueueUrl=https://sqs.us-east-1.amazonaws.com/767779967756/time,MessageBody= event[

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
