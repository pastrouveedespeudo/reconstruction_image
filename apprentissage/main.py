from voix import *
from traitement_phrase import *
from sens import *
from database import *


#une voiture
#de quoi est fait une voiture
#de 4 roues, de 6 vitres, d'une antenne et d'un corps



class main:
 
    def question(self):
        
        demande = demande_voix.question_voix(self)
        traitement = traitement_phrase.traitement_nm(self, demande)

        for i in traitement:
            reponse = demande_voix.retour_reponse(self, i)
            liste = traitement_reponse.nombre(self, reponse)
            liste1 = traitement_reponse.nm(self, reponse, liste)
            sens_mot.sens(self, liste1)


if __name__ == "__main__":
    main = main()
    main.question()
