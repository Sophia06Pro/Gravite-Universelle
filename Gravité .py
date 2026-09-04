import matplotlib.pyplot as plt
import math

plt.ion() #active le mode interactif de Matplotlib

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


#ajout de rayon, de l'angle et de la vitesse
r = [i for i in range(2, 10) ]
angles = [2 * math.pi * i / 8 for i in range(8)] #multiplier de 0 à 7 2pi/8 

omega = [0.5 for i in range (8)]  # vitesse angulaire de chaque planète

vitesses = [omega[i] * r[i] for i in range(8)] #calculer 

for etape in range(100):
#déclarer x et y dans une liste chaune vides 
    x = []
    y = []

    
    for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste    
        angles[i] = angles[i] + omega[i] # faire avancer l'angle de chaque planète
    

#calculer x et y avec le rayon et cos/sin des angles
    for rayon, angle in zip(r, angles) : # zip associe les éléments de deux listes deux par deux
         x.append(rayon * math.cos(angle)) #append : ajoute la valeur à la fin de la liste.
         y.append(rayon * math.sin(angle)) 
#la boucle for nécessaire afin de calculer une position pour chaque angle

# utiliser scatter de plt afin de dessiner un rond en le nommant le soleil avec label
    plt.scatter(0,0, s=500, label="Soleil") #s pour size
    plt.text(0, 0, "Soleil")
# utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000


    for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
     plt.text(x[i], y[i], planetes[i]) #il nomme et place les planète
    

    
    plt.scatter(x,y, s=1000)
    plt.xlim(-10, 10) #limite de l'axe horizontal x
    plt.ylim(-10, 10) #limite de l'axe vertical y
    plt.grid() #ajt la grille au graphique
    plt.pause(0.1)
    plt.clf() #efface les anciennes prositions avant de dessiner une nouvelle position


plt.show() #Pour montrer
 