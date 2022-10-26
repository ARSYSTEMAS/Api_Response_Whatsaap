import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as b
# from decimal import Decimal, ROUND_HALF_UP

def Get_information(url,input):
    html = requests.get(url, verify=False)
    statusCode = html.status_code
    content = html.content
    soup = b(content, "html.parser")
    if statusCode == 200:
        try:
            if input == "tasa bcv":
                search = soup.find("div", {"id": "dolar"}, {"class": "col-sm-12 col-xs-12"})
                value = search.text.strip().replace("USD","").replace(" ","")
                P = value.index(",")
                return F'La tasa VES/USD del BCV actualmente es:  {value[0:P+3]}'

            elif input == "tasa monitor":
                search = soup.find("div", {"id": "2"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de EnParaleloVzla actualmente es:    {search[P + 3:I]}'

            elif input == "tasa binance":
                search = soup.find("div", {"id": "28"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Binance actualmente es:  {search[P + 3:I]}'

            elif input == "tasa airtm":
                search = soup.find("div", {"id": "31"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de AirTM actualmente es:  {search[P + 3:I]}'

            elif input == "tasa localbitcoins":
                search = soup.find("div", {"id": "29"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de LocalBitcoins actualmente es:  {search[P + 3:I]}'

            elif input == "tasa reserve":
                search = soup.find("div", {"id": "32"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Reserve actualmente es:  {search[P + 3:I]}'

            elif input == "tasa yadio":
                search = soup.find("div", {"id": "33"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Yadio actualmente es:  {search[P + 3:I]}'

            elif input == "tasa dolar today":
                search = soup.find("div", {"id": "34"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de DolarToday actualmente es:  {search[P + 3:I]}'

            elif input == "tasa mkambio":
                search = soup.find("div", {"id": "36"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Mkambio actualmente es:  {search[P + 3:I]}'

            elif input == "tasa cambios rya":
                search = soup.find("div", {"id": "37"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Cambios RYA actualmente es:  {search[P + 3:I]}'

            elif input == "tasa paypal":
                search = soup.find("div", {"id": "38"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de PAYPAL actualmente es:  {search[P + 3:I]}'

            elif input == "tasa petro":
                search = soup.find("div", {"id": "4"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'La tasa VES/USD de Petro actualmente es:  {search[P + 3:I]}'

            elif input == "promedio":
                # RESERVE
                search_1 = soup.find("div", {"id": "32"}, {"p class": "precio"}).getText()
                P_1 = search_1.index("USD")
                I_1 = search_1.index("CAMBIO")
                TASARESERVE = search_1[P_1 + 3:I_1]

                # MKAMBIO
                search_2 = soup.find("div", {"id": "36"}, {"p class": "precio"}).getText()
                P_2 = search_2.index("USD")
                I_2 = search_2.index("CAMBIO")
                TASAMKAMBIO = search_2[P_2 + 3:I_2]

                # RYA
                search_3 = soup.find("div", {"id": "37"}, {"p class": "precio"}).getText()
                P_3 = search_3.index("USD")
                I_3 = search_3.index("CAMBIO")
                TASARYA = search_3[P_3 + 3:I_3]

                # AIRTM
                search_4 = soup.find("div", {"id": "31"}, {"p class": "precio"}).getText()
                P_4 = search_4.index("USD")
                I_4 = search_4.index("CAMBIO")
                TASAAIRTM = search_4[P_4 + 3:I_4]

                # LOCALBITCOINS
                search_5 = soup.find("div", {"id": "29"}, {"p class": "precio"}).getText()
                P_5 = search_5.index("USD")
                I_5 = search_5.index("CAMBIO")
                TASALOCALBITCOINS = search_5[P_5 + 3:I_5]

                # YADIO
                search_6 = soup.find("div", {"id": "33"}, {"p class": "precio"}).getText()
                P_6 = search_6.index("USD")
                I_6 = search_6.index("CAMBIO")
                TASAYADIO = search_6[P_6 + 3:I_6]

                promedio = float(TASARESERVE.replace(",",".")) + float(TASAMKAMBIO.replace(",","."))  + float(TASARYA.replace(",",".")) + float(TASAAIRTM.replace(",",".")) + float(TASALOCALBITCOINS.replace(",",".")) + float(TASAYADIO.replace(",","."))
                promedio = promedio / 6
                P_P = str(promedio).index(".")
                promedio = str(promedio)[0:P_P + 3]
                return 'El promedio actual para el dolar es: ' + promedio
            else:
                pass

        except requests.exceptions.ConnectTimeout:
            print("Problemas con la conexion e Internet")

        except requests.exceptions.ConnectionError:
            return "Problemas con la comunicacion a la pagina web para extraer la informacion"
    else:
        print("Status Code %d" % statusCode)