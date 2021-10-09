import flask
from flask import Flask
from Domain.intervention import Intervention


class Technicien:
    def __init__(self, nom, prenom, competences, dispo, interventions):
        self.nom = nom
        self.prenom = prenom
        self.competences = [competences]
        self.dispo = [dispo]
        self.interventions = [interventions]

    def ajout_competence(self, competence):
        self.competences.append(competence)

    def ajout_intervention(self, intervention):
        self.interventions.append(intervention)

    def ajout_dispo(self, dispo):
        self.dispo.append(dispo)

    def jesonification(self):
        return flask.json.dumps(self.__dict__)