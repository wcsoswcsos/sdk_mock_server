import json

data = {"error_code":0,"msg":"success"}

def report():
    return json.dumps(data)