from tkinter import *
from moviepy.editor import VideoFileClip
from pathlib import Path
import os
import re


def on_progress(stream, chunk, bytes_remaining, janela):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100

    texto = Label(janela, text=f"Status: {round(pct_completed, 2)} %", width=30,
                  background='#93A8AC', font=('sans-serif', 12), wraplength=150)
    texto.pack()
    janela.update_idletasks()
    janela.after(3000, texto.destroy())


def on_complete(stream, file_path, janela, path_user):
    texto_caminho = Label(
        janela, text=f"Download concluido! Arquvio salvo na pasta: \n\n{file_path}", width=60, background='#93A8AC', font=('sans-serif', 16), wraplength=450)
    texto_caminho.pack(pady=8)
    janela.update_idletasks()
    janela.after(3000, texto_caminho.destroy())

    video = VideoFileClip(file_path)
    duracao_total = int(video.duration)
    caminho_video = Path(path_user)

    nome_pasta = stream.title
    nome_pasta = str(nome_pasta).strip()
    nome_pasta = re.sub(r'[^a-zA-Z0-9\s]', '', nome_pasta)
    nome_pasta = nome_pasta[:256] if len(nome_pasta) > 256 else nome_pasta
    
    caminho_video = caminho_video.joinpath(nome_pasta)
    caminho_video.mkdir()
    intervalo_corte = 90
    for i in range(0, duracao_total, intervalo_corte):
        tempo_inicio = i
        tempo_fim = min(i + intervalo_corte, duracao_total)
        video_cortado = video.subclip(tempo_inicio, tempo_fim)

        caminho_salvar = caminho_video.joinpath(
            f"{nome_pasta}_{i}_{tempo_fim}.mp4")
        caminho_salvar = str(caminho_salvar)
        video_cortado.write_videofile(caminho_salvar)

    video.close()
