import boto3 


#demo_table = resource('dynamodb').Table('FUTURE_TICKS')
#response = demo_table.in

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FUTURE_TICKS')
table.put_item()


print(table)