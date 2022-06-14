Notre première classe
Exercice class_livre

Dans cet exercice, nous allons créer une classe pour représenter un livre.

Les instances de cette classe devront posséder les trois attributs suivants :

nom

nombre_de_pages

prix

À partir de cette classe, nous créerons ensuite deux instances de livres.

La première instance devra s'appeler livre_HP et aura comme attributs :

nom = "Harry Potter"

nombre_de_pages = 300

prix = 10.99

La deuxième instance devra s'appeler livre_LOTR et aura comme attributs :

nom = "Le Seigneur des Anneaux"

nombre_de_pages = 400

prix = 13.99

Pensez à utiliser la méthode __init__ et à ne pas oublier le paramètre self !

--------------------------------------------------------------------------
Notes :
Les dataclasses : pour ecrires moi de code lorsque l'on crée des attribut d'instances et donc ne pas a utiliser le self

Pour cela il faut importer le module : from dataclasses import dataclasse

@dataclass
class "nom_de_class":
_repre_ affiche la chaine de caractere avec tout les donner
pour creer des attribut de classes on import la module :
from typing import ClassVar
@dataclass
class "nom_de_class":
    c : ClassVar[int] = ''

LA METHODE __post_init__(self) :
va etre executer juste apres les attribut d'instances
---------------------------------------------------------------------------
Exercice 
Dans cet exercice sur la programmation orientée objet, vous allez devoir créer une classe Voiture, qui doit contenir plusieurs attributs et méthodes afin de la faire fonctionner correctement.

Créez une classe voiture avec un attribut essence qui est égal à 100.

Créez une méthode afficher_reservoir qui affiche le nombre de litres d’essence restant (La voiture contient x litres d’essence).

Créez une méthode roule avec un paramètre km (kilomètre) qui va faire avancer la voiture et vider petit à petit le réservoir. On considère une consommation de 5L pour 100km, l’opération mathématique pour déterminer le nombre de litres d’essence nécessaire en fonction du nombre de kilomètres est donc :
(km * 5) / 100

Si le réservoir est vide quand on essaie de rouler, afficher la phrase : Vous n'avez plus d'essence, faites le plein ! et empêchez la voiture d’avancer.

Si la jauge d’essence descend en dessous de 10L, affichez la phrase : Vous n'avez bientôt plus d'essence !

Créez une méthode faire_le_plein qui remet le niveau d’essence à 100L et qui affiche la phrase Vous pouvez repartir !


