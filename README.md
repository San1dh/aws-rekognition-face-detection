# aws-rekognition-test

Worked on some AWS services during an internship. Used a Lambda function to trigger everytime an image (PNG/JPG is supported) to a particular S3 bucket. Initially the files were hardcoded to test whether the Rekognition, S3 & Lambda worked. Now automated to detect any file & outputs the result to another bucket in JSON format for each face. (Only tried out the Detect Faces option so far.) Mostly many image & file uploads to S3 & detection capabilities by Rekognition are covered under the free trial.

The result JSON file will give attributes of the face like Wearing Glasses or Beard and their Emotions and many more features. It also gives the position of the face detected as a [Bounding Box](https://docs.aws.amazon.com/rekognition/latest/dg/images-displaying-bounding-boxes.html).

Basics made with the help of a video by Be a Better Dev on [Using Rekognition for Facial Analysis](https://www.youtube.com/watch?v=3PGPfs-ARdo). (The region for the Lambda function & S3 Bucket should be same or it cannot be accessed by the Lambda function. Spent some time on this.) Made the result S3 file dynamic from searching the web across multiple articles & Stack Overflow links but they were too complex for me. Finally got a simple solution from Be a Better Dev on [S3 & Lambda Triggers](https://www.youtube.com/watch?v=OJrxbr9ebDE). Don't remember where I got the upload to S3 result. But its the basic Official Boto3 Documentation on [S3 upload](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html).

Spaces in file name cause errors in triggering the Lambda function. Do not know if any other special characters affect it.

The bounding box creation is from the official AWS docs [here](https://docs.aws.amazon.com/rekognition/latest/dg/images-displaying-bounding-boxes.html). It should be run on the console so that Pillow can be installed but I had a problem with connecting to AWS from work system. So manually uploaded the files to Replit from S3 & tested it. Increase the width of the line to make it visible, width = 2 given in the docs is very small & not visible. Tried adding Pillow to Lambda function as a Zip file (installed & zipped using AWS Shell) but size is larger than Lambda's zip file limit which prevents writing to the Lambda function again (3 MB, I think). Maybe should try & add the Python code along with the Pillow package & zip it & then add it to Lambda.

Tried out the Label Detection from the official Boto3 [Rekognition API docs](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html). Made a new Lambda function & hardcoded the image to test it & printed the output to console because I didn't want to incease Free Tier limits so soon. Already got some 500+ PUT & 2500+ GET requests for S3 within the first few days of using Rekognition's Face Detection API (& writing the o/p to S3).

Added printing out the major emotion in each face in a picture into another Lambda function. Mostly like the previous code for face detection. I think it is accurate for the most part if the face is clear.

***Lambda has a interesting feature (at least in Python) where a single word with colon (:) at the end is printed in green to the console.***
