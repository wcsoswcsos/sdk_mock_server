import json

data = {
	"ad_network_id": "mt_brand",
	"ad_idea_id_infos": [{
		"ad_idea_id": "106"
	}],
	"date": "20170830",
	"ad_data_infos": [{
		"ad_data": {
			"tracking_url": ["http://www.impressiontracking.com"],
			"ad_imp_type": 5,
			"cache_expires": 1504108800,
			"render_info": {
				"content_base_size": "375x667",
				"adjustment_padding": "0,0,0,0",
				"preferred_ad_size": "1000x1000",
				"background": "",
				"elements": [{
					"resource": "http://stage.meitudata.com/meitu-ecom-advert/378aaf74fccdf349fc003bb283bb6c20-3263.jpg?imageView2/2/format/webp",
					"position": "0,0,1024,768",
					"element_type": 2,
					"background_color": "",
					"click_tracking_url": ["http://clicktrackingurl.com"],
					"link_instructions": ""
				}],
				"adjustment_style": 5
			},
			"report_info": {
				"ad_entity_type": "0",
				"ad_score": 0,
				"ad_position_id": "10138",
				"ad_entity_id": "0",
				"ad_algo_id": "0",
				"ad_owner_id": "9",
				"ad_position_type": "1",
				"ad_cost": 0,
				"ad_position_sub_id": 0,
				"ad_join_id": "101381504058908948658381",
				"ad_type": "1"
			}
		},
		"ad_idea_id": "106"
	}],
	"ad_id": "417",
	"ad_sale_type": 1
}

def webview_data():
    return json.dumps(data)