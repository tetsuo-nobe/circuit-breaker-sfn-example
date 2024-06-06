import json
import time

def lambda_handler(event, context):
    print("invoked TestCircuitBreaker")
    print(event)
    time.sleep(12)
    order = event["order"]
    message = "Payment process is completed:  "  + json.dumps(order)
    print(message)
    # return {
    #         "message": message
    # }