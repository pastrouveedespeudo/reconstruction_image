import mysql.connector
from config import *


class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        
class table:
    def creation_table(self):
        connexion_database.connexion(self)
        self.cursor.execute("""""")
        self.connexion.commit()

class insertion_table:
    def insertion(self):
        connexion_database.connexion(self)


class visualisation_table:
    def visualisation(self):
        connexion_database.connexion(self)

    

