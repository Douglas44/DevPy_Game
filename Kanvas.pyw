from tkinter import *

class Kanvas:
    def __init__(self, event):
        self.canvas = Canvas(event, width=400, height=400,
                             cursor='X_cursor', bd=5)
        self.canvas.pack()

        self.frame = Frame(event)
        self.frame.pack()

        """ --- Config para os botões b1, b2, b3 e b4 ---"""
        configs = {'fg': 'darkblue', 'bg': 'ghostwhite', 'relief': GROOVE,
                   'width': 11, 'font': ('Verdana', '12', 'bold')}

        self.last = [200, 200]

        self.b1 = Button(self.frame, configs, text='Esquerda', command=self.left)
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.frame, configs, text='Direita', command=self.righ)
        self.b2.pack(side=LEFT)

        self.b3 = Button(self.frame, configs, text='Para cima', command=self.up)
        self.b3.pack(side=LEFT)

        self.b4 = Button(self.frame, configs, text='Para baixo', command=self.down)
        self.b4.pack(side=LEFT)

    def left(self):    # Linha para esquerda
        x, y = self.last[0]-10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='yellow')
        self.last = [x, y]

    def righ(self):    # Linha para direita
        x, y = self.last[0]+10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='blue')
        self.last = [x, y]

    def up(self):    # Linha para cima
        x, y = self.last[0], self.last[1]-10
        self.canvas.create_line(self.last, x, y, fill='red')
        self.last = [x, y]

    def down(self):    # Linha para baixo
        x, y = self.last[0], self.last[1]+10
        self.canvas.create_line(self.last, x, y, fill='purple')
        self.last = [x, y]

root = Tk()
Kanvas(root)
root.mainloop()
