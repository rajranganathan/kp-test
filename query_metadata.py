#!/usr/bin/env python

'''
Program to query AWS EC2 Instance's metadata and display the outputs in JSON format.
'''

import json
import requests


# Function called to collect Metadata
def collect_metadata(url,path):
    for metadata_path in requests.get(url).text.split('\n'):
        metadata_url_path = '{0}{1}'.format(url,metadata_path)
        if metadata_path.endswith('/'):
            metadata_subpath = metadata_path.split('/')[-2]
            path[metadata_subpath] = {}
            collect_metadata(metadata_url_path, path[metadata_subpath])
        else:
            response = requests.get(metadata_url_path)
            if response.status_code != 404:
                try:
                    path[metadata_path] = json.loads(response.text)
                except ValueError:
                    path[metadata_path] = response.text
            else:
                path[metadata_path] = ""

# Main function to get metadata in Json format
def get_metadata():
    metadata_url = 'http://169.254.169.254/latest'
    metadata_dict = {'COLLECTED-METADATA': {}}
    collect_metadata('{0}/{1}/'.format(metadata_url,'meta-data'),metadata_dict['COLLECTED-METADATA'])
    return metadata_dict

print(json.dumps(get_metadata(),indent=4, sort_keys=True))
