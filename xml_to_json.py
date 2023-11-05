# function call for XML to JSON API
import requests

def convert_xml_to_json(xml_data=None, xml_url=None):
    api_url = 'https://api.factmaven.com/xml-to-json'  # Updated API endpoint
    payload = {'xmlData': xml_data, 'xmlUrl': xml_url}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # Added headers for form data
    response = requests.post(api_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Usage:
json_data = convert_xml_to_json(xml_data='<root><child>data</child></root>')  # or xml_url='https://example.com/feed.xml'
