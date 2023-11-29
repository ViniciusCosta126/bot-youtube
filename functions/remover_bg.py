from rembg import remove
from pathlib import Path
from PIL import Image
import os


def remover_bg(caminho, imagem):
    extensoes_imagem = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

    extensao = imagem.filename.rsplit(
        '.', 1)[1].lower() if '.' in imagem.filename else ''
    nome = imagem.filename.rsplit(
        '.', 1)[0] if '.' in imagem.filename else imagem.filename

    if extensao in extensoes_imagem:
        img = Image.open(imagem)

        if Path(caminho).is_dir():
            caminho_imagem = Path(caminho)
            if extensao != 'png':
                caminho_imagem = caminho_imagem.joinpath(
                    f'{nome}-removed-bg')
                img.save(f'{caminho_imagem}.png', format='PNG')
                nova = Image.open(f'{caminho_imagem}.png')
                output = remove(nova)
                os.remove(f'{caminho_imagem}.png')
                output.save(f'{caminho_imagem}.png')
            else:
                caminho_imagem = caminho_imagem.joinpath(
                    f'{nome}-removed-bg.{extensao}')
                output = remove(img)
                output.save(caminho_imagem)

        else:
            raise ValueError("Diretório invalido. Digite um local que exista!")
    else:
        raise ValueError("Tipo de arquivo não aceito!!")
