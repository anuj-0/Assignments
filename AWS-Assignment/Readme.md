# AWS Assignment:

### Question 1:

1. Create S3 bucket from AWS CLI
  1. Create an IAM role with S3 full access.
  2. Create an EC2 instance with above role
  3. Create a bucket from AWS CLI
  ![alt text](https://github.com/anuj-0/Assignments/blob/main/AWS-Assignment/Screenshots/CreateBucket.png)
 
### Question 2:
2. Put files in S3 bucket from lambda
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
3. API gateway - Lambda integration
  1. Modify lambda function to accept parameters and return file name.
  2. Create a POST API from API Gateway, pass parameters as request body to Lambda job. Return filename and status code as response.
  3. Consume API from local machine and pass unique data to lambda. 
  4. Check if cloudwatch logs are generated
