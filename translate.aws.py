import json
import boto3


translate_client = boto3.client('translate')


def lambda_handler(event, context):
    body = event.get('body')
    input_text = event["body"].strip()
    objet_json = json.loads(input_text)
    valeur_data = objet_json["data"]
    valeur_target = objet_json["target"]
    translate_response = translate_client.translate_text(
        Text=valeur_data,
        SourceLanguageCode='auto',
        TargetLanguageCode=valeur_target
        )
    return {
        'statusCode': 200,
        'body': json.dumps(translate_response['TranslatedText'])
    }
