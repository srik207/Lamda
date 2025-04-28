import json

def lambda_handler(event, context):

    Print("Hello World from lamda")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
