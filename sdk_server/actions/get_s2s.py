import json

err_data = {
	"error_code": 3101,
	"msg": "ad engine result code 312"
}

def  get_s2s():
    return json.dumps(err_data)