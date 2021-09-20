import flask
import requests
from flask import render_template
import json


app=flask.Flask(__name__)

@app.route('/')
def index():
    headers = { 'Accept':'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer BQC4xgjN481FPNxxA_cLF6Djd3YrPfs6Q7N2bQ8dJ8GozsCX61lwBjFHaA2CE5DgQxv4sw7Czrn8nces2fhS4Rz5KKguLGCIIhmI5oLFKbAg_KrgJeapyd6NFCwML9qGD_1jjmA3BoLnXBS4hR7AHL6o9fcYsLJk6mDqJzP-J3HT0MrAef6ohQ'}
    response = requests.get('https://api.spotify.com/v1/artists/1uNFoZAHBGtllmzznpCI3s', headers=headers)
    response_payload = response.json()
    popularity = response_payload['popularity']
    genres = response_payload['genres']

    return render_template('index.html', popularity=popularity, genres=genres)
app.run()