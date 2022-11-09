from flask import Flask, request, json
from PIL import Image
import requests
import base64
import response_bot as bot
import mimetypes

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
TOKEN        = "Bearer EAAI0NrVoYQoBAMyB7NLSXDyYj1ejIIfK3Bc4A8sg3nFH0ohNEBxs6J83ZCPWJZCaAIvRFzgwkZB92v5BOyO6tUsl7b5aOGlc1RqWpDEPYtzfAmlbagpqPiIMis99cRuHIdeIKOoUDZB7xZBepqBZBHbAypXwGFPqfWfvqjICZAHrvVp8HZCsDGVh"
LINK         = ''


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

    image_template = {
        'messaging_product': 'whatsapp',
        "recipient_type": "individual",
        'to': msg_from,
        'type': 'image',
        "image": {
            "id": id
        }
    }

    response_link = requests.post('https://graph.facebook.com/v14.0/105609815670329/messages', headers=headers,
                             json=json_data)

def upload_media_content():

    image_file = 'img/persona.jpg'

    with open(image_file, "rb") as f:
        im_bytes = f.read()

    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    #print(im_b64)

    url = "https://graph.facebook.com/v14.0/105609815670329/media"

    payload = {'messaging_product': 'whatsapp'}

    files = [
        ('file', ('persona.jpg', open('img/persona.jpg', 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Authorization': TOKEN
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)


    res = response.json()
    id = res["id"]
    return id


def dowmload_media_content(id):


    url = "https://graph.facebook.com/v15.0/"+id


    payload = {}
    headers = {
        'Authorization': TOKEN
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    res = response.json()
    url_image = res["url"]



    response_url = requests.request("GET", url_image, headers=headers, data=payload)


    if response_url.status_code == 200:

        folder='img/'
        url_imagen = response_url.url
        nombre_local_imagen = folder+id+".jpg"

        imagen = requests.get(url_imagen).content

        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)

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

            type_ = res["entry"][0]["changes"][0]["value"]["messages"][0]["type"]


            if type_ == "text":
                msg_body   = res["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
                telf_from  = res["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
                contacts   = res["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]
            else:
                id_image = res["entry"][0]["changes"][0]["value"]["messages"][0]["image"]["id"]
                dowmload_media_content(id_image)


            responseBot = bot.get_response(msg_body)
            responseBot = responseBot.replace("@name", contacts)
            #identifier= upload_media_content()
            send_msg(responseBot,telf_from)
        except:
            pass
        return '200'

if __name__ == '__main__':
    app.run(debug=True)