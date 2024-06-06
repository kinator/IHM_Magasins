import json

# --------------------------------------------------------------------------
# --- class Produit
# --------------------------------------------------------------------------
class Produit:

    #constructeurs
    def __init__(self):
        self.nom : str = None

    def __init__(self,nom_prod : str, price : float):
        self.nom : str = nom_prod
        self.prix : float = price

    @staticmethod
    def buildFromJSon(data: dict):
        return Produit(nom=data['nom'], prix=data['prix'])
    
    def getNom(self):
        return self.nom
    
    def setNom(self, name : str):
        self.nom = name
    
if __name__ == '__main__':
    
    nouv_prod = Produit('bouteille_eau', 4)

    print(nouv_prod.getNom())

    nouv_prod.setNom('Mascara')
    print(nouv_prod.getNom())