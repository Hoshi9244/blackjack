from carte import Carte 

class Main:
    def __init__(self):
        self.cartes = []

    def tire(self, carte):
        self.cartes.append(carte)

    def __repr__(self):
        return f"Main({self.cartes})"