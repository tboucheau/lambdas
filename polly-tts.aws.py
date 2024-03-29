import json
import boto3
import base64


polly_client = boto3.client('polly')


def lambda_handler(event, context):
    body = event.get('body')
    input_text = event["body"].strip()
    objet_json = json.loads(input_text)
    valeur_data = objet_json["text"]

    response = polly_client.synthesize_speech(
        Text=valeur_data,
        OutputFormat='mp3',
        VoiceId='Lea',  # Remplacer par le nom de la voix désirée
        Engine='neural' 
    )
    audio_base64 = base64.b64encode(response['AudioStream'].read()).decode('utf-8')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'audio/mpeg',
            'Content-Disposition': 'attachment; filename="output.mp3"'
        },
        'body': audio_base64
    }
