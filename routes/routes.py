from flask import Blueprint, request, redirect, url_for, jsonify, render_template
from functions.video_download import video_download, playlist_download


rotas = Blueprint('rotas', __name__)


@rotas.route('/download-video')
def download_video():
    action_url = url_for('home', _external=True)
    action_url += 'download-video-corte'
    return render_template('download-video.html', titulo='Download Video | Video', action_url=action_url)


@rotas.route('/download-playlist')
def download_playlist():
    action_url = url_for('home', _external=True)
    action_url += 'download-videos-playlist'
    return render_template('download-playlist.html', titulo='Download Video | Playlist', action_url=action_url)


@rotas.route('/download-video-corte', methods=['POST'])
def download_video_corte():
    if request.method == 'POST':
        try:
            data = request.json
            video_url = data['url']
            caminho = data['caminho']
            corte = data['corte']
            corte = int(corte)
            video_download(video_url, caminho, corte)
            return redirect(url_for('download_video'))
        except ValueError as e:
            error_message = str(e)
            return jsonify({'error': error_message}), 400


@rotas.route('/download-videos-playlist', methods=['POST'])
def download_videos_playlist():
    if request.method == 'POST':
        try:
            data = request.json
            playlist_url = data['url']
            caminho = data['caminho']
            audio_only = False
            if 'audio_check' in data:
                audio_only = True
            playlist_download(playlist_url, caminho, audio_only)
            return redirect(url_for('download_playlist'))
        except ValueError as e:
            error_message = str(e)
            return jsonify({'error': error_message}), 400
