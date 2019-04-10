import requests
from bs4 import BeautifulSoup

class sens_mot:
    def sens(self, phrase):
        self.phrase = phrase

        for i in phrase:
            if i[1] == "nm":
                
                path = "https://www.le-dictionnaire.com/definition/{}"
                path = path.format(j.lower())
                requete = requests.get(path)
                page = requete.content
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find("div", {"class":"defbox"})


                #on cherche dans database
                #synonyme
                #on stocjk
                #et voila ca part en couille
                #detection de forme apres avoir faire un gray treshold
                #find contour
