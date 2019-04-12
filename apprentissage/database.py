import mysql.connector
from config import *


        
class create_base:
    def database(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()
        
        self.cursor.execute("""CREATE DATABASE JOJO""")
        self.connexion.commit()

class connexion_database:
    def connexion(self):
        
        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)
        self.cursor = self.connexion.cursor()

        self.cursor.execute("""use JOJO""")
        self.connexion.commit()


class table:
    def creation_table_geo(self):
        connexion_database.connexion(self)
        self.cursor.execute("""create table forme_geometrique(
                            carre varchar(100),
                            rond varchar(100),
                            rectangle varchar(100));
                            """)
        self.connexion.commit()




class insertion_table:
    def insertion(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""insert into forme_geometrique
                            (rectangle) value('caisse');
                
                            """)
        self.connexion.commit()

class visualisation_table:
    def visualisation(self):
        connexion_database.connexion(self)

        self.cursor.execute("""select * from forme_geometrique""")
        rows = self.cursor.fetchall()
        liste = [i for i in rows]

        return liste



class suppression_table:
    def suppression(self):
        connexion_database.connexion(self)
        
        self.cursor.execute("""drop table forme_geometrique;
                            """)
        self.connexion.commit()

           
    
if __name__ == "__main__":
            
    create_base = create_base()
    table = table()
    insertion_table = insertion_table()
    suppression_table = suppression_table()


    #suppression_table.suppression()
    
    #create_base.database()

    

    #table.creation_table_geo()
    #insertion_table.insertion()




























    
