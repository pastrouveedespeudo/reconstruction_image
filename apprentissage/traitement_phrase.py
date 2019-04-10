import requests
from bs4 import BeautifulSoup


class traitement_phrase:

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

    def traitement_reponse(self, phrase):
        pass
