#Python Discord Webhook Proxy
#Author: BarrySploit

from flask import Flask, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict 
import select
import sys
import re
import logging
import json
import time
import os
import base64
import requests

app = Flask(__name__)

def sendDiscordMessage(message):
    message = message.split(";")
    date = message[0]
    status = "\n".join(message[1:])
    headers = {"Content-Type":"application/json"}

    data = {
        "content": "",
        "embeds": [
            {
                f"title": f"ELK Alert - {date}",
                f"description": f"{status}\nView Recent Alerts: https://10.5.20.4:5601/app/security/alerts"
            }
        ]
    }

    r = requests.post(url="https://discord.com/api/webhooks/1326217223647399966/Y4IdrM84zvOo3oJ7tO6oFBW8RLj-CCSIR6K_XfGUvlDDTaY3dsj8FabAZeTPRutcxFMo",json=data,headers=headers)
    #print(r.status_code)
    if r.status_code != 204:
        print("ERROR SENDING DISCORD NOTIFICATION")
        print(r.status_code)
        print(type(r.status_code))
        print(r.text)
@app.route('/webhook', methods=['POST'])
def post_endpoint():
    message = list(request.form.to_dict().keys())[0].strip('\"')
    sendDiscordMessage(message=message)
    return 'test'

if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host="0.0.0.0",port=8080)
