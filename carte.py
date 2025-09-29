class Carte:
    
    def __init__(self, nom, valeur):
        self.nom = ["As","K","Q","J",10,9,8,7,6,5,4,3,2]
        self.valeur = valeur

    def __str__(self):
        return f"{self.nom} ({self.valeur})"