import boto3 
from io import BytesIO
import joblib
import json 

def get_model(model):
	with BytesIO() as f:
		if model == '/mlpclassifiers':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_MLPClassifier.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/kneighbors':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_KNeighbors.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/decisiontrees':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_DecisionTree.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/randomforests':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_RandomForest.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		else:
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_MLPClassifier.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		
		
	return model


import re
def preprocessor(text):
	text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
	emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
	text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
	return text


def classify_message(message):
	path= preprocessor(message["path"]).replace(" ", "")
	message = message["queryStringParameters"]['message']
	model = get_model(path)
	#preprocess message like during the training
	message = preprocessor(message)
	#predict
	label = model.predict([message])[0]
	#calculate probability
	spam_prob = model.predict_proba([message])
	#return 'This message is: ' + label + ' with probability of being spam of: ' + str(spam_prob[0][1])
	return {path: [ {"id": 1, "label":label,"message": message, "spamprob":spam_prob[0][1],"model":path } ] }


def lambda_handler(event, context):
	result = json.dumps(classify_message(event))
	return{ "statusCode": 200, "headers": {"Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token","Access-Control-Allow-Credentials":"true","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET"} , "body": result}