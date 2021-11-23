import boto3
from boto3.dynamodb.conditions import Key
import json 
from decimal import Decimal
from pwd_functions import get_password_hash

class DecimalEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return json.JSONEncoder.default(self, obj)

def create_user(user_data):
	username = user_data["queryStringParameters"]['username']
	full_name = user_data["queryStringParameters"]['full_name']
	password = user_data["queryStringParameters"]['password']
	hashed_password = get_password_hash(password)
	email = user_data["queryStringParameters"]['email']

	dynamodb = boto3.resource('dynamodb')
		
	table = dynamodb.Table('spam-detection-users')	
	
	user = table.put_item(
		Item={
			'username': username,
			'full_name': full_name,
			'hashed_password': hashed_password,
			'email': email
		}
	)

	return user

def create_user_handler(event, context):
	result = json.dumps(create_user(event))
	return{ "statusCode": 200, "headers": {"Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token","Access-Control-Allow-Credentials":"true","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET"} , "body": result}
