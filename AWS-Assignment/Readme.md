# AWS Assignment:

## Question 1:

1. Create S3 bucket from AWS CLI
  a. Create an IAM role with S3 full access.
  b. Create an EC2 instance with above role
  c. Create a bucket from AWS CLI
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CreateBucket.png)
  
2. Put files in S3 bucket from lambda
  a. Create custom role for AWS lambda which will have only put object access
  b. Add role to generate and access Cloudwatch logs
  c. In python script, generate json in given format and save json file in bucket created
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/LambdaFunction.png)
  d. Schedule the job to run every minute. Stop execution after 3 runs
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/OneMinRule.png)
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/Bucket.png)
  e. Check if cloudwatch logs are generated
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CloudWatch.png)

3. API gateway - Lambda integration
  a. Modify lambda function to accept parameters and return file name.
  b. Create a POST API from API Gateway, pass parameters as request body to Lambda job. Return filename and status code as response.
  c. Consume API from local machine and pass unique data to lambda. 
  d. Check if cloudwatch logs are generated
