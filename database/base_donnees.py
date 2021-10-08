import sqlite3


class CreateEasySAV :
    def __init__(self):
        pass

    def connect(self, db):
        self.connexion = sqlite3.connect(db)
        self.curseur = self.connexion.cursor()

    def requete_execute(self, sqlCmd):
        self.curseur.execute(sqlCmd)

    def commit(self):
        self.connexion.commit()

    def close_connection(self):
        self.connexion.close()

    def create_intervention(self):
        createTableIntervention = f"CREATE TABLE IF NOT EXISTS INTERVENTION(" \
                                        f"code INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                                        f"client TEXT," \
                                        f"technicien TEXT," \
                                        f"date_intervention DATE ," \
                                        f"lieu TEXT ," \
                                        f"panne TEXT ," \
                                        f"piece TEXT ," \
                                        f"temps_ecoule TEXT ," \
                                        f"etat_panne TEXT ," \
                                        f"satisfaction TEXT ," \
                                        f"duree TEXT)"
        return createTableIntervention

    def create_technicien(self):
        createTableTechnicien =  f"CREATE TABLE IF NOT EXISTS TECHNICIEN(" \
                                f"nom TEXT," \
                                f" prenom TEXT," \
                                f"competences TEXT," \
                                f" dispo TEXT," \
                                f" interventions TEXT)"
        return createTableTechnicien

    def insert_intervention(self):
        insertDataIntervention =  f"INSERT INTO INTERVENTION VALUES(" \
                                  f"1," \
                                  f"'Remi Staelen', " \
                                  f"'Emile Najare'," \
                                  f"2020-02-02," \
                                  f"'Lille'," \
                                  f"'Machine a laver'," \
                                  f"'Reservoir'," \
                                  f"'120'," \
                                  f"'Terminee'," \
                                  f"'Très Bien'," \
                                  f"'15')"
        return insertDataIntervention

    def insert_technicien(self):
        insertDataTechnicien =  f"INSERT INTO TECHNICIEN VALUES(" \
                                f"'Najare', " \
                                f"'Emile'," \
                                f"'Réparer des machines à laver'," \
                                f"'oui'," \
                                f"'Plusieurs')"
        return insertDataTechnicien

if __name__ == '__main__':

    database = "EasySAV.db"

    #instencier l'objet
    database_name = CreateEasySAV()

    #faire la conexion a la base de donnee
    database_name.connect(database)

    #creer une table dans le fichier *.db cree

    CreateEasySAV.requete_execute(database_name, database_name.create_intervention())
    CreateEasySAV.requete_execute(database_name, database_name.create_technicien())
    CreateEasySAV.requete_execute(database_name, database_name.insert_intervention())
    CreateEasySAV.requete_execute(database_name, database_name.insert_technicien())

    #envoyer a la base
    CreateEasySAV.commit(database_name)

    #fin de la connexion
    CreateEasySAV.close_connection(database_name)