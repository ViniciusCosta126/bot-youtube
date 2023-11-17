from tkinter import *
from functions import video_download


janela = Tk()

default_color = '#93A8AC'
font_default = 'sans-serif'

def config_default(janela, title, headerText):
    janela.geometry('400x400')
    janela.title(title)
    janela.configure(background=default_color)
    janela.resizable(width=False, height=False)
    header = Label(janela, text=headerText, width=30,
                   background=default_color, font=(font_default, 22,'bold'))
    header.pack(pady=10)


config_default(janela, "Tela Inicial | Home", "Menu principal")


def view_baixar_video():
    global janela
    janela.destroy()
    janela = Tk()
    config_default(janela, "Tela Inicial | Baixar Video", "Baixar Video")
    janela.geometry('500x600')
    texto_url = Label(janela, text="Digite a url do video que deseja baixar*", background=default_color, font=(font_default, 12))
    texto_url.pack(pady=4)
    url = Entry(width=40,border=0)
    url.pack(pady=10, ipady=4, ipadx=4)

    texto_caminho = Label(janela, text="Digite onde deseja salvar(Opcional)", background=default_color, font=(font_default, 12))
    texto_caminho.pack(pady=4)
    caminho = Entry(width=40,border=0)
    caminho.pack(pady=10, ipady=4, ipadx=4)
    
    button = Button(text='Baixar video',width=30,font=(font_default,10), command=lambda: video_download(url.get(),janela,caminho.get()))
    button.pack()


baixar_video = Button(janela, text="Ir para baixar um video",
                      width=30, command=view_baixar_video)
baixar_video.pack(pady=10)
baixar_playlist = Button(janela, text="Ir para baixar uma playlist", width=30)
baixar_playlist.pack(pady=10)


janela.mainloop()
