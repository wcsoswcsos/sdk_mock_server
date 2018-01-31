import json

data = {
	"ad_network_id": "mt_fallback",
	"date": "20180125",
	"ad_idea_id_infos": [{
		"tracking_url": [],
		"click_tracking_url": [],
		"show_times": ["1516809600-1516896000"],
		"ad_idea_id": "8836"
	}],
	"ad_data_infos": [{
		"ad_data": {
			"tracking_url": [],
			"ad_imp_type": 3,
			"cache_expires": 1516896000,
			"render_info": {
				"content_base_size": "411x553",
				"clip_area": "47,0,48,0",
				"adjustment_padding": "0,0,120,0",
				"background": "http:\/\/mea.meitudata.com\/5503ac1215cdd54f9c0c06a9950768c5_1440*1920?imageView\/1\/format\/webp\/w\/1080\/h\/1920",
				"extra_configs": {
					"duration": 3
				},
				"color_index": 0,
				"preferred_ad_size": "411x553",
				"elements": [{
					"resource": "http:\/\/mea.meitudata.com\/f5e70aef39849e7f059c4b0e66322419-3194.gif",
					"position": "0,0,411,553",
					"element_type": 2,
					"background_color": "",
					"click_tracking_url": [],
					"link_instructions": "mtbusinesskit:\/\/lint?type=3&jump_id=0&event_id=main&event_type=1&jump_scheme=scheme%3A+meituxiuxiu%3A%2F%2Fsketchselfie%3F1011_1014&backup_url=https%3A%2F%2Fwww.meitu.com%2F&is_mt=0&backup_url_type=1"
				}],
				"adjustment_style": 4
			},
			"report_info": {
				"ad_entity_type": "0",
				"ad_score": 0,
				"ad_position_id": "38",
				"ad_entity_id": "0",
				"ad_algo_id": "0",
				"ad_owner_id": "24",
				"ad_position_type": "1",
				"ad_cost": 0,
				"ad_position_sub_id": 0,
				"ad_join_id": "6F7E646A-F7D8-42DC-BF84-6EC3F553CB6A",
				"ad_type": "3",
				"charge_type": "CPM"
			}
		},
		"ad_idea_id": "8836"
	}],
	"ad_id": "69825",
	"ad_sale_type": 2
}


def load_data():
    return json.dumps(data)