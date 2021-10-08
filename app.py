import flask
from flask import Flask, jsonify, request
import json
from Domain.intervention import Intervention
from script.requete import DatabaseActions
import data

app = Flask(__name__)



@app.route('/api/interventions/list')
def afficher_interventions():

    db_name = "database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)
    return db.get_all_interventions()


@app.route('/api/interventions/add')
def ajouter_interventions():

    db_name = "database/EasySAV.db"
    db = DatabaseActions()
    db.connexion(db_name)

    json_file = "data/data.json"
    with open(json_file, encoding='utf-8') as mon_fichier:
        file = json.load(mon_fichier)
        for cle in file.values():
            intervention = Intervention(cle["code"], cle["client"], cle["technicien"], cle["date"], cle["lieu"], cle["panne"], cle["piece"], cle["tmp_ecoule"], cle["etat_panne"], cle["satisfaction"], cle["duree"])
            db.save_intervention(intervention)
    mon_fichier.close()

if __name__ == '__main__':
    app.run()