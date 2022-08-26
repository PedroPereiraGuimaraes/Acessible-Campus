import matplotlib.pyplot as plt

from main import triangulacao


def grafico(pos):

    x = [0,2,5,pos[0]]
    y = [0,5,0,pos[1]]

    plt.scatter(x,y,200,['black','black','black','#00FFF0'])
    plt.show()


rssi0_0=-65.05149978319906
rssi2_5=-56.98970004336019
rssi0_5=-62.30448921378274





grafico(triangulacao(0,0,rssi0_0,2,5,rssi2_5,0,5,rssi0_5))