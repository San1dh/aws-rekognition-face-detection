from PIL import Image, ImageDraw
import json


def main():
  # print("hello")

  image = Image.open("pexels-omer-derinyar.jpg")
  # image.show()

  f = open("pexels-omer-derinyar.jpg_face_1.json")
  faceDetail = json.load(f)

  imgWidth, imgHeight = image.size
  draw = ImageDraw.Draw(image)

  # calculate and display bounding boxes for each detected face
  # print('Detected faces for ' + photo)
  # for faceDetail in response['FaceDetails']:
  print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) +
        ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

  box = faceDetail['BoundingBox']
  left = imgWidth * box['Left']
  top = imgHeight * box['Top']
  width = imgWidth * box['Width']
  height = imgHeight * box['Height']

  print('Left: ' + '{0:.0f}'.format(left))
  print('Top: ' + '{0:.0f}'.format(top))
  print('Face Width: ' + "{0:.0f}".format(width))
  print('Face Height: ' + "{0:.0f}".format(height))

  points = ((left, top), (left + width, top), (left + width, top + height),
            (left, top + height), (left, top))
  # print(points)
  draw.line(points, fill='#ffffff', width=16)

  # draw.rectangle((left, top, left + width, top + height),
  #                outline='#00d400',
  #                width=16)

  image.save("bounding_box.jpg")

  # image.show()

  # Alternatively can draw rectangle. However you can't set line width.
  # draw.rectangle([left,top, left + width, top + height], outline='#00d400')

  # return len(response['FaceDetails'])


if __name__ == "__main__":
  main()

# def show_faces(photo):

# session = boto3.Session(profile_name='profile-name')
# client = session.client('rekognition')

# Load image from S3 bucket
# s3_connection = boto3.resource('s3')
# s3_object = s3_connection.Object(bucket, photo)
# s3_response = s3_object.get()

# stream = io.BytesIO(s3_response['Body'].read())
# image = Image.open(stream)

# Call DetectFaces
# response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
#                                Attributes=['ALL'])

# def main():
#     # bucket = "bucket-name"
#     photo = "photo-name"
#     # faces_count = show_faces(photo)
#     # print("faces detected: " + str(faces_count))
