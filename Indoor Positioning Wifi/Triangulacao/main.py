import tkinter as tk
from tkinter import font as tkfont
import matplotlib.pyplot as plt
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
        for F in (Home, Login):
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

        tk.Button(self, text='Plotar', width=10, height=2, bd=2, bg="#FFFFFF",
                  command=lambda: grafico(self,[x.get(), y.get()])).place(x=550, y=300)
        tk.Label(self, text="Valor de x: ").place(x=548, y=170)
        x = tk.Entry(self, width=30, bd=2, bg="#FFFFFF")
        x.place(x=550, y=190)
        tk.Label(self, text="Valor de y:").place(x=548, y=220)
        y = tk.Entry(self, width=30, bd=2, bg="#FFFFFF")
        y.place(x=550, y=240)


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = Main()
    app.mainloop()
