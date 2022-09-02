import math

##Para o correto funcionamento da função é necessario que sejam
##colocados em ordem de Beacon1[x,y,rssi], Beacon2[x,y,rssi], Beacon3[x,y,rssi]
def triangulacao(x1, y1, rssi1, x2, y2, rssi2, x3, y3, rssi3):

    raio1 = rssiParaDistancia(rssi1)
    raio2 = rssiParaDistancia(rssi2)
    raio3 = rssiParaDistancia(rssi3)

    print("Distancia R1: ")
    print(round(raio1,2))
    print("Distancia R2: ")
    print(round(raio2,2))
    print("Distancia R3: ")
    print(round(raio3,2))

    ##Fazendo os calculos da triangulação por simplificação
    a = 2 * (-x1 + x2)
    b = 2 * (-y1 + y2)
    c = (raio1 ** 2) - (raio2 ** 2) - (x1 ** 2) + (x2 ** 2) - (y1 ** 2) + (y2 ** 2)
    d = 2 * (-x2 + x3)
    e = 2 * (-y2 + y3)
    f = (raio2 ** 2) - (raio3 ** 2) - (x2 ** 2) + (x3 ** 2) - (y2 ** 2) + (y3 ** 2)

    x = 10000
    y = 10000

    ##Calculando as coordenadas de x e y do dispositivo
    if ((e * a) - (b * d)) == 0 & ((b * d) - (a * e)) == 0:
        x = 0
        y = 0
    elif((e*a) - (b*d)) == 0:
        y = ((c * d) - (a * f)) / ((b * d) - (a * e))
        x=0
    elif((b * d) - (a * e)) == 0:
        x = ((c * e) - (f * b)) / ((e * a) - (b * d))
        y = 0
    else:
        x = ((c * e) - (f * b)) / ((e * a) - (b * d))
        y = ((c * d) - (a * f)) / ((b * d) - (a * e))

    return x, y

def rssiParaDistancia(rssi):

    ## Rssi por um metro
    a = -50
    ## Rssi - Rssi/metro dividido pelo PathLoss
    w = (rssi - a) / -20
    ## Calculo do Log(distancia)
    distancia = 10 ** w

    return distancia

def distanciaParaRssi(distancia):

    rssi = -50 - 20*math.log(distancia,10)
    return rssi

