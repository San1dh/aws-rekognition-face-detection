import json
import boto3

client = boto3.client('rekognition')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement

    # bucket = event['Records'][0]['s3']['bucket']['name']
    bucket = "my-own-rekognition-bucket"
    key = "CyberCity.jpg"
    # key = event['Records'][0]['s3']['object']['key']
    
    # print(bucket)
    # print(key)
    
    # response = s3.get_object(Bucket=bucket, Key=key)
    
    bucket_name = "my-own-rekognition-bucket"
    file_name = key

    response = client.detect_labels(
        
            Image={
                'S3Object':{
                    'Bucket':bucket_name,
                    'Name':file_name
                }
            },
            # Features = ['ALL']
        )

    # Process result
    i = 0
    print("LABEL NO         NAME            CONFIDENCE")
    print("-----------------------------------------------")
    for label in response['Labels']:
        i += 1
        # print(i)
        # print(str(i) + "             " + label['Name'] + "             ", label["Confidence"])
        print("{: >20} {: >20} {: >20}".format(i, label["Name"], round(label["Confidence"], 2)))

    if i == 0:
        print("no labels :(")

    j = 0
    for key, value in response.items():
        j += 1
        print("Key ", j , ":")
        print(key)

    # print(json.dumps(response, indent=2))
    
    # result_buck = "my-rekog-results"

    # i = 0
    # for face in response['FaceDetails']:
    #     i += 1
    #     res_file_name = file_name + '_face_' + str(i) + '.json'
    #     uploadByteStream = bytes(json.dumps(face, indent = 2).encode('UTF-8'))
    
    #     s3.put_object(
    #         Bucket = result_buck,
    #         Key = res_file_name,
    #         Body = uploadByteStream
    #     )
  
