import unittest
import json

from script.request_interventions import DatabaseActions
from Domain.intervention import Intervention

class DataBaseActionsTestCase(unittest.TestCase):
    def test_connexion(self):
        #arrange
        data_actions = DatabaseActions()
        dbname = '../../database/EasySAV.db'
        #act
        action = DatabaseActions.connexion(data_actions, dbname)
        #assert

        self.assertEqual(action, True)

    def test_execute(self):
        #arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        insertdata = f"INSERT INTO TECHNICIEN VALUES(" \
                                f"'test', " \
                                f"'test'," \
                                f"'test'," \
                                f"'test'," \
                                f"'test')"
        # act
        database.connexion(dbname)
        DatabaseActions.execute(database , insertdata)
        #assert
        self.assertIsNotNone(insertdata)

    def test_commit(self):
        #arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        database.connexion(dbname)
        #act
        commit= DatabaseActions.commit(database)
        #assert
        self.assertTrue(commit)

    def test_close(self):

        # arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        database.connexion(dbname)
        # act
        disconnect = database.close()
        # assert
        self.assertEqual(disconnect,True)

    def test_return_intervention(self):
        #arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        database.connexion(dbname)
        #act
        intervention = DatabaseActions.return_interventions(database)
        #assert
        self.assertIsNotNone(intervention)

    def test_add_intervention(self):
        #arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        database.connexion(dbname)
        json_file = "../../data/data.json"
        with open(json_file, encoding='utf-8') as mon_fichier:
            file = json.load(mon_fichier)
        #act
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
                commit = database.commit_intervention(intervention)
                self.assertIsNotNone(commit, True)

    def test_commit_intervention(self):
        # arrange
        dbname = '../../database/EasySAV.db'
        database = DatabaseActions()
        database.connexion(dbname)
        intervention= Intervention('Amaury','Aya','2021-05-17','Lille','lave-linge','tambour',130,'finit','Satisfait',200)
        #act
        comit_inter = DatabaseActions.commit_intervention(database, intervention)
        #assert
        self.assertTrue(comit_inter)

if __name__ == '__main__':
    unittest.main()
