import requests,datetime
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as b
# from decimal import Decimal, ROUND_HALF_UP

today = datetime.datetime.now().date()

def extract_information(url,command):
    global today
    html = requests.get(url, verify=False)
    statusCode = html.status_code
    content = html.content
    soup = b(content, "html.parser")
    if statusCode == 200:
        try:
            if command == "tasa bcv":
                search = soup.find("div", {"id": "dolar"}, {"class": "col-sm-12 col-xs-12"})
                value = search.text.strip().replace("USD","").replace(" ","")
                P = value.index(",")
                return F'\u270d\ufe0fLa tasa VES/USD del BCV actualmente es:  {value[0:P+3]}'

            elif command == "tasa monitor":
                search = soup.find("div", {"id": "2"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                MONITOR = search[P + 3:I]
                return f'\u270d\ufe0fLa tasa VES/USD de EnParaleloVzla actualmente es:    {search[P + 3:I]}'

            elif command == "tasa binance":
                search = soup.find("div", {"id": "28"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Binance actualmente es:  {search[P + 3:I]}'

            elif command == "tasa airtm":
                search = soup.find("div", {"id": "31"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de AirTM actualmente es:  {search[P + 3:I]}'

            elif command == "tasa localbitcoins":
                search = soup.find("div", {"id": "29"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de LocalBitcoins actualmente es:  {search[P + 3:I]}'

            elif command == "tasa reserve":
                search = soup.find("div", {"id": "32"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Reserve actualmente es:  {search[P + 3:I]}'

            elif command == "tasa yadio":
                search = soup.find("div", {"id": "33"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Yadio actualmente es:  {search[P + 3:I]}'

            elif command == "tasa dolar today":
                search = soup.find("div", {"id": "34"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de DolarToday actualmente es:  {search[P + 3:I]}'

            elif command == "tasa mkambio":
                search = soup.find("div", {"id": "36"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Mkambio actualmente es:  {search[P + 3:I]}'

            elif command == "tasa cambios rya":
                search = soup.find("div", {"id": "37"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Cambios RYA actualmente es:  {search[P + 3:I]}'

            elif command == "tasa paypal":
                search = soup.find("div", {"id": "38"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de PAYPAL actualmente es:  {search[P + 3:I]}'

            elif command == "tasa petro":
                search = soup.find("div", {"id": "4"}, {"p class": "precio"}).getText()
                P = search.index("USD")
                I = search.index("CAMBIO")
                return f'\u270d\ufe0fLa tasa VES/USD de Petro actualmente es:  {search[P + 3:I]}'

            elif command == "promedio" or command == "tasas":
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

                # ENPARALELOVZLA
                search_7 = soup.find("div", {"id": "2"}, {"p class": "precio"}).getText()
                P_7 = search_7.index("USD")
                I_7 = search_7.index("CAMBIO")
                ENPARALELOVZLA = search_7[P_7 + 3:I_7]

                promedio = float(TASARESERVE.replace(",",".")) + float(TASAMKAMBIO.replace(",","."))  + float(TASARYA.replace(",",".")) + float(TASAAIRTM.replace(",",".")) + float(TASALOCALBITCOINS.replace(",",".")) + float(TASAYADIO.replace(",","."))
                promedio = promedio / 6
                P_P = str(promedio).index(".")
                promedio = str(promedio)[0:P_P + 3]

                if command == "promedio":
                    return f'{today }: El promedio actual para el dolar es: ' + promedio
                else:

                    tasas = (f'\ud83d\udcdd{today}:\n'
                                     f'\ud83d\udcccRESERVE                   = {TASARESERVE}\n'
                                     f'\ud83d\udcccAIRTM                        = {TASAAIRTM}\n'
                                     f'\ud83d\udcccLOCALBITCOINS      = {TASALOCALBITCOINS}\n'
                                     f'\ud83d\udcccMKAMBIO                 = {TASAMKAMBIO}\n'
                                     f'\ud83d\udcccCAMBIOS RYA          = {TASARYA}\n'
                                     f'\ud83d\udcccYADIO                        = {TASAYADIO}\n'
                                     f'\ud83d\udcccENPARALELOVZLA = {ENPARALELOVZLA}\n'
                                     f'\ud83d\udcccENPARALELOVZLA = {ENPARALELOVZLA}\n'
                                     f'\ud83d\udea7 Tasas Actualizada en linea \ud83d\udea7')
                    return tasas



            elif command == "criptos":

                # BTC
                search_7 = soup.find("div", {"id": "BTCUSD"}, {"p class": "precio"}).getText()
                P_7 = search_7.index("BTC")
                I_7 = search_7.index("CAMBIO")
                BTC = search_7[P_7 + 3:I_7]

                # Ethereum
                search_8 = soup.find("div", {"id": "ETHUSD"}, {"p class": "precio"}).getText()
                P_8 = search_8.index("ETH")
                I_8 = search_8.index("CAMBIO")
                ETH = search_8[P_8 + 3:I_8]


                # XRP
                search_9 = soup.find("div", {"id": "XRPUSD"}, {"p class": "precio"}).getText()
                P_9 = search_9.index("XRP0")
                I_9 = search_9.index("CAMBIO")
                XRP = search_9[P_9 + 3:I_9]


                # Tether
                search_10 = soup.find("div", {"id": "USDTUSD"}, {"p class": "precio"}).getText().replace(" ","")
                P_10 = search_10.index("USDT")
                I_10 = search_10.index("CAMBIO")
                USDT = search_10[P_10 + 4:I_10]

                # Dogecoin
                search_11 = soup.find("div", {"id": "DOGEUSD"}, {"p class": "precio"}).getText().replace(" ", "")
                P_11 = search_11.index("DOGE")
                I_11 = search_11.index("CAMBIO")
                DOGECOIN = search_11[P_11 + 4:I_11]

                # Dai
                search_12 = soup.find("div", {"id": "DAIUSD"}, {"p class": "precio"}).getText().replace(" ", "")
                P_12 = search_12.index("DAI")
                I_12 = search_12.index("CAMBIO")
                DAI = search_12[P_12 + 3:I_12]

                # SHIBA INU
                search_13 = soup.find("div", {"id": "SHIBUSD"}, {"p class": "precio"}).getText().replace(" ", "")
                P_13 = search_13.index("SHIB0")
                I_13 = search_13.index("CAMBIO")
                SHIBA = search_13[P_13 + 4:I_13]

                # LITECOINS
                search_14 = soup.find("div", {"id": "LTCUSD"}, {"p class": "precio"}).getText().replace(" ", "")
                P_14 = search_14.index("LTC")
                I_14 = search_14.index("CAMBIO")
                LTC = search_14[P_14 + 3:I_14]

                # AXS
                search_15 = soup.find("div", {"id": "AXSUSD"}, {"p class": "precio"}).getText().replace(" ", "")
                P_15 = search_15.index("AXS")
                I_15 = search_15.index("CAMBIO")
                AXS = search_15[P_15 + 3:I_15]

                criptomonedas = (f'\ud83d\udcdd{today}:\n'
                                 f' \ud83d\udcb9BITCOIN    = {BTC} \n '
                                 f'\ud83d\udcb9ETHERUM =  {ETH} \n '
                                 f'\ud83d\udcb9XRP           =  {XRP} \n '
                                 f'\ud83d\udcb9TETHER    =  {USDT} \n '
                                 f'\ud83d\udcb9DOGE        =  {DOGECOIN} \n '
                                 f'\ud83d\udcb9DAI            =  {DAI} \n '
                                 f'\ud83d\udcb9SHIBA      =  {SHIBA} \n '
                                 f'\ud83d\udcb9LTC           =  {LTC} \n '
                                 f'\ud83d\udcb9AXS          =  {AXS} \n '
                                 f'\ud83d\udea7 Tasas Actualizada en linea \ud83d\udea7'
                                 )

                return criptomonedas
            else:
                pass
        except requests.exceptions.ConnectTimeout:
            print("Problemas con la conexion e Internet")

        except requests.exceptions.ConnectionError:
            return "Problemas con la comunicacion a la pagina web para extraer la informacion"
    else:
        return("Status Code %d" % statusCode)



def searchID(param: str):
    url_2= "http://www.cne.gob.ve/web/js/re.php"
    nac= "V"
    url = f"http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad={nac}&cedula={param},true"

    html = requests.get(url, verify=False)
    statusCode = html.status_code
    content = html.content
    soup = b(content, "html.parser")
    if statusCode == 200:
        try:
            search_data = soup.text.replace("\n","")
            P_nombre = search_data.index("Nombre:")
            I_nombre = search_data.index("Estado:")

            P_estado = search_data.index("Estado:")
            I_estado = search_data.index("Municipio:")

            P_cedula = search_data.index("Cédula:")
            I_cedula = search_data.index("Nombre:")

            P_municipio = search_data.index("Municipio:")
            I_municipio = search_data.index("Parroquia:")


            NOMBRE = search_data[P_nombre + 7:I_nombre]
            ESTADO = search_data[P_estado + 7:I_estado]
            CEDULA = search_data[P_cedula + 7:I_cedula]
            MUNICIPIO = search_data[P_municipio + 10:I_municipio]

            data = (f'\ud83d\udd0d Datos encontrados:\n'
                f'\ud83d\udd34NOMBRE = {NOMBRE} \n '
                f'\ud83d\udd34ESTADO      = {ESTADO} \n '
                f'\ud83d\udd34MUNICIPIO  = {MUNICIPIO} \n '
                f'\ud83d\udd34CEDULA    = {CEDULA} \n '
                         )
        except ValueError:
            return "\u274cCedula not found\u274c"
        return data
    else:
        return ("Status Code %d" % statusCode)
