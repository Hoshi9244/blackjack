class Carte:
    
    def __init__(self, nom, valeur):
        self.nom = nom       # le nom de cette carte uniquement, ex: "K"
        self.valeur = valeur # la valeur numérique de la carte, ex: 10

    def __repr__(self):
        return f"Carte('{self.nom}', {self.valeur})"
