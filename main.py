from flask import Flask, request, json
import requests
import response_bot as bot

app = Flask(__name__)

#########################################################################
#                                                                       #
#                 BIENVENIDO CODIGO ABIERTO, SIENTASE LIBRE             #
#                 DE USAR ESTA CODIFICACION PARA MODIFICAR              #
#                 Y MEJORAR ESTE BOT `PARA USO PERSONAL,                #
#                 EMPRESARIAL Y / O COMERCIAL, SIN FINES                #
#                 DE LUCRO.                                             #
#                                                                       #
#########################################################################



#########################################################################
#                           INFORMACION                                 #
#########################################################################
Version_Bot = "1.0.0 Alpha"
datos_Bot = ('Anderson Garcia','23/10/2022','Abi',38,'robot de uso publico para facilitar el dia a dia del venezolano, de uso gratuito y codigo abierto')
creador,fecha_creacion,nombre_Bot,edad_bot,desc_bot = datos_Bot
info = f'Hola mi nombre es {nombre_Bot} soy un {desc_bot} codificado a partir del dia {fecha_creacion} por {creador} '


VERIFY_TOKEN = "anderson"
TOKEN = "Bearer EAAI0NrVoYQoBAMyB7NLSXDyYj1ejIIfK3Bc4A8sg3nFH0ohNEBxs6J83ZCPWJZCaAIvRFzgwkZB92v5BOyO6tUsl7b5aOGlc1RqWpDEPYtzfAmlbagpqPiIMis99cRuHIdeIKOoUDZB7xZBepqBZBHbAypXwGFPqfWfvqjICZAHrvVp8HZCsDGVh"



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
    #"link": "https://digitallzoneve.com/wp-content/uploads/2021/07/4-600x600-1.jpg"
    template_Image = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "584120420838",
        "type": "template",
        "template": {
            "name": "products",
            "language": {
                "code": "es"
            },
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": "https://digitallzoneve.com/wp-content/uploads/2021/07/4-600x600-1.jpg"
                            }
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "currency",
                            "currency": {
                                "fallback_value": 150,
                                "code": "USD",
                                "amount_1000": 15
                            }
                        },

                    ]
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": "0",
                    "parameters": [
                        {
                            "type": "payload",
                            "payload": "a"
                        }
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": "1",
                    "parameters": [
                        {
                            "type": "payload",
                            "payload": "b"
                        }
                    ]
                }
            ]
        }
    }

    response_link = requests.post('https://graph.facebook.com/v13.0/105609815670329/messages', headers=headers,
                             json=template_Image)

@app.route('/webhook', methods = ['POST', 'GET'])

# METODO POST RESPUESTA AL MENSAJE CLIENTE
def webhook():

    if request.method == 'GET':
        # CONEXION CON WEEBHOOK CONFIGURATION METODO GET
        if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
            if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
                return "Verification token mismatch", 403
            return request.args["hub.challenge"], 200

        return "WebHook Configurado...", 200


    elif request.method == 'POST':

        res = request.get_json()
        print(res)
        print(json.dumps(res, indent=4))
        try:

            if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
                msg_body = res["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
                telf_from = res["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
                responseBot = bot.get_response(msg_body)
                send_msg(responseBot,telf_from)
        except:
            pass
        return '200'

if __name__ == '__main__':
    app.run(debug=True)