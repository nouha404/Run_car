from dataclasses import dataclass
from typing import ClassVar

class Voiture:
    essence : int = 100
    
    def rouler(self, km):
        self.essence -= km * 0.05
        
        while self.essence <= 0:
            return f"Vous n'avez plus d'essence, faites le plein !"
        
        if self.essence < 10 and self.essence >= 0:
            return f"Vous n'avez bientôt plus d'essence ! \n La voiture contient {self.essence}L d'essence"
        
        return f'{self.essence}'
    
    def faire_le_plein(self):
        self.essence = 100
        return f"Vous pouvez repartir !"
        
    def afficher_reservoir(self):
        return f'La voiture contient {self.essence} litres d’essence'


