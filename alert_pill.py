import os
import requests
from datetime import datetime

thistime = datetime.now()
text = thistime.strftime("%y/%m/%d - %H:%M")
text = text + " 에 약을 드시길 권해드렸습니다."

url = os.environ.get('SLACK_URL')
url = "https://hooks.slack.com/services/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"

def slack_post_text(url, text):
    result = requests.post(url, json = {"text": text})
    return result

if __name__ == '__main__':
    slack_post_text(url, text)