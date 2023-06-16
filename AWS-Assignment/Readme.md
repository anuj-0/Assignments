# AWS Assignment:

### Question 1:
Create S3 bucket from AWS CLI
  
  1. Create an IAM role with S3 full access.
      ```
      aws iam create-role --role-name demo_rule  --assume-role-policy-document file://trustpolicy.json 
      ```
      Trust Policy contains:
      ```
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Service": "ec2.amazonaws.com"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```
      
      Attach the S3FullAccess policy:
      ```
      aws iam attach-role-policy --role-name demo_role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
      ```
  3. Create an EC2 instance with above role
      ```
      aws iam create-instance-profile --instance-profile-name demo_instance
      ```
      Attach role to it:
      ```
      aws iam add-role-to-instance-profile --instance-profile-name demo_instance  --role-name demo_role
      ```
  4. Create a bucket from AWS CLI
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CreateBucket.png)
 
### Question 2:
Put files in S3 bucket from lambda
  1. Create custom role for AWS lambda which will have only put object access
  2. Add role to generate and access Cloudwatch logs
  3. In python script, generate json in given format and save json file in bucket created
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/LambdaFunction.png)
  4. Schedule the job to run every minute. Stop execution after 3 runs
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/OneMinRule.png)
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/Bucket.png)
  5. Check if cloudwatch logs are generated
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CloudWatch.png)

### Question 3:
API gateway - Lambda integration
  1. Modify lambda function to accept parameters and return file name.
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/LambdaAPI.png)
  2. Create a POST API from API Gateway, pass parameters as request body to Lambda job. Return filename and status code as response.
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/Gateway.png)
  3. Consume API from local machine and pass unique data to lambda. 
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/Test.png)
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/Postman.png)
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/BucketOutput.png)
  4. Check if cloudwatch logs are generated
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CloudWatchAPI.png)  
