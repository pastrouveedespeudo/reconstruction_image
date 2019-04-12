import cv2
from database import *
#notion de couleur et de taille



class dessin:
    def traitement(self, liste):
        self.liste = liste


        forme = visualisation_table.visualisation(self)
        #traitement nombre

        c = 0
        for i in self.liste:
            
            if i == []:
                pass
            else:
                if i[0][1] == 'int':#or numeral et traiteùent_pjrase.traitement_nombre

                    for j in forme:

                    
                        if self.liste[c + 1][0][2] == j[1]:
  
                            for i in range(i[0][0]):
                                dessin.cercle(self)
                                #coordonée différente

                        #elif fome[1 ou 0] 
                
                            
            c+=1

        
    def ouverture_image(self, image):
        self.image = image

        im = cv2.imread(self.image)
        return im
    
    def lignes(self):
        img = dessin.ouverture_image(self, image)
        cv2.line(img, (0, 0), (264, 100), (0, 0, 255))
        dessin.image_show(self, img)

    def rectangle(self):
        img = dessin.ouverture_image(self, image)
        cv2.rectangle(img, (110, 200), (200, 250), (255, 0, 0), 1)
        dessin.image_show(self, img)
        
    def cercle(self):
        img = cv2.imread("trait.png")
        cv2.circle(img, (180, 130), 20, (0, 255, 0), 1)
        
        cv2.imshow("image.jpg", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #remettre les import meme si c une faute d'importer
        
    def image_show(self, image):
        self.image = image

        cv2.imshow("image.jpg", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    #faudra lui faire faire des formes + de l'ia du moin ce que t'a sbité
