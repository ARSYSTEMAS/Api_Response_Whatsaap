from flask import Flask, request, json
import requests

app = Flask(__name__)

VERIFY_TOKEN = "anderson"
TOKEN =  "Bearer EAAI0NrVoYQoBAEPdni6XZCRF1BRq5ZBY93cEUsFnOlGl5qxZAmDZCdVvKcWdA1BSEpzUZCsHZAGPW2W1GKFqL4kZBB8TZCPHETlKas2oC5abaZBUMITqi2gRsOrpaZBPTorW0nSxw5Q5ci5ZAYLpZAy7RqVG1TqfulMngjaUT4lPSuaGAxb8dsEPfdOn"
@app.route('/')
def index():
    return "Hello Conexion establecida"

def send_msg(msg):
    headers = {"Authorization":TOKEN,
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

@app.route('/webhook', methods = ['POST', 'GET'])

def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


def webhook():
    res = request.get_json()
    print(res)
    print(json.dumps(res, indent= 4 ))
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            msg_body = res["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
            send_msg("\ud83e\udd1a gracias por responder, tu mensaje es: " + msg_body)
    except:
        pass
    return '200 OK HTTPS.'






if __name__ == '__main__':
    app.run(debug=True)