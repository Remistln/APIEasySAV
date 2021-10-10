import unittest
from Domain.intervention import Intervention


class InterventionTestCase(unittest.TestCase):
    def test_intervention(self):
        intervention = Intervention('tom', 'Remi', "2021-05-29", 'Lille', 'lave-linge', 'tambour', 130, 'mauvaise',
                                    'heureux', 200)
        self.assertIsNotNone(intervention)

    def test_jsonification(self):
        intervention = Intervention('tom', 'Remi', "2021-05-29", 'Lille', 'lave-linge', 'tambour', 130, 'mauvaise',
                                    'heureux', 200)
        interventionJson = intervention.jesonification()
        self.assertIsNotNone(interventionJson)


if __name__ == '__main__':
    unittest.main()
