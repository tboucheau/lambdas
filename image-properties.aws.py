import boto3
import base64
import json


client = boto3.client('rekognition')


def lambda_handler(event, context):
    body = event.get('body')
    request_body = event["body"].strip()
    request_data = json.loads(request_body)
    photo_bytes = base64.b64decode(request_data["image_bytes"])
    response = client.detect_labels(Image={'Bytes': photo_bytes}, MaxLabels=10,
     Features=["GENERAL_LABELS", "IMAGE_PROPERTIES"],
     Settings={"GeneralLabels": {"LabelInclusionFilters":["Cat"]},
     "ImageProperties": {"MaxDominantColors":10}}
     )
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
