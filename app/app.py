import flask
from flask import Flask, jsonify, request
import json
from Domain.intervention import Intervention
from script.request_interventions import DatabaseActions
import data

app = Flask(__name__)



@app.route('/api/interventions/list')
def afficher_interventions():

    db_name = "../database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)
    return db.return_interventions()


@app.route('/api/interventions/add')
def ajouter_interventions():

    db_name = "../database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)

    json_file = "../data/data.json"
    if db.add_intervention(json_file) is True:
        return "Les informations de l'intervention ont bien ete ajoutes"
    else:
        return "Un probleme est survenue lors du transfere des informations"


if __name__ == '__main__':
    app.run()