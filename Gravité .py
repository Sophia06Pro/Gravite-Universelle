import matplotlib.pyplot as plt

#1 : nommer les planets avec une list []
planetes = [
    
    "Mercure",
    "Venus",
    "Terre",
    "Mars",
    "Jupitère",
    "Saturne",
    "Uranus",
    "Neptune",
]

#2 : faire une liste de cordonnée x et y avec des listes
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 0, 0, 0, 0, 0, 0, 0]

# 3 : utiliser scatter de plt afin de dessiner un rond en le nommant le soleil avec label
plt.scatter(0,0, s=500, label="Soleil") # s pour size
plt.text(0, 0, "Soleil")

#4 : utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000
plt.scatter(x,y, s=1000)

for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
    plt.text(x[i], y[i], planetes[i]) #il écrit et nomme les planète

plt.xlim(-2, 10) #limite de l'axe horizontal x
plt.ylim(-3, 3) #limite de l'axe vertical y

plt.grid #ajt la grille au graphique

plt.show()