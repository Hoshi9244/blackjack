from carte import Carte 

class Main:
    def __init__(self):
        self.cartes = []

    def tire(self, carte):
        """Ajoute une carte à la main du joueur."""
        self.cartes.append(carte)