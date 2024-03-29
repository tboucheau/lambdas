import logging
import os, boto3
import json


logger = logging.getLogger()
logger.setLevel(logging.INFO)


client = boto3.client('comprehend')

def lambda_handler(event, context):
    logger.info("#### Lambda API event 01 #### - %s" % event)
    body = event.get('body')
    logger.info("#### Lambda API event 02 #### - %s" % body)
    input_text = event["body"].strip()
    logger.info("#### Lambda API event 03 #### - %s" % input_text)
    sentiment=client.detect_sentiment(Text=input_text,LanguageCode='fr')
    res = sentiment['Sentiment']
    logger.info("#### Lambda API event 04 #### - %s" % sentiment)
    result = {
        "statusCode": 200,
        "body": json.dumps(res)
        }
        
    return result