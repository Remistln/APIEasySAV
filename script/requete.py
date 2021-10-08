import sqlite3
import flask
from flask import jsonify

from Domain.intervention import Intervention
from Domain.technicien import Technicien

class DatabaseActions:
    def __init__(self):
        pass

    def connexion(self, connection_link):
        self.__conn = sqlite3.connect(connection_link)
        self.__cursor = self.__conn.cursor()

    def __execute_commande(self, sqlCommand):
        self.__cursor.execute(sqlCommand)

    def __commit(self):
        self.__conn.commit()

    def get_all_interventions(self):
        lst = {}
        n = 1
        self.__cursor.execute("SELECT * FROM INTERVENTION")
        for row in self.__cursor:
            lst.update({n: Intervention(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]).jesonification()})
            n += 1
        return lst

    def get_all_techniciens(self):
        liste = []
        self.__execute("SELECT * FROM TECHNICIEN")
        for row in self.__cursor:
            liste.append(Technicien(row[0], row[1], row[2], row[3], row[4]).to_dict())
        return liste


    def save_intervention(self, intervention):
        supp = f"INSERT INTO INTERVENTION(client," \
                    f"                 technicien," \
                    f"                 date_intervention," \
                    f"                 lieu," \
                    f"                 panne," \
                    f"                 piece," \
                    f"                 etat_panne," \
                    f"                 temps_ecoule," \
                    f"                 satisfaction," \
                    f"                  duree) " \
                    f"VALUES('{intervention.client}'," \
                    f"       '{intervention.technicien}'," \
                    f"       '{intervention.date}'," \
                    f"       '{intervention.lieu}'," \
                    f"       '{intervention.panne}'," \
                    f"       '{intervention.piece}'," \
                    f"       '{intervention.etat_panne}'," \
                    f"       '{intervention.tmp_ecoule}'," \
                    f"       '{intervention.satisfaction}'," \
                    f"       '{intervention.duree}')"
        self.__cursor.execute(supp)
        self.__commit()
        return True