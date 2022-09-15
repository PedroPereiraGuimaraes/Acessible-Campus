from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def grafico(janela, pos):
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    x = [2.5, 2.5]
    y = [0, pos]

    plt = fig.add_subplot(111)
    plt.scatter(x, y, 200, ['black', '#00FFF0'])

    canvas = FigureCanvasTkAgg(fig, janela)
    canvas.draw()
    canvas.get_tk_widget().pack()

    canvas.get_tk_widget().place(x=10, y=10)