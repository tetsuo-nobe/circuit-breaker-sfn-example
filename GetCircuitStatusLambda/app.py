import json
import boto3
import time

ddbClient = boto3.client("dynamodb")
table_name = "CircuitBreakerPython"

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
    print(response)
    if response["Count"] != 0:
        status = response["Items"][0]["CircuitStatus"]["S"]
    else:
        status = ""

    return {
            "TargetLambda": event["TargetLambda"],
            "CircuitStatus": status
    }
    