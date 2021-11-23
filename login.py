import boto3
from boto3.dynamodb.conditions import Key
import json 
from decimal import Decimal
from pwd_functions import verify_password

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

def get_user(user_data):
    usern = user_data["queryStringParameters"]['username']
    pwd = user_data["queryStringParameters"]['password']
    #hashed_password

    dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('spam-detection-users')    
    
    users = table.query(
        KeyConditionExpression=Key('username').eq(usern)
    )
                
    if 'Items' in users:
        if len(users['Items']) >= 1:
            if verify_password(pwd,users['Items'][0]['hashed_password']):
                return {"users":[users['Items'][0]]}
    return {"users":[{}]}

def login_handler(event, context):
    user = get_user(event)
    result = json.dumps(user, cls=DecimalEncoder)
    return{ "statusCode": 200, "headers": {"Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token","Access-Control-Allow-Credentials":"true","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET"} , "body": result}
