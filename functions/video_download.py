from functions import YouTube, on_complete, on_progress


def video_download(url, caminho):
    if (url == ''):
        pass
    else:
        path = caminho if caminho != '' else ''
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining),
                     on_complete_callback=lambda stream, file_path: on_complete(stream, file_path, path))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution')[-1].download(path)
