import matplotlib.pyplot as plt
import math

#nommer les planets avec une list []
planetes = [
    
    "Mercure",
    "Vénus",
    "Terre",
    "Mars",
    "Jupiter",
    "Saturne",
    "Uranus",
    "Neptune",
]

r = 5
angles = [2 * math.pi * i / 8 for i in range(8)] #multiplier de 0 à 7 2pi/8 



#calculer x et y avec le rayon et cos/sin des angles 
x = [r * math.cos(angle) for angle in angles] 
y = [r * math.sin(angle) for angle in angles] 
#la boucle for nécessaire afin de calculer une position pour chaque angle


# utiliser scatter de plt afin de dessiner un rond en le nommant le soleil avec label
plt.scatter(0,0, s=500, label="Soleil") # s pour size
plt.text(0, 0, "Soleil")

# utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000
plt.scatter(x,y, s=1000)

for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
    plt.text(x[i], y[i], planetes[i]) #il nomme et place les planète

plt.xlim(-2, 10) #limite de l'axe horizontal x
plt.ylim(-3, 3) #limite de l'axe vertical y

plt.grid() #ajt la grille au graphique
plt.show() #Pour montrer