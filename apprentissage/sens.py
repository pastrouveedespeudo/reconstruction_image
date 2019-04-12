import requests
from bs4 import BeautifulSoup

from database import *
from synonyme import *



class sens_mot:
    def sens(self, phrase):
        self.phrase = phrase

        forme = visualisation_table.visualisation(self)


        for i in phrase:
            print(i)
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
                          
                                recherche = str(propriete).find(str(j))
                                #dessin

                                #caisse
                                #rond
                                if recherche >= 0:
                                    
                                    synonyme.recherche_syno(self,j)


                    
                    #stockage des synonymes
                    #plus rond dans circulaire

    def localisation(self, liste, reponse):
        self.reponse = reponse
        self.liste = liste
  
        dessus = ['sur']
        dessous = []
        meme_pos = ['juxtaposées']
        


        
        for i in self.reponse:
            if i == []:
                pass
            else:
                for j in dessus:
         
                    if i== j:
                        indexage = self.reponse.index(i)
                        self.liste[indexage].append('dessus')
                        
                for k in dessous:
                    if i == j:
                        indexage = self.reponse.index(i)
                        self.liste[indexage].append('dessus')
                        
                for l in meme_pos:
                    if i == j:
                        indexage = self.reponse.index(i)
                        self.liste[indexage].append('meme_pos')

        print(self.liste)
        return self.liste


        






































