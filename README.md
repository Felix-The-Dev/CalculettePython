# CalculettePython
Une calculette graphique réalisée en Python avec Tkinter

## Documentation

### Lancement et Fonctionnement général
La calculette se lance soit en lançant le script calculette.py directement, soit en important le module dans un autre programme python comme ceci :
```py
from calculette import *

calculette = UltimateCalculator()
calculette.open()
```

C'est la classe UltimateCalculator qui représent la calculette. Elle hérite de la classe Tk de Tkinter et est donc porteuse de la fenêtre qui s'ouvre.
Chacune de ses méthodes sont commentées.

### Caractéristiques

Cette calculatrice présente 3 modes interchangeables en cliquant sur le titre en haut et en choissant entre :

#### Standard
La calculatrice ne présente que les opérations mathématiques élémentaires

#### Scientifique
Permet de rajouter : 
- les parenthèses, 
- racine carrée et puissance
- les fonctions trigonométriques usuelles (sin, cos, tan) ainsi que pi
et en cliquant sur l'option 2nd :
- la racine cubique
- les arc-s des fonctions trigonométriques usuelles
- le modulo (mod)
- le pourcentage
- la multiplication par une puissance de 10 pour les notations scientifiques

Il y a possibilité de basculer entre les grandients et les degrès en cliquant sur deg ou rad.


#### Experte
Tout comme la scientifique avec en plus :
- le logarythme
- le nombre d'or, phi
- la constante exponentielle e
- les fonctions :
    - bin pour convertir un entier en binaire
    - hex pour convertir un entier en hexadécimal
    - dec pour convertir un binaire en entier




On remarquera également :

- La présence d'une touche C pour effacer complétement l'expression. Celle ci devient C-h, c'est à dire "Clear Historique" lorsque la touche 2nd est enfoncée
et permet explicitement de vider l'historique.

- La touche rouge permet d'enlever le dernier caractère entré (alternative à la touche du clavier du même effet)

- Le clavier est tout à fait utilisable pour taper plus vite ! 

- La calculatrice présente un historique des calculs. Pour récupérer la dernière **expression** entrée, taper ⬅, pour récupérer le dernier résultat, taper ⭡

- Lorque on entre une opérations mathématiques élémentaires alors que rien n'a été entré dans l'expression, le programme insère automatiquement le dernier résultat derrière cette expression.

- Il est possible d'utiliser une notation sans multiplier pour les constantes pi, phi et e, le programme l'ajoute automatiquement dans son calcul interne. Par exemple : `31e` ou `3π/2`

- Toutes les opérations sont combinables. Il est donc possible de réaliser de longs calculs tels que `12*6 - log15 * sin(12*6/3)` ou `π*6 + e**6 - 10%520 - √(52*6)` d'un seul coup. Cela suggère dans le code pas mal de remplacements et de conditions car toutes ses fonctions doivent être utilisés par python le plus souvent sous de telles formes : `12/3*math.log(45)-math.degrees(math.sin(math.radians((12*6/3))))` ce qui n'est pas très agréable à l'oeil, il faut en convenir ^^

- Attention cependant, certains longs calculs peuvent générer de longs résultats et peuvent sortir de l'écran ou déranger la disposition générale. Pour pouvoir tout voir en entier, il suffit de redimentionner.





Ce projet était très amusant à faire ^^