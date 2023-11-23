import json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    # TODO implement
    
    bucket_name = "my-own-rekognition-bucket"
    file_name = "grouping-3rd.jpg"
    
    response = client.detect_faces(
            Image={
                'S3Object':{
                    'Bucket':bucket_name,
                    'Name':file_name
                }
            },
            Attributes = ['ALL']
        )
        
    # process result
    # print(response)
    # for face in response['FaceDetails']:
    #     maxx = 0
    #     for em in face["Emotions"]:
    #         if em["Confidence"] > maxx:
    #             maxx = em["Confidence"]
    #             emotion = em["Type"]
    #             break
    i = 0
    for face in response['FaceDetails']:
        # maxx = 0
        i += 1
        conf = face["Emotions"][0]["Confidence"]
        emotion = face["Emotions"][0]["Type"]
        print("-----------")
        print("Face No ", i)
        print("Emotion: ")
        print(emotion)
        print(round(conf, 2))
        print("------------")    
    
# Duration: 812.41 ms	Billed Duration: 813 ms	Memory Size: 128 MB	Max Memory Used: 75 MB	Init Duration: 378.05 ms
# Similar with 1 or 2 for loops.
