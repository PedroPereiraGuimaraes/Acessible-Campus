import requests
import time


def distancia():
    time.sleep(1)
    resposta = requests.get('http://192.168.0.100/')
    dados = resposta.text
    dados = int(dados)

    print(f"{dados} dbm")
    print(f"{round(rssiParaDistancia(dados),4)} metros")

    return rssiParaDistancia(dados)


def rssiParaDistancia(rssi):
    ## Rssi por um metro
    a = -35
    ## Rssi - Rssi/metro dividido pelo PathLoss
    w = (rssi - a) / -20
    ## Calculo do Log(distancia)
    distancia = 10 ** w

    return distancia

