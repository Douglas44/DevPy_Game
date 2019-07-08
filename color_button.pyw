from tkinter import *
class Janela:
    def __init__(self, event):
        self.frame = Frame(event)
        self.frame.pack()

        self.texto = Label(self.frame, text="Clique para ficar amarelo")
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()

        self.botao_verde = Button(self.frame, text="Clique")
        self.botao_verde['bg'] = 'green'
        self.botao_verde.bind("<Button>", self.muda_cor)
        self.botao_verde.pack()

    def muda_cor(self, event):
        """ Muda a cor do botão"""
        if self.botao_verde['bg'] == 'green':
            self.botao_verde['bg'] = 'yellow'
            self.texto['text'] = 'Clique para ficar verde'
        else:
            self.botao_verde['bg'] = 'green'
            self.texto['text'] = 'Clique para ficar amarelo'

root = Tk()
Janela(root)
root.mainloop()
