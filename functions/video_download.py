from functions import YouTube, on_complete, on_progress, Playlist
import re


def video_download(url, caminho, corte):
    path = caminho if caminho != '' else ''

    yt_regex_video = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    match = re.match(yt_regex_video, url)
    if match is not None:
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining),
                     on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, path, corte))

        if yt.length < corte:
            raise ValueError('O corte é maior que o video por favor ajuste')
        else:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution')[-1].download(path)
    else:
        raise ValueError("Url invalida, por favor digite uma url do youtube!!")


def playlist_download(url, caminho, audio_only):
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
