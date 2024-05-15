from cadrillage import Case

# --------------------------------------------------------------------------
# --- class Produit
# --------------------------------------------------------------------------
class Produit:

    #constructeur
    def __init__(self):
        self.nom = None
        self.emplacement = Case((0, 0), True)

    def __init__(self, nom_prod : str, x : int, y : int):
        self.nom = nom_prod
        self.emplacement = Case((x, y), True)