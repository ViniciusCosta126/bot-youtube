from tkinter import *


def on_progress(stream, chunk, bytes_remaining, janela):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100

    texto = Label(janela, text=f"Status: {round(pct_completed, 2)} %", width=30,
                  background='#93A8AC', font=('sans-serif', 12), wraplength=150)
    texto.pack()
    janela.update_idletasks()


def on_complete(stream, file_path, janela):
    texto_caminho = Label(
        janela, text=f"Download concluido! Arquvio salvo na pasta: \n\n{file_path}", width=60, background='#93A8AC', font=('sans-serif', 16), wraplength=450)
    texto_caminho.pack(pady=8)
    janela.update_idletasks()
