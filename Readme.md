
# Bot para download de videos e playlists youtube

Este projeto consiste em agilar a forma de baixar videos do youtube sem precisar entrar em sites que contem varios anuncios!

## Funções

### Download de videos

Para a função de download de videos, eles são baixados um por um, o cliente precisara colar a url para que o bot faça a busca, tambem será necessario a inclusão do diretório onde deseja salvar. Os videos por padrão serão cortados com 1 minuto e 30 segundos.

### Download playlists
A função de download de playlists é similiar a de video, porem neste caso será necessario pegar a url da playlist, e ai o bot ira percorrer e baixar todos os videos, por enquanto esta função não tem a opção de cortar os videos

## Rodando localmente

Para rodar localmente siga os passos a seguir

- Primero clone o repositorio

```bash
    git clone https://github.com/ViniciusCosta126/bot-youtube.git
```

- Entre na pasta

```bash
    cd bot-youtube
```

- Crie o ambiente virtual

```bash
    python -m venv env
```

- Ative o ambiente virtual

Windows
```bash
    .\env\Scripts\activate
```

Linux ou macos
```bash
    source env/bin/activate
```

- Instale os requisitos
```bash
    pip install -r requirements.txt
```

- Para rodar o projeto 

```bash
    python app.py
```