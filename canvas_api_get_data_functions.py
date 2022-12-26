import json
import requests

API_KEY = #Your key for accessing the Canvas Live API goes here
URL = #Here is where the URL goes! A sample one I've used recently: "https://stfrancis.instructure.com:443/api/v1/courses/1174984/discussion_topics?include[]=all_dates&order_by=title?page_views?per_page=100"

def grab_all_canvas_data_requested_and_write_json_file(api_key, url, filename):
    data_set = []
    header_argument = {"Authorization": "Bearer " + api_key}
    r = requests.get(URL, headers=header_argument)
    raw = r.json()

    while r.links['current']['url'] != r.links['last']['url']:
        r = requests.get(r.links['next']['url'], headers=header_argument)
        raw = r.json()
        for entry in raw:
            data_set.append(entry)

    with open(f"/Users/spicy.kev/Desktop/{filename}", 'w') as f:
        json.dump(data_set, f)

grab_all_canvas_data_requested_and_write_json_file(API_KEY, URL, 'assignment_json_test.json')