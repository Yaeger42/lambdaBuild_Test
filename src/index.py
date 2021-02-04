import boto3


def lambda_handler(event=None, context=None):
    
    data = event["Details"]["Parameters"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('US_BANK_SubscribableEvents') 
    
    response = response = table.put_item(
       Item={
            'uuid': event["Details"]["ContactData"]["ContactId"],
            'completed': 'false',
            'fname': data["fname"],
            'transactions_length': "0",
            'transactions': []
        }
    )
    print(response)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('US_BANK_SubscribableEvents')

    response = table.update_item(
        Key={
            'uuid': 'test',
        },
        UpdateExpression="set completed=:r, transactions=:p, transactions_length=:a",
        ExpressionAttributeValues={
            ':r': "false", 
            ':p': [],
            ':a': '0'
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
