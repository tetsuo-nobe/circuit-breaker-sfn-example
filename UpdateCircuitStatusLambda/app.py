import json
import boto3
import time

ddbClient = boto3.client("dynamodb")
table_name = "CircuitBreakerPython"
CIRCUIT_STATUS = "OPEN";
EXPIRE_SECONDS = 20;

def lambda_handler(event, context):
    ctime = time.time()
    # クエリー発行
    response = ddbClient.query(
        TableName=table_name,
        KeyConditionExpression='ServiceName = :service_name and ExpireTimeStamp > :current_time',
        ExpressionAttributeValues={
            ':service_name': {"S": event["TargetLambda"]},
            ':current_time': {"N": str(ctime)}
        },
        ConsistentRead = True
    )
    
    if  response["Count"] == 0:
        print("Inside save construct");
        item = {
            "ServiceName": {"S": event["TargetLambda"]},
            "CircuitStatus": {"S": CIRCUIT_STATUS},
            "ExpireTimeStamp":  {"N": str(ctime + EXPIRE_SECONDS)}
        }
        ddbClient.put_item(TableName=table_name, Item=item)

    return {
            "TargetLambda": event["TargetLambda"],
            "CircuitStatus": CIRCUIT_STATUS
    }
    