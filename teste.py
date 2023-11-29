from rembg import remove
from pathlib import Path

input_path = 'passaros-tropicos-mais-coloridos-conexao-planeta.jpg'
output_path = 'cortado.jpg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)