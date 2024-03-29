import boto3
import base64
import json


def lambda_handler(event, context):
    client = boto3.client('rekognition')
    body = event.get('body')
    request_body = event["body"].strip()
    request_data = json.loads(request_body)
    photo_bytes = base64.b64decode(request_data["image_bytes"])
    
    response = client.detect_labels(Image={'Bytes': photo_bytes}, MaxLabels=15,
    Features=["GENERAL_LABELS"]
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
