from tkinter import *
from tkinter import messagebox
import Banco_Dados

class PyGame:
    def __init__(self, master):
        # ==== Frame da Direita ==== #
        self.RightFrame = Frame(master, width=395, height=300, bg='Orange')
        self.RightFrame.pack(side=RIGHT)
        # ==== Frame da Esquerda ==== #
        self.LeftFrame = Frame(master, width=200, height=300, bg='Orange')
        self.LeftFrame.pack(side=LEFT)

        # ==== Logo ==== #
        logo = PhotoImage(file='Images/7-2-python-logo-free-download-png-thumb.png')
        self.Logo = Label(self.LeftFrame, bg='Orange')
        self.Logo['image'] = logo
        self.Logo.image = logo
        self.Logo.place(x=10, y=40)

        self.Logo_Mensagem = Label(self.LeftFrame, text='DevPy_Game', bg='Orange')
        self.Logo_Mensagem['font'] = ('Calibri', '24', 'bold')
        self.Logo_Mensagem.place(x=8, y=200)

        # ==== Label e Entry do User ==== #
        self.User_Label = Label(self.RightFrame, text='Username:', bg='Orange')
        self.User_Label['font'] = ('Calibri', '20')
        self.User_Label.place(x=40, y=100)

        self.User_Entry = Entry(self.RightFrame, width=30)
        self.User_Entry.place(x=180, y=112)

        # ==== Label e Entry do Pass ==== #
        self.Pass_Label = Label(self.RightFrame, text='Password:', bg='Orange')
        self.Pass_Label['font'] = ('Calibri', '20')
        self.Pass_Label.place(x=40, y=170)

        self.Pass_Entry = Entry(self.RightFrame, width=30, show='*')
        self.Pass_Entry.place(x=180, y=182)

        # ==== Botões de Login e Register ==== #
        self.Login = Button(self.RightFrame, width=30, text='==LOGIN==', fg='MIDNIGHTBLUE', command=self.Login_Dev)
        self.Login.place(x=90, y=220)

        self.Register = Button(self.RightFrame, width=30, text='==REGISTER==', fg='Purple', command=self.Register)
        self.Register.place(x=90, y=250)

    def Login_Dev(self):
        Username = self.User_Entry.get()
        Pass = self.Pass_Entry.get()

        Banco_Dados.cursor.execute("""
        SELECT * FROM Users
        WHERE User=? and Password=?
        """, (Username, Pass))
        VerificaLogin = Banco_Dados.cursor.fetchone()
        try:
            if Username in VerificaLogin and Pass in VerificaLogin:
                messagebox.showinfo(title='Login info', message='Conta Registrada com Sucesso')
                self.Tela_Joguinho()  # Chamando a função que mostra os joguinhos
        except:
            messagebox.showerror(title='Login info', message='Erro no Login da conta')

    def Register(self):
        """Removendo o Botão de Login e de Register"""
        self.Login.place(x=5000)
        self.Register.place(x=5000)
        """Colocando o Botão de Back e de Registrar"""
        self.Back = Button(self.RightFrame, width=30, text='==BACK==', fg='Black', command=self.BackToLogin)
        self.Back.place(x=90, y=220)

        self.Registrar = Button(self.RightFrame, width=30, text='==REGISTRAR==', fg='Brown', command=self.RegisterToData_Base)
        self.Registrar.place(x=90, y=250)

        self.Name_Label = Label(self.RightFrame, text='Nome:', bg='Orange')
        self.Name_Label['font'] = ('Calibri', '20')
        self.Name_Label.place(x=45, y=55)

        self.Name_Entry = Entry(self.RightFrame, width=30)
        self.Name_Entry.place(x=138, y=67)

    def RegisterToData_Base(self):
        Username = self.User_Entry.get()
        Pass = self.Pass_Entry.get()
        Nome = self.Name_Entry.get()

        if Username == "" and Pass == "" and Nome == "":
            messagebox.showerror(title='Register DataBase', message='Não deixe nenhum campo vazio')
        elif Username == "" or Pass == "" or Nome == "":
            messagebox.showerror(title='Register DataBase', message='Não deixe nenhum campo vazio')
        else:
            Banco_Dados.cursor.execute("""
            INSERT INTO Users(Name, User, Password) VALUES(?, ?, ?)
            """, (Nome, Username, Pass))
            Banco_Dados.conectar.commit()    # Salvando as operações
            messagebox.showinfo(title='Register Info', message='Conta registrada com sucesso')

    def BackToLogin(self):
        """Recolocando os widgets de volta ao normal"""
        self.Back.place(x=5000)
        self.Registrar.place(x=5000)
        self.Name_Label.place(x=5000)
        self.Name_Entry.place(x=5000)

        self.Login.place(x=90, y=220)
        self.Register.place(x=90, y=250)

    def BackToLogin_Game(self):
        self.Back_Game.place(x=5000)
        self.Button1_Game.place(x=5000)
        self.Button2_Game.place(x=5000)

        self.User_Label.place(x=40, y=100)
        self.User_Entry.place(x=180, y=112)
        self.Pass_Label.place(x=40, y=170)
        self.Pass_Entry.place(x=180, y=182)
        self.Login.place(x=90, y=220)
        self.Register.place(x=90, y=250)

    def Tela_Joguinho(self):
        self.User_Label.place(x=5000)
        self.User_Entry.place(x=5000)
        self.Pass_Label.place(x=5000)
        self.Pass_Entry.place(x=5000)
        self.Login.place(x=5000)
        self.Register.place(x=5000)

        self.Back_Game = Button(self.RightFrame, width=30, text='==BACK==', fg='Black', command=self.BackToLogin_Game)
        self.Back_Game.place(x=90, y=220)

        self.Button1_Game = Button(self.RightFrame, width=20, text='Game 1', fg='Blue', command=self.Game1)
        self.Button1_Game.place(x=70, y=120)

        self.Button2_Game = Button(self.RightFrame, width=20, text='Game 2', fg='Red', command=self.Game2)
        self.Button2_Game.place(x=225, y=120)

    def Game1(self):
        """Joguinho com o Canvas"""
        import Kanvas
    def Game2(self):
        """Joguinho de mudar a cor do botão"""
        import color_button

# === INICIANDO O TKINTER === #
root = Tk()
root.title('DevPy_Game')
root.geometry('600x300')
root.iconbitmap(default='Images/Cornmanthe3rd-Plex-Other-python.ico')
PyGame(root)
root.mainloop()
