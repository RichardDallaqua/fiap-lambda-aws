import json
import boto3
import jwt

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'user'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Extract the user ID from the query parameters
    user_id = event['queryStringParameters']['id']

    try:
        # Use the get_item method to retrieve the user by ID
        response = table.get_item(
            Key={
                'id': user_id  # Replace with the name of your primary key attribute
            }
        )
        
        # Check if the item was found
        if 'Item' in response:
            user_data = response['Item']
            return {
                'statusCode': 200,
                'body': jwt.encode(user_data, "secret", algorithm="HS256")
            }
        else:
            return {
                'statusCode': 404,
                'body': 'Ops... '
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
