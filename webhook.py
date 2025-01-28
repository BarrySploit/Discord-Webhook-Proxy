#Python Discord Webhook Proxy
#Author: BarrySploit

from flask import Flask, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict 
import logging
import json
import time
import requests

elk_url = "https://10.5.20.4:5601/app/security/alerts"
discord_webhook = "https://discord.com/api/webhooks/1326217223647399966/Y4IdrM84zvOo3oJ7tO6oFBW8RLj-CCSIR6K_XfGUvlDDTaY3dsj8FabAZeTPRutcxFMo"
listen_port = 8080

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
                f"description": f"{status}\nView Recent Alerts: {elk_url}"
            }
        ]
    }

    r = requests.post(url={discord_webhook},json=data,headers=headers)
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
    app.run(host="0.0.0.0",port=listen_port)
