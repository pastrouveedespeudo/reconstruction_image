import psycopg2


conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cursor = conn.cursor()
                    cursor.execute("INSERT INTO mes_aliments_categorie(name_categorie) VALUES ('{0}')".format(str(self.liste[c])))
            conn.commit()
