import os, boto3
import json


client = boto3.client('comprehend')


def lambda_handler(event, context):
    body = event.get('body')
    input_text = event["body"].strip()
    sentiment=client.detect_sentiment(Text=input_text,LanguageCode='en')
    res = sentiment['Sentiment']
    result = {
        "statusCode": 200,
        "body": json.dumps(res)
        }
        
    return result
