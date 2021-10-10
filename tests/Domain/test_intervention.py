import unittest
from Domain.intervention import Intervention


class InterventionTestCase(unittest.TestCase):
    def test_intervention(self):
        intervention = Intervention('tom', 'Remi', "2021-05-29", 'Lille', 'lave-linge', 'tambour', 130, 'terminee',
                                    'heureux', 200)

        self.assertIsNotNone(intervention)

    def test_jsonification(self):
        intervention = Intervention('tom', 'Remi', "2021-05-29", 'Lille', 'lave-linge', 'tambour', 130, 'terminee',
                                    'heureux', 200)
        intervention.code = 8

        intervention_json = {
                    "code": 8,
                    "client": "tom",
                    "technicien": "Remi",
                    "date": "2021-05-29",
                    "lieu": "Lille",
                    "panne": "lave-linge",
                    "piece": "tambour",
                    "tmpEcouleDepuisPanne": 130,
                    "etatPanne": "terminee",
                    "satisfaction": "heureux",
                    "dureeIntervention": 200
                }



        interventionJson = intervention.jesonification()

        self.assertIsNotNone(interventionJson)
        print(interventionJson)
        print(intervention_json)
        assert interventionJson == intervention_json





if __name__ == '__main__':
    unittest.main()
