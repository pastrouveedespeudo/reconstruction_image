from voix import *
from traitement_phrase import *



class main:
    def question(self):
        
        demande = demande_voix.question_voix(self)
        traitement = traitement_phrase.traitement_nm(self, demande)

        for i in traitement:
            demande_voix.retour_reponse(self, i)




if __name__ == "__main__":
    main = main()
    main.question()
