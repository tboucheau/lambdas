import boto3
import base64
import json


client = boto3.client('rekognition')


def lambda_handler(event, context):
    body = event.get('body')
    request_body = event["body"].strip()
    request_data = json.loads(request_body)
    photo_bytes = base64.b64decode(request_data["image_bytes"])
    
    response = client.recognize_celebrities(Image={'Bytes': photo_bytes})
    
    celebrities_info = []
    for celebrity in response['CelebrityFaces']:
        celebrity_info = {
            'Name': celebrity['Name'],
            'Id': celebrity['Id'],
            'KnownGender': celebrity['KnownGender']['Type'],
            'Smile': celebrity['Face']['Smile']['Value'],
            'Position': {
                'Left': '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']),
                'Top': '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top'])
            },
            'Info': celebrity['Urls']
        }
        celebrities_info.append(celebrity_info)

    return {
        "statusCode": 200,
        "body": json.dumps(celebrities_info)
    }
