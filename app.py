from flask import Flask, render_template
from routes import routes
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes.rotas)
app.debug = os.getenv('DEBUG')
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('home.html', titulo='Donwload Video | Home')


app.run()
