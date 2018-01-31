import json

data = {"error_code":0,"msg":"success"}

def report_data():
    return json.dumps(data)