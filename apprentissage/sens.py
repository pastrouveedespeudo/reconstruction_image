import requests
from bs4 import BeautifulSoup

from database import *
from synonyme import *
from traitement_phrase import *


class sens_mot:
    def sens(self, phrase):
        self.phrase = phrase

        rond = visualisation_table.visualisation_rond(self)
        rectangle = visualisation_table.visualisation_rectangle(self)
        carre = visualisation_table.visualisation_carre(self)

     
        for i in self.phrase:
  
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

                    for form in rond:
                        for j in form:
                            if j == None:
                                pass
                            else:
                                recherche = str(propriete).find(str(j))
                                if recherche >= 0:
                                    synonyme.recherche_syno(self,j)
                                    indexage = self.phrase.index(i)
                                    self.phrase[indexage][0].append('rond')
                                break
                            
                    for form1 in carre: 
                        for k in form1:
                            if k == None:
                                pass
                            else:
                                recherche = str(propriete).find(str(k))
                                if recherche >= 0:
                                    synonyme.recherche_syno(self,k)
                                    indexage = self.phrase.index(i)
                                    self.phrase[indexage][0].append('carre')
                                break
                                
                    for form2 in rectangle: 
                        for l in form2:
                            if l == None:
                                pass
                            else:
                                recherche = str(propriete).find(str(l))
                                if recherche >= 0:
                                    synonyme.recherche_syno(self,l)
                                    indexage = self.phrase.index(i)
                                    self.phrase[indexage][0].append('rectangle')
                                break

                                    
                    #stockage des synonymes
                    #plus rond dans circulaire



    def localisation(self, liste, reponse):
        self.reponse = reponse
        self.liste = liste
  

        dessus = ['sur']
        dessous = []
        meme_pos = ['juxtaposées']
        devant = ['avant']
        arriere = ['arrière']
        #mettre ca en database
        
        liste2 = [[],[],[],[],[],[],[],[],[],[],
                  [],[],[],[],[],[],[],[],[],[]]
        

 
        
        c = 0
        for i in self.reponse:
         
            if i == []:
                c += 1
            else:
                
                for j in dessus:
         
                    if i == j:
                        self.liste[c].append(['dessus','pos'])
                        
                for k in dessous:
                    if i == k:
                        self.liste[c].append(['dessus','pos'])
                        
                for l in meme_pos:
                    if i == l:
                        self.liste[c].append(['meme_pos','pos'])

                for m in devant:
                    if i == m:
                        self.liste[c].append(['devant','pos'])
                        
                for n in arriere:
                    if i == n:
                        self.liste[c].append(['arrière','pos'])

    
                c += 1
   
        return self.liste


    def association_morceau_phrase(self,  liste, reponse):
        self.reponse = reponse
        self.liste = liste

        dessus = ['sur']
        dessous = []
        meme_pos = ['juxtaposées']
        devant = ['devant']
        arriere = ['arrière']
        #mettre ca en database

        liste2 = [[],[],[],[],[],[],[],[],[],[],
                  [],[],[],[],[],[],[],[],[],[]]

        nombre = traitement_reponse.traitement_nombre(self, self.liste)
        #normalement faut capturer l'adjectif aussi

 
        c = 0
        for i in self.liste:
            if i == []:
                pass
            else:
                liste2[c].extend(i)
 
                if i[0][1] == 'pos':
                    c+=1


        return liste2
        











        
































