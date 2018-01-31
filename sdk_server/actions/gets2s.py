import json

err_data = {
	"error_code": 3101,
	"msg": "ad engine result code 312"
}

def  s2s_data():
    return json.dumps(err_data)