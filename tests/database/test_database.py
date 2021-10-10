import unittest
from database.database import CreateDatabase


class CreateDatabaseTestCase(unittest.TestCase):

    def test_connect(self):
        #arrange
        dbname = '../database/EasySAV.db'
        database = CreateDatabase()
        #act
        test =database.connect(dbname)
        #assert
        self.assertEqual(test, True)

    def test_execute(self):
        # arrange
        dbname = '../database/EasySAV.db'
        database = CreateDatabase()
        insertdata = f"INSERT INTO TECHNICIEN VALUES(" \
                                f"'test', " \
                                f"'test'," \
                                f"'test'," \
                                f"'test'," \
                                f"'test')"
        # act
        database.connect(dbname)
        CreateDatabase.execute(database , insertdata)
        #assert
        self.assertIsNotNone(insertdata)

    def test_commit(self):
        #arrange
        dbname = '../database/EasySAV.db'
        database = CreateDatabase()
        database.connect(dbname)
        #act
        commit= CreateDatabase.commit(database)
        #assert
        self.assertEquals(commit, True)

    def test_close(self):
        # arrange
        dbname = '../database/EasySAV.db'
        database = CreateDatabase()
        database.connect(dbname)
        #act
        close = database.close()
        #assert
        self.assertEqual(close, True )

    def test_create_intervention(self):
        # arrange
        dbname = '../database/EasySAV.db'
        database = CreateDatabase()
        database.connect(dbname)
        #act
        create=database.create_intervention()
        #assert
        self.assertIsNotNone(create)

if __name__ == '__main__':
    unittest.main()

