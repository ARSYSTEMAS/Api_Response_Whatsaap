from flask import Flask, request, json
import requests

app = Flask(__name__)


VERIFY_TOKEN = ""
TOKEN =  ""

@app.route('/')
def index():
    return "Hello Conexion establecida"

def send_msg(msg,msg_from):
    headers = {"Authorization":TOKEN,
               "Content-Type": "application/json",
               }
    json_data = {
        'messaging_product': 'whatsapp',
        'to': msg_from,
        'type': 'text',
        "text": {
            "body": msg
        }
    }
    response = requests.post('https://graph.facebook.com/v13.0/105609815670329/messages', headers=headers,
                             json=json_data)


@app.route('/webhook', methods = ['POST', 'GET'])

def webhook():
    res = request.get_json()
    print(res)
    print(json.dumps(res, indent=4))
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            msg_body = res["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
            msg_from = res["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
            send_msg("\ud83e\udd1a gracias por responder, tu mensaje es: " + msg_body,msg_from)
    except:
        pass
    return '200'

def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "WebHook Configurado...", 200





if __name__ == '__main__':
    app.run(debug=True)