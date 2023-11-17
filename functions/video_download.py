from functions import YouTube, on_complete, on_progress
from tkinter import *


def video_download(url, janela):
    texto = Label(janela)
    texto.pack(pady=10)
    if (url == ''):
        texto.config(text='Digite uma url!!', background='#93A8AC', font=('sans-serif', 14,'bold'),foreground='#ea1d2c')
        janela.update_idletasks()
        janela.after(1500, texto.destroy())
    else:
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining, janela),
                     on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, janela))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution')[-1].download()
