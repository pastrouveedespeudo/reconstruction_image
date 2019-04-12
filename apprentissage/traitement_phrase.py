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
                    indexage = self.phrase.index(str(i))
                    liste[indexage].append([int(i), "int"])
            except:
                pass

        return liste


    def nm(self, phrase, liste):

        self.liste = liste     
        self.phrase = phrase

        self.phrase = self.phrase.split()


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
                    indexage = self.phrase.index(i)
                    self.liste[indexage].append([j, "Nom"])
                    
                elif numeral >= 0:
                    indexage = self.phrase.index(i)
                    self.liste[indexage].append([j, "numeral"])



                    
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
                    indexage = self.phrase.index(i)
                    self.liste[indexage].append([i, "Nom"])
                    
                elif numeral >= 0:
                    indexage = self.phrase.index(i)
                    self.liste[indexage].append([i, "numeral"])

                    
     
        return self.liste

        #a la fin faire: liste2 = [i for i in liste if i != []]



    
    def traitement_nombre(self, liste):
        self.liste = liste
























