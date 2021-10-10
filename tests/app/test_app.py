import unittest
from flask import Flask

from script.request_interventions import DatabaseActions


class MyTestCase(unittest.TestCase):
    def test_afficher_interventions(self):

        db_name = "../../database/EasySAV.db"
        db = DatabaseActions()
        db.connexion(db_name)

        inter = db.return_interventions()

        returnJson = {1: {'code': None, 'client': 'Remi Staelen', 'technicien': 'Emile Najare', 'date': 2016, 'lieu': 'Lille', 'panne': 'Machine a laver', 'piece': 'Reservoir', 'tmpEcouleDepuisPanne': 120, 'etatPanne': 'Terminee', 'satisfaction': 'Très Bien', 'dureeIntervention': 15}}


        self.assertEqual(inter, returnJson)  # add assertion here

    def test_ajouter_intervention(self):
        db_name = "../../database/EasySAV.db"
        db = DatabaseActions()
        db.connexion(db_name)

        json_file = "../../data/data.json"
        db.add_intervention(json_file)

        self.assertEqual(db.add_intervention(json_file), True)  # add assertion here



if __name__ == '__main__':
    unittest.main()
