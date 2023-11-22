from functions import YouTube, on_complete, on_progress, Playlist
import re


def video_download(url, caminho):
    if (url == ''):
        pass
    else:
        path = caminho if caminho != '' else ''
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining),
                     on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, path))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution')[-1].download(path)


def playlist_download(url, caminho, audio_only):
    if url != '':
        playlist = Playlist(url)
        for video in playlist.videos:
            titulo = str(video.title).strip()
            titulo = re.sub(r'[^a-zA-Z0-9\s]', '', titulo)
            titulo +='.mp3'
            if audio_only:
                audio_streams = video.streams.filter(only_audio=True)
                if audio_streams:
                    audio_streams[0].download(
                        output_path=caminho, filename=titulo)
            else:
                video.streams.filter(progressive=True, file_extension='mp4').order_by(
                    'resolution')[-1].download(caminho)
