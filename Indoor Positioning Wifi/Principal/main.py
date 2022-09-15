import tkinter as tk
from tkinter import font as tkfont

from Dados import distancia
from Fala import falar
from grafico import *


## Funcao principal
class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Righteous', size=18)
        self.base_font = tkfont.Font(family='Righteous', size=12)
        self.title("Acessible Campus")

        ## Definido as dimensões da tela
        width = 800
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width

        height = 550
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width

        ## Calculos para colocar a janela no meio da tela
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2

        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        ## Container vai conter todas as telas
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Nada):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


## Pagina inicial
class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global img0, img1, img2

        img0 = tk.PhotoImage(file="imagens/background.png")
        img1 = tk.PhotoImage(file="imagens/logo.png")
        img2 = tk.PhotoImage(file="imagens/plotar.png")

        def plotar():
            saida = distancia()
            grafico(self, saida)
            resposta(saida)


        def resposta(metros):
            falar(f"Você está a aproximadamente {round(metros,2)} metros do roteador")

        tk.Label(self, image=img0).place(x=-2, y=0)
        tk.Label(self, image=img1, bg="#51C1E1").place(x=580, y=150)
        tk.Button(self, image=img2, bd=0, bg='#51C1E1', activebackground='#51C1E1',
                  command=lambda: [plotar()]).place(x=570, y=350)


class Nada(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = Main()
    app.mainloop()
