from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def grafico(janela, pos):

    fig = Figure(figsize=(5, 5),
                 dpi=100)

    x = [0, 2, 5, pos[0]]
    y = [0, 5, 0, pos[1]]

    plt = fig.add_subplot(111)
    plt.scatter(x, y, 200, ['black', 'black', 'black', '#00FFF0'])

    canvas = FigureCanvasTkAgg(fig, janela)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, janela)
    toolbar.update()

    canvas.get_tk_widget().place(x=0, y=0)





