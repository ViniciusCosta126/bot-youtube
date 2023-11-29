from functions import YouTube, on_complete, on_progress
import re
from pathlib import Path


def video_download(url, caminho, corte):
    '''Função que realiza download de uma video do youtube'''
    path = caminho if caminho != '' else ''
    if Path(path).is_dir():
        yt_regex_video = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

        match = re.match(yt_regex_video, url)
        if match is not None:
            yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining),
                        on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, path, corte))

            if corte <= 0:
                raise ValueError(
                    'O valor do corte não poder ser igual ou menor que zero!')

            if yt.length < corte:
                raise ValueError('O corte é maior que o video por favor ajuste')

            else:
                yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                    'resolution')[-1].download(path)
        else:
            raise ValueError("Url invalida, por favor digite uma url do youtube!!")
    else:
        raise ValueError("Diretório invalido. Digite um local que exista!")
