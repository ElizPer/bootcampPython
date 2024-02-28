'''
Local onde será consumido os dados do API
------------------------------------------
Passo a passo: https://flask.palletsprojects.com/en/3.0.x/installation/
1º criar um ambiente virtual do flask dentro da pasta desejada: py -3 -m venv .venv (cria o ambiente com o nome da pasta de .venv)
2º ativar esse ambiente virtual: .venv\Scripts\activate
3º instalação do FLASK no projeto:  pip install Flask

'''

from flask import Flask, render_template
import urllib.request, json #urllib ajuda a manipular as requisições para uma URL (ou seja, o endpoint) e a JSON vai ajudar a tratar, ou seja, imprimir na tela o resultado que receber da requisição

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])

@app.route("/profile_locations/<id>")
def get_profile_locations(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile_locations.html", profile_locations=dict)

@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"])

@app.route("/profile_episodes/<id>")
def get_profile_episodes(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile_episodes.html", profile_episodes=dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()#vai fazer a leitura dos resultados
    dict = json.loads(characters)#vai formartar para formato de JSON 

    return render_template("lista.html", lista=dict["results"])
    '''characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]          
        }

        characters.append(character)

    return {"characters": characters}'''
