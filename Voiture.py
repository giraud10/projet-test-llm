import sys
import random

class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0

    def accelerer(self, increment):
        self.vitesse += increment

    def freiner(self, decrement):
        self.vitesse -= decrement

    def afficher_informations(self):
        print(f"Marque : {self.marque}")
        print(f"Couleur : {self.couleur}")
        print(f"Vitesse : {self.vitesse} km/h")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        voiture = Voiture(marque=sys.argv[1], couleur=sys.argv[2])
        voiture.accelerer(random.randint(50,150))
        voiture.freiner(random.randint(0,20))
        voiture.afficher_informations()
    else:
        sys.exit('Usage: ./Voiture.py <marque> <couleur>')
