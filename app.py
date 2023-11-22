from flask import Flask, render_template, request, redirect, url_for
from functions.video_download import video_download, playlist_download
app = Flask(__name__)

app.debug = True
app.secret_key = 'sfjasfjasifjifjaisfjioasda'


@app.route('/')
def home():
    return render_template('home.html', titulo='Donwload Video | Home')


@app.route('/download-video')
def download_video():
    action_url = url_for('home', _external=True)
    action_url += 'download-video-corte'
    return render_template('download-video.html', titulo='Download Video | Video', action_url=action_url)


@app.route('/download-playlist')
def download_playlist():
    action_url = url_for('home', _external=True)
    action_url += 'download-videos-playlist'
    return render_template('download-playlist.html', titulo='Download Video | Playlist', action_url=action_url)


@app.route('/download-video-corte', methods=['POST'])
def download_video_corte():
    if request.method == 'POST':
        data = request.json
        video_url = data['url']
        caminho = data['caminho']
        video_download(video_url, caminho)
        return redirect(url_for('download_video'))


@app.route('/download-videos-playlist', methods=['POST'])
def download_videos_playlist():
    if request.method == 'POST':
        data = request.json
        playlist_url = data['url']
        caminho = data['caminho']
        audio_only = False
        if 'audio_check' in data:
            audio_only = True
        playlist_download(playlist_url, caminho, audio_only)
        return redirect(url_for('download_playlist'))


app.run()
