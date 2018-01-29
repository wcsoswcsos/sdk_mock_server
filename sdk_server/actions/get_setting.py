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
	"preload_4g": true,
	"dfp_splash_duration": 3,
	"ad_settings": [{
		"positionid": 45,
		"max_request_num": 4,
		"preload_material_4g": false
	},
	{
		"positionid": 41,
		"max_request_num": 3,
		"preload_material_4g": true
	},
	{
		"positionid": 38,
		"max_request_num": 3,
		"preload_material_4g": true
	},
	{
		"positionid": 46,
		"max_request_num": 3,
		"preload_material_4g": true
	},
	{
		"positionid": 176,
		"max_request_num": 6,
		"preload_material_4g": false
	},
	{
		"positionid": 42,
		"max_request_num": 1,
		"preload_material_4g": false
	},
	{
		"positionid": 52,
		"max_request_num": 3,
		"preload_material_4g": true
	},
	{
		"positionid": 50,
		"max_request_num": 3,
		"preload_material_4g": true
	}],
	"ad_join_id": "195F16FA-DF62-4F18-83A2-6E5F58DEE193",
	"timestamp": 1516859612,
	"preload_wifi": true
}
def get_setting(request):
    return json.dumps(data)