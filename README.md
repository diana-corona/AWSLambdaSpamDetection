# AWS Lambda SpamDetection

### Spam Text Message Classification Data
Obtained from

https://www.kaggle.com/team-ai/spam-text-message-classification

### Trainning 
https://github.com/diana-corona/FastAPISpamDetection/tree/AWSLambda

### Create AWS lambda
1. Install serverless https://www.serverless.com/framework/docs/getting-started/
1. Install serverless-python-requirements https://www.serverless.com/plugins/serverless-python-requirements
1. Install aws cli https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
1. Configure aws credentials https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

In AWS
1. Create a s3 bucket 
1. Upload the trained model to ```model/spam_classifier.joblib```
1. Create a lambda function < classify_message_lambda > with python3.7


In the serverless.yml
1. Replace service name
1. Replace the bucket name 

Deploy 
1. In the /app folder, run 'serverless deploy' to upload the lambda function to aws

### Create a custom authenticator
1. To Use/Create API Gateway Lambda authorizers follow: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html
2. To test the authorizer with postman follow: https://docs.aws.amazon.com/apigateway/latest/developerguide/call-api-with-api-gateway-lambda-authorization.html

