from functions import Playlist
import re
from pathlib import Path


def playlist_download(url, caminho, audio_only):
    '''Função que realiza download de uma playlist completa do youtube'''
    if Path(caminho).is_dir():
        yt_regex_playlist = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(playlist\?|.*&)(list=)([^_&=\s]+)')

        match = re.match(yt_regex_playlist, url)
        if match is not None:
            playlist = Playlist(url)
            for video in playlist.videos:
                if audio_only:
                    titulo = str(video.title).strip()
                    titulo = re.sub(r'[^a-zA-Z0-9\s]', '', titulo)
                    titulo += '.mp3'
                    audio_streams = video.streams.filter(only_audio=True)
                    if audio_streams:
                        audio_streams[0].download(
                            output_path=caminho, filename=titulo)
                else:
                    video.streams.filter(progressive=True, file_extension='mp4').order_by(
                        'resolution')[-1].download(caminho)
        else:
            raise ValueError(
                "Url invalida, por favor digite a url de uma playlist do youtube!!")
    else:
        raise ValueError("Diretório invalido. Digite um local que exista!")
