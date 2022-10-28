from tkinter import *
from turtle import bgcolor

root = Tk ()
cor_fr = '#1B2232'
cor_bg = '#2D3341'
cor_bd = '#EC2542'

class Application():
  def __init__(self):
    self.root = root
    self.tela()
    self.frame_da_tela()
    self.widgets_frame_1()
    root.mainloop()
    
  def tela(self):
    self.root.title("Pilot School - Escola de pilotagem")
    self.root.configure(background= cor_fr)
    self.root.geometry("700x580")
    self.root.resizable(True, True)
    self.root.maxsize(width=800, height=700)
    self.root.minsize(width=400, height=500)

  def frame_da_tela(self):
    self.frame_1 = Frame(self.root, bd= 4, bg= cor_bg, highlightbackground=cor_bd, highlightthickness='2')
    self.frame_1.place(relx = 0.02 , rely= 0.02, relwidth=0.96, relheight=0.46)


    self.frame_2 = Frame(self.root, bd= 4, bg= cor_bg, highlightbackground=cor_bd, highlightthickness='2')
    self.frame_2.place(relx = 0.02 , rely= 0.5, relwidth=0.96, relheight=0.46)


  def widgets_frame_1(self):
    #Criando botão limpar
    self.limpar = Button(self.frame_1, text='Limpar')
    self.limpar.place(relx = 0.5, rely=0.8, relwidth=0.1, relheight=0.15)
    #Criando botão buscar
    self.limpar = Button(self.frame_1, text='Buscar')
    self.limpar.place(relx = 0.6, rely=0.8, relwidth=0.1, relheight=0.15)
    #Criando botão novo
    self.limpar = Button(self.frame_1, text='Novo')
    self.limpar.place(relx = 0.7, rely=0.8, relwidth=0.1, relheight=0.15)
    #Criando botão alterar
    self.limpar = Button(self.frame_1, text='Alterar')
    self.limpar.place(relx = 0.8, rely=0.8, relwidth=0.1, relheight=0.15)
    #Criando botão apagar
    self.limpar = Button(self.frame_1, text='Apagar')
    self.limpar.place(relx = 0.9, rely=0.8, relwidth=0.1, relheight=0.15)

    #Criação da label 
    ##self.lb_nome = Label(self.frame_1, text="Nome")
    #self.lb.nome.place(relx=)




Application()