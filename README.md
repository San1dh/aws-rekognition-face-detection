# aws-rekognition-test

Worked on some AWS services during an internship. Used a Lambda function to trigger everytime an image (PNG/JPG is supported) to a particular S3 bucket. Initially the files were hardcoded to test whether the Rekognition, S3 & Lambda worked. Now automated to detect any file & outputs the result to another bucket in JSON format for each face. (Only tried out the Detect Faces option so far.) Mostly many image & file uploads to S3 & detection capabilities by Rekognition are covered under the free trial.
