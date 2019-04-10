import cv2

#notion de couleur et de taille

class dessin:

    def ouverture_image(self, image):
        self.image = image

        im = cv2.imread(self.image)
        return im
    
    def lignes(self):
        img = dessin.ouverture_image(self, image)
        cv2.line(img, (0, 0), (264, 100), (0, 0, 255))

    def rectangle(self):
        img = dessin.ouverture_image(self, image)
        cv2.rectangle(img, (110, 200), (200, 250), (255, 0, 0), 1)

        
    def cercle(self):
        img = dessin.ouverture_image(self, image)
        cv2.circle(img, (180, 130), 20, (0, 255, 0), 1)


    def image_show(self, image):
        self.image = image

        cv2.imshow("image.jpg", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    #faudra lui faire faire des formes + de l'ia du moin ce que t'a sbité
