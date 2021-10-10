import sqlite3
import flask
from flask import jsonify
import json

from Domain.intervention import Intervention

class DatabaseActions:
    def __init__(self):
        pass

    def connexion(self, connection_link):
        self.conn = sqlite3.connect(connection_link)
        self.cursor = self.conn.cursor()
        return True

    def execute(self, command):
        self.cursor.execute(command)
        return True

    def commit(self):
        self.conn.commit()
        return True

    def close(self):
        self.connexion.close()
        return True

    def return_interventions(self):
        lst = {}
        n = 1
        self.cursor.execute("SELECT * FROM INTERVENTION")
        for row in self.cursor:
            lst.update({n: Intervention(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                       .jesonification()})
            n += 1
        return lst

    def add_intervention(self, json_file):
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
                self.commit_intervention(intervention)
        mon_fichier.close()
        return True

    def commit_intervention(self, intervention):
        supp = f"INSERT INTO INTERVENTION(client," \
                    f"                 technicien," \
                    f"                 date_intervention," \
                    f"                 lieu," \
                    f"                 panne," \
                    f"                 piece," \
                    f"                 tmpEcouleDepuisPanne," \
                    f"                 etatPanne," \
                    f"                 satisfaction," \
                    f"                  dureeIntervention) " \
                    f"VALUES('{intervention.client}'," \
                    f"       '{intervention.technicien}'," \
                    f"       '{intervention.date}'," \
                    f"       '{intervention.lieu}'," \
                    f"       '{intervention.panne}'," \
                    f"       '{intervention.piece}'," \
                    f"       '{intervention.tmpEcouleDepuisPanne}'," \
                    f"       '{intervention.etatPanne}'," \
                    f"       '{intervention.satisfaction}'," \
                    f"       '{intervention.dureeIntervention}')"
        self.cursor.execute(supp)
        self.commit()
        return True