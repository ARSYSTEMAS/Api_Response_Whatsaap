from flask import Flask, request, json
import requests

app = Flask(__name__)

VERIFY_TOKEN = "anderson"

@app.route('/webhook', methods = ['POST', 'GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200




'''
@app.route('/')
def index():
    return "Hello"


def send_msg(msg):
    headers = {"Authorization":"Bearer EAAI0NrVoYQoBAEPdni6XZCRF1BRq5ZBY93cEUsFnOlGl5qxZAmDZCdVvKcWdA1BSEpzUZCsHZAGPW2W1GKFqL4kZBB8TZCPHETlKas2oC5abaZBUMITqi2gRsOrpaZBPTorW0nSxw5Q5ci5ZAYLpZAy7RqVG1TqfulMngjaUT4lPSuaGAxb8dsEPfdOn",
               "Content-Type": "application/json",
               }
    json_data = {
        'messaging_product': 'whatsapp',
        'to': '584120420838',
        'type': 'text',
        "text": {
            "body": msg
        }
    }
    response = requests.post('https://graph.facebook.com/v13.0/105609815670329/messages', headers=headers,
                             json=json_data)
    print(response.text)


@app.route('/recibir', methods=['POST', 'GET'])
def webhook():
    print("1. ",request)
    res = request.get_json()
    req = request.get_json(silent=True, force=True)
    print("2 . ",res)
    print("3 - ",json.dumps(req, indent=4))
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            send_msg("gracias por responder OK")
    except:
        pass
    return '200 OK HTTPS.'
'''

if __name__ == '__main__':
    app.run(debug=True)
