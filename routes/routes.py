from flask import Blueprint, request, redirect, url_for, jsonify, render_template
from functions.video_download import video_download
from functions.playlist_download import playlist_download
from functions.remover_bg import remover_bg

rotas = Blueprint('rotas', __name__)


@rotas.route('/download-video')
def download_video():
    action_url = url_for('home', _external=True)
    action_url += 'download-video-corte'
    return render_template('download-video.html', titulo='Cortador de Mídia Online | Video', action_url=action_url)


@rotas.route('/download-playlist')
def download_playlist():
    action_url = url_for('home', _external=True)
    action_url += 'download-videos-playlist'
    return render_template('download-playlist.html', titulo='Cortador de Mídia Online | Playlist', action_url=action_url)


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
            return jsonify({'erro': error_message}), 400


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
            return jsonify({'erro': error_message}), 400


@rotas.route('/remover-fundo-img')
def remover_fundo_img():
    action_url = url_for('home', _external=True)
    action_url += 'remover-fundo-bg'
    return render_template('remover-fundo-img.html', titulo='Cortador de Mídia Online | Remover fundo', action_url=action_url)


@rotas.route('/remover-fundo-bg', methods=['POST'])
def remover_fundo_bg():
    if request.method == "POST":
        try:
            imagem = request.files['image']
            caminho = request.form['caminho']
            remover_bg(caminho, imagem)
            return jsonify({'message':f'Fundo removido com sucesso!! Salvo no caminho {caminho}'}),200
        except ValueError as e:
            error_message = str(e)
            print(error_message)
            return jsonify({'erro': error_message}), 400
