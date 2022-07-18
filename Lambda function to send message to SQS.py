import json
import boto3
from datetime import datetime

def lambda_handler(event,context)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sqs = boto3.client("sqs")
    sqs.send_message(
    #input Queue URL the URL that provided when you created the SQS queue
         response = client.send_message(QueueUrl=https://sqs.us-east-1.amazonaws.com/767779967756/time,MessageBody= current_time
        )
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
