from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


def on_complete(stream, file_path):
    print(stream.title)
    print(file_path)


url = input("Digite a url que deseja baixar =>")

yt = YouTube(url, on_progress_callback=on_progress,
             on_complete_callback=on_complete)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution')[-1].download()
