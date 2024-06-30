import requests
import sys
import os


virus_total_url = 'https://www.virustotal.com/vtapi/v2/file/scan'


def get_file_path():
    file_path = input('Insert file path : ')
    return file_path


def is_file_valid(file_path):
    return os.path.isfile(file_path)


def get_virus_total_api_key():
    virus_total_api_key = input('Insert api key : ')
    return virus_total_api_key


def upload_file_to_virus_total(api_key, file_path):
    global virus_total_url

    params = {'apikey': api_key}
    file_to_upload = {'file': open(file_path, 'rb')}

    response = requests.post(url=virus_total_url, files=file_to_upload, params=params)

    if response.status_code == 200:
        print(response.text)


upload_file_to_virus_total("c3617cd08f4a4582899ab2a6cc1e96bd43f370ac3e37a9a1918dbe94cd44eebf", "C:\\Users\\shai\\Desktop\\t.txt")
