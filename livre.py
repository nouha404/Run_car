class Livre:
    nom = 'Le Seigneur des Anneaux'
    nombre_de_pages = 300
    prix = 10.99
    
    def __init__(self, nom):
        self.nom = nom
  
livre_HP = Livre('Harry Potter')

livre_LOTR = Livre(Livre.nom)
livre_LOTR.nombre_de_pages = 400
livre_LOTR.prix = 13.99



""" SOlution
class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
        
livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99

        """

    