import json

import flask
from flask import Flask

class Intervention:
    def __init__(self, client, technicien, date, lieu, panne, piece, tmp_ecoule, etat_panne, satisfaction, duree):
        self.code = None
        self.client = client
        self.technicien = technicien
        self.date = date
        self.lieu = lieu
        self.panne = panne
        self.piece = piece
        self.tmp_ecoule = tmp_ecoule
        self.etat_panne = etat_panne
        self.satisfaction = satisfaction
        self.duree = duree

    def jesonification(self):
        return flask.json.dumps(self.__dict__)