import json

def lambda_handler(event, context):
    print("invoked Payment")
    print(event)
    order = event["order"]
    message = "Payment process is completed:  "  + json.dumps(order)
    print(message)
    # return {
    #         "message": message
    # }