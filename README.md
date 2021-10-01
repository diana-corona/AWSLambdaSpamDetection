# FastAPISpamDetection

### Spam Text Message Classification Data
Obtained from

https://www.kaggle.com/team-ai/spam-text-message-classification

### Trainning 
The data was preprocessed by 
1. Removing HTML markup tags
1. Removing punctuation marks
1. Removing capital letters

The model was trainned using MLPClassifier
1. TFIDF vectorizer
1. 700 hidden layers 
1. Relu activation function
1. Adam Optimization Algorithm 
1. Constant learning rate

MLPClassifier

https://scikit-learn.org/stable/modules/neural_networks_supervised.html

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

Test
1. Once deployed, the lambda function can be tested by running
```
curl -X POST <url> -d  <message>
```
for example
```
curl -X POST https://url.amazonaws.com/dev/classify_message -d  "Is this spam?"
```


