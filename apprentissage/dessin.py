import cv2
from database import *
#notion de couleur et de taille



class dessin:
    def traitement(self, liste):
        self.liste = liste

        forme = visualisation_table.visualisation(self)

        #toute la notion haut bas sur pos

        pos = []

        
        c = 0
        for i in self.liste:
            if i == []:
                pass
            else:
       
                for j in i:
                    try:
                       if j[2] == 'rond':
                           if i[-1][-1] == 'pos' and i[-1][-2] == 'devant':
                               av = dessin.cercle_devant(self)
                               pos.append(av)
                           elif i[-1][-1] == 'pos' and i[-1][-2] == 'arrière':
                               ar = dessin.cercle_arriere(self)
                               pos.append(ar)
                           #print(self.liste[c + 1]) meme pos
                           
                       elif j[2] == 'rectangle':
                           dessin.rectangle(self, pos[0][0], pos[0][1], pos[1][0])
                           #triche
                                         

                           
                       elif j[2] == 'carre':
                           pass
                    except:
                        pass
            c+=1
        

        dessin.image_show(self)


        
    def ouverture_image(self, image):
        self.image = image

        im = cv2.imread(self.image)
        return im
    
    def lignes(self):
        img = dessin.ouverture_image(self, image)
        cv2.line(img, (0, 0), (264, 100), (0, 0, 255))
        dessin.image_show(self, img)

    def rectangle(self, pts1, pts2, pts3):
        
        self.pts1 = pts1
        self.pts2 = pts2
        self.pts3 = pts3
        
        img = cv2.imread("trait.png")
        cv2.rectangle(img, (self.pts1, self.pts2), (self.pts3, 80), (255, 0, 0), 1)
        cv2.imwrite("trait.png", img)
        
    def cercle_devant(self):
        
        img = cv2.imread("trait.png")

        #devant
        devant_bas = int(round(img.shape[1] * 10 / 100))
        devant_droite = int(round(img.shape[0] * 60 / 100))
        
        cv2.circle(img, (devant_bas, devant_droite), 20, (0, 255, 0), 1)
        
        cv2.imwrite("trait.png", img)
    
        return devant_bas, devant_droite
   
    def cercle_arriere(self):
        
        img = cv2.imread("trait.png")

        #derriere
        arriere_bas = int(round(img.shape[1] * 40 / 100))
        arriere_droite = int(round(img.shape[0] * 60 / 100))

        
        #en haut
        #en bas
        #ect

        cv2.circle(img, (arriere_bas, arriere_droite), 20, (0, 255, 0), 1)
        cv2.imwrite("trait.png", img)
        return arriere_bas, arriere_droite
        
    def image_show(self):

        image = dessin.ouverture_image(self, 'trait.png')
        cv2.imshow("image.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    #faudra lui faire faire des formes + de l'ia du moin ce que t'a sbité
