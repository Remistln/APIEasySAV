import json

import flask
from flask import Flask

class Intervention:
    def __init__(self, client, technicien, date, lieu, panne, piece, tmpEcouleDepuisPanne, etatPanne, satisfaction, dureeIntervention):
        self.code = None
        self.client = client
        self.technicien = technicien
        self.date = date
        self.lieu = lieu
        self.panne = panne
        self.piece = piece
        self.tmpEcouleDepuisPanne = tmpEcouleDepuisPanne
        self.etatPanne = etatPanne
        self.satisfaction = satisfaction
        self.dureeIntervention = dureeIntervention

    def jesonification(self):
        return flask.json.dumps(self.__dict__)
