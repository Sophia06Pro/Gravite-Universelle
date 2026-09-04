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


#ajout de la gravité et la masse
G = 4 * math.pi**2  # constante gravitationnelle en UA³ / an² / masse solaire
M = 1               # masse du Soleil en masse solaire
dt = 0.01           # temps simulé par image, en années


#définir les rayons, les angles initiaux et les vitesses orbitales
r = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.2, 30.1]        #en UA dans l'ordre des planètes
vitesses = [math.sqrt(G*M / rayon) for rayon in r] 
angles = [2 * math.pi * i / 8 for i in range(8)]   

#omega = [vitesses[i] / r[i] for i in range (8)]   # vitesse angulaire de chaque planète
# positions initiales
x = [rayon * math.cos(angle) for rayon, angle in zip(r, angles)]
y = [rayon * math.sin(angle) for rayon, angle in zip(r, angles)]

# vitesses initiales tangentielles
vx = [-vitesses[i] * math.sin(angles[i]) for i in range(8)]
vy = [vitesses[i] * math.cos(angles[i]) for i in range(8)]


 

for etape in range(100):
#déclarer x et y dans une liste chaune vides 

# utiliser scatter de plt afin de dessiner un rond en le nommant le soleil avec label
    plt.scatter(0,0, s=500, label="Soleil") #s pour size
    plt.text(0, 0, "Soleil")
# utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000


    for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
     
     r2 = math.sqrt(x[i]**2 + y[i]**2)

     ax = -G * M * x[i] / r2**3
     ay = -G * M * y[i] / r2**3     #gravité en x et y dirigé par le soleil
     
     vx[i] = vx[i] + ax * dt
     vy[i] = vy[i] + ay * dt

     x[i] = x[i] + vx[i] * dt
     y[i] = y[i] + vy[i] * dt
    
     plt.text(x[i], y[i], planetes[i]) #il nomme et place les planète

    
    plt.scatter(x,y, s=1000)
    plt.xlim(-32, 32) #limite de l'axe horizontal x
    plt.ylim(-32, 32) #limite de l'axe vertical y
    plt.grid() #ajt la grille au graphique
    plt.pause(0.1)
    plt.clf() #efface les anciennes prositions avant de dessiner une nouvelle position


plt.show() #Pour montrer
 