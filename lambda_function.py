import json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    # TODO implement

    bucket_name = "my-own-rekognition-bucket"
    file_name = "img5.jpg"

     response = client.detect_faces(
            Image={
                'S3Object':{
                    'Bucket':bucket_name,
                    'Name':file_name
                }
            },
            Attributes = ['ALL']
        )

    # Process result
    i = 0
    for face in response['FaceDetails']:
        i += 1
        print("this is face number ", i)
        print(json.dumps(face, indent = 2))
    
