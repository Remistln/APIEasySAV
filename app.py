import flask
from flask import Flask, jsonify, request
import json
from Domain.intervention import Intervention
from script.request_interventions import DatabaseActions
import data

app = Flask(__name__)



@app.route('/api/interventions/list')
def afficher_interventions():

    db_name = "database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)
    return db.return_interventions()


@app.route('/api/interventions/add')
def add_interventions():

    db_name = "database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)

    json_file = "data/data.json"
    with open(json_file, encoding='utf-8') as mon_fichier:
        file = json.load(mon_fichier)
        for cle in file.values():
            intervention = Intervention(cle["client"],
                                        cle["technicien"],
                                        cle["date"],
                                        cle["lieu"],
                                        cle["panne"],
                                        cle["piece"],
                                        cle["tmpEcouleDepuisPanne"],
                                        cle["etatPanne"],
                                        cle["satisfaction"],
                                        cle["dureeIntervention"])

            db.commit_intervention(intervention)
    mon_fichier.close()

if __name__ == '__main__':
    app.run()