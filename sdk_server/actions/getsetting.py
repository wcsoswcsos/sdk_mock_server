import json

data = {
	"splash_delay": {
		"meitu": 2,
		"other": 2
	},
	"hot_splash_interval": 1800,
	"hot_frequency": 3,
	"region": {
		"country": "中国",
		"city": "北京",
		"province": "北京",
		"area_code": "10267",
		"city_code": "10267"
	},
	"preload_4g": True,
	"dfp_splash_duration": 3,
	"ad_settings": [
	{
		"positionid": 50,
		"max_request_num": 3,
		"preload_material_4g": True
	}],
	"ad_join_id": "195F16FA-DF62-4F18-83A2-6E5F58DEE193",
	"timestamp": 1516859612,
	"preload_wifi": True
}
def setting_data():
    return json.dumps(data)