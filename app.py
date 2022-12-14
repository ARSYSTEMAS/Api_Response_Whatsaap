from flask import Flask, request, json
import requests

app = Flask(__name__)

VERIFY_TOKEN = ""

@app.route('/webhook', methods = ['POST', 'GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200