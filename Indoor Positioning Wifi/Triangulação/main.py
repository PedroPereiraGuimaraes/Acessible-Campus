
##Para o correto funcionamento da função é necessario que sejam
##colocados em ordem de Beacon1[x,y,rssi], Beacon2[x,y,rssi], Beacon3[x,y,rssi]
def triangulacao(x1, y1, rssi1, x2, y2, rssi2, x3, y3, rssi3):

    ##Referencia ao rssi em 1 metro
    dbm = -61
    ##Referente ao path loss devido ao ambiente. Em um local aberto o path loss é aproximadamente 2
    pathLoss = 2

    ##Calculo da distancia pelo rssi
    r1 = 10**((rssi1-dbm)/(-10*pathLoss))
    print(r1)
    r2 = 10**((rssi2-dbm)/(-10*pathLoss))
    r3 = 10**((rssi3-dbm)/(-10*pathLoss))

    ##Fazendo os calculos da triangulação por simplificação
    a = 2 * (-x1 + x2)
    b = 2 * (-y1 + y2)
    c = (r1 ** 2) - (r2 ** 2) - (x1 ** 2) + (x2 ** 2) - (y1 ** 2) + (y2 ** 2)
    d = 2 * (-x2 + x3)
    e = 2 * (-y2 + y3)
    f = (r2 ** 2) - (r3 ** 2) - (x2 ** 2) + (x3 ** 2) - (y2 ** 2) + (y3 ** 2)

    x = 10000
    y = 10000

    ##Calculando as coordenadas de x e y do dispositivo
    if ((e * a) - (b * d)) == 0 & ((b * d) - (a * e)) == 0:
        x = 0
        y = 0
    elif(((e*a) - (b*d)) == 0):
        y = ((c * d) - (a * f)) / ((b * d) - (a * e))
        x=0
    elif(((b * d) - (a * e)) == 0):
        x = ((c * e) - (f * b)) / ((e * a) - (b * d))
        y = 0
    else:
        x = ((c * e) - (f * b)) / ((e * a) - (b * d))
        y = ((c * d) - (a * f)) / ((b * d) - (a * e))

    return x,y



if __name__ == '__main__':
    ##Mostrando a posição do dispositivo
    print(triangulacao(0,0,7,8,12,10,-8,12,10))
