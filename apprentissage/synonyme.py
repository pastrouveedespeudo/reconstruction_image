import requests
from bs4 import BeautifulSoup
from database import *

#selon si c un nom ou un adj
class synonyme:

    def recherche_syno(self, mot):
        
        self.mot = mot
   
        
        liste = [[],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[]]


        liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[]]

        
        
        path = "http://www.synonymes.com/synonyme.php?mot={}"
        path = path.format(self.mot)
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
        propriete = soup.find_all("div", {"class":"defbox"})


        c = 0
        d = 0
        
        for i in propriete:
            
            adj = str(i).find(str('Adjectif'))
            nom = str(i).find(str('Nom'))

            if adj >= 0:
 
                for j in i.text[9:]:

                    if j == ",":
                        pass
                    elif j == " ":
                        c+=1
                    else:
                        liste[c].append(j)
               
            
            elif nom >= 0:

                for j in i.text[4:]:
            
                    if j == ",":
                        pass
                    
                    elif j == " ":
                        c+=1
                    else:
                        liste2[c].append(j)
            

        liste_nom2 = []
        for i in liste2:
            if i == []:
                pass
            else:
                i = "".join(i)
                liste_nom2.append(i)
                
        liste_adj2 = []
        for i in liste:
            if i == []:
                pass
            else:
                i = "".join(i)
                liste_adj2.append(i)

                
        #print(liste_nom2)
        #print(liste_adj2)
                
          

    def insertion(self, liste):
        pass
    














