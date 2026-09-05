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

masses = [
    1.660e-7,   #Mercure
    2.447e-6,   #Vénus
    3.003e-6,   #Terre
    3.227e-7,   #Mars
    9.545e-4,   #Jupiter
    2.857e-4,   #Saturne
    4.366e-5,   #Uranus
    5.151e-5    #Neptune
]  #masses en masses solaires


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

 

for etape in range(10000):
#déclarer x et y dans une liste chaune vides 

# utiliser scatter de plt afin de dessiner un rond en le nommant le soleil avec label
    plt.scatter(0,0, s=500, label="Soleil") #s pour size
    plt.text(0, 0, "Soleil")
# utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000


    for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
        
     # i : planète dont on calcul l’accélération
     # j : une autre planète qui l’attire

        
     #accélération de la planète due au soleil
     
     r2 = math.sqrt(x[i]**2 + y[i]**2)

     ax_total = -G * M * x[i] / r2**3
     ay_total = -G * M * y[i] / r2**3     #gravité en x et y dirigé par le soleil
     
     
     #accélération de la planètes due aux autres planètes
     for j in range(len(planetes)) : 
         
         if i != j : 
             
             dx = x[j] - x[i]
             dy = y[j] - y[i]
             
             distance = math.sqrt(dx**2 + dy**2)
             
             ax_total += G * masses[j] * dx / distance**3
             ay_total += G * masses[j] * dy / distance**3
         
     vx[i] = vx[i] + ax_total * dt 
     vy[i] = vy[i] + ay_total * dt

     x[i] = x[i] + vx[i] * dt
     y[i] = y[i] + vy[i] * dt
     
     
     
    
     plt.text(x[i], y[i], planetes[i]) #il nomme et place les planète

    
    plt.scatter(x,y, s=1000)
    plt.xlim(-32, 32) #limite de l'axe horizontal x
    plt.ylim(-32, 32) #limite de l'axe vertical y
    plt.grid() #ajt la grille au graphique
    plt.pause(0.001)
    plt.clf() #efface les anciennes prositions avant de dessiner une nouvelle position


plt.show() #Pour montrer
 