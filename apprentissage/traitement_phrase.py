import requests
from bs4 import BeautifulSoup


class traitement_phrase:

    def trait(self, phrase):
        self.phrase = phrase
        self.phrase = self.phrase.split()
   
        return self.phrase

    def traitement_nm(self, phrase):
        self.phrase = phrase

        self.phrase = self.phrase.split()

        liste_nm = []

        for i in self.phrase:
         
            path = "https://www.le-dictionnaire.com/definition/{}"
            path = path.format(i.lower())
            requete = requests.get(path)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")      
            propriete = soup.find("div", {"class":"defbox"})

            nm = str(propriete).find("Nom commun")

            if nm >= 0:
                liste_nm.append(i)
       
        return liste_nm

class traitement_reponse:
    def nombre(self, phrase):

   
        liste = [[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],
                 [],[],[],[],[],[],[]]


        self.phrase = phrase
        self.phrase = self.phrase.split()
        c = 0
        for i in self.phrase:

            try:
                i = int(i)
                if i == int(i):
                    liste[c].append([int(i), "int"])
            except:
                pass
            finally:
                c+=1

    
        return liste


    def nm(self, phrase, liste):
        
        self.liste = liste     
        self.phrase = phrase

        self.phrase = self.phrase.split()

        c = 0
        for i in self.phrase:

            if i[-1] == 's':
                j = i[:-1]
            
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})

                nm = str(propriete).find("Nom commun")
                numeral = str(propriete).find("Forme d’adjectif numéral")

                if nm >= 0:
                    self.liste[c].append([j, "Nom"])
               
                    
                elif numeral >= 0:
                    self.liste[c].append([j, "numeral"])

                c+=1
                


                    
            else:
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(i.lower())
                requete = requests.get(path)
                page = requete.content
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})

                nm = str(propriete).find("Nom commun")
                numeral = str(propriete).find("Forme d’adjectif numéral")

                if nm >= 0:
                    self.liste[c].append([i, "Nom"])
                 
                    
                elif numeral >= 0:
                    self.liste[c].append([i, "numeral"])
                   
                c+=1
                    
        

        return self.liste

        #a la fin faire: liste2 = [i for i in liste if i != []]



    
    def traitement_nombre(self, liste):
        self.liste = liste

        dico = {"un":1,"une":1, "deux":2, "trois":3,"quattre":4,
                "cinq":5, "six":6, "sept":7, "huit":8, "neuf":9,
                "dix":10}

        c = 0
        for i in self.liste:
            if i == []:
                pass
            else:
                if i[0][1] == 'numeral':
                    for cle, valeur in dico.items():
                        try:
                            if i[0][0] == cle:
                                self.liste[c][0][0] = valeur
                        except:
                            pass
            c+=1

        return self.liste
    






















