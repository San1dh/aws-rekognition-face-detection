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

    if i == 0:
        print("no faces :(")

    result_buck = "my-rekog-results"

    i = 0
    for face in response['FaceDetails']:
        res_file_name = file_name + '_face_' + str(i) + '.json'
        i += 1
        uploadByteStream = bytes(json.dumps(face, indent = 2).encode('UTF-8'))
    
        s3.put_object(
            Bucket = result_buck,
            Key = res_file_name,
            Body = uploadByteStream
        )
