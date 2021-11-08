class Voiture:
    def __init__(self, marque, modele, cv, immat):
        self._marque = marque
        self._model = modele
        self._cv = cv
        self._immat = immat

    def afficher_marque(self):
        print(self._marque)

    @staticmethod
    def demarrer():
        print("Vroum, Vroum, ,Pouet, Pouet")


mavoiture = Voiture("Audi", "S5", 333, "AB-123-AC")
mavoiture2 = Voiture("Renauld", "Mégane", 150, "CD-123-DC")

mavoiture.afficher_marque()
mavoiture2.afficher_marque()
Voiture.demarrer()
