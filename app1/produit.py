import json

# --------------------------------------------------------------------------
# --- class Produit
# --------------------------------------------------------------------------
class Produit:

    #constructeurs
    def __init__(self):
        self.id_prod : int = None
        self.nom : str = None

    def __init__(self,id : int, nom_prod : str):
        self.id_prod : int = id
        self.nom : str = nom_prod

    def getIdProd(self):
        return self.id_prod
    
    def getNom(self):
        return self.nom
    
    def setNom(self, name : str):
        self.nom = name
    
if __name__ == '__main__':
    
    nouv_prod = Produit(0, 'bouteille_eau')

    print(nouv_prod.getIdProd())
    print(nouv_prod.getNom())

    nouv_prod.setNom('Mascara')
    print(nouv_prod.getNom())