import requests
from bs4 import BeautifulSoup

from database import *
from synonyme import *



class sens_mot:
    def sens(self, phrase):
        self.phrase = phrase

        forme = visualisation_table.visualisation(self)


        for i in phrase:
            if i == []:
                pass
            else:
                if i[0][1] == "Nom":

                    path = "https://www.le-dictionnaire.com/definition/{}"
                    path = path.format(i[0][0].lower())
                    requete = requests.get(path)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find("div", {"class":"defbox"})

                    for form in forme:
                        for j in form:
                            if j == None:
                                pass
                            else:
                                print(j)
                                recherche = str(propriete).find(str(j))
                                
                                if recherche >= 0:
                                   
                                    synonyme.recherche_syno(self,j)


                    
                    #on cherche dans database
                    #synonyme
                    #on stocjk
                    #et voila ca part en couille
                    #detection de forme apres avoir faire un gray treshold
                    #find contour












