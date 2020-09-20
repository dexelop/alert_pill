import os
import requests

url = os.environ.get('SLACK_URL')

def slack_post_text(url, text):
    result = requests.post(url, json = {"text": text})
    return result