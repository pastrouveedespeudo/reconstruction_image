
class demande_voix:
    def question_voix(self):
        demande = input("balance !")

        return demande
        #une voiture

    def retour_reponse(self, mot):
        self.mot = mot
        
        demande = input("décrit moi {} ? ".format(self.mot))
        #demande = input("de quoi est fait {} ? ".format(self.mot))
        #on peut mettre un ou une ou des ou les

        return demande
