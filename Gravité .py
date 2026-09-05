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

 
# stocker l'accélération de chaque planète
ax = [0 for i in range(len(planetes))]
ay = [0 for i in range(len(planetes))]


#position initiale du Soleil
x_soleil = 0
y_soleil = 0

#vitesse initiale du Soleil
vx_soleil = 0
vy_soleil = 0

     
for etape in range(10000):

   
# utiliser scatter afin d'avoir les coordonnée de x et y des planète avec une taille de 1000


#calculer les accélérations
    for i in range(len(planetes)) : #len c'est pour compter le nombre d'une liste
        
     # i : planète dont on calcul l’accélération
     # j : une autre planète qui l’attire

     #accélération de la planète due au soleil :

     #distance du soleil
     dx_soleil = x_soleil - x[i] 
     dy_soleil = y_soleil - y[i]

     rSoleil = math.sqrt(dx_soleil**2 + dy_soleil**2)
     ax_total = G * M * dx_soleil / rSoleil**3
     ay_total = G * M * dy_soleil / rSoleil**3     #accélération gravitationnelle en x et y, dirigée vers le Soleil
     
     
     #accélération de la planètes due aux autres planètes
     for j in range(len(planetes)) : 
         
         if i != j : 
             
             dx = x[j] - x[i]
             dy = y[j] - y[i]
             
             distance = math.sqrt(dx**2 + dy**2)
             
             ax_total += G * masses[j] * dx / distance**3
             ay_total += G * masses[j] * dy / distance**3
             
     ax[i] = ax_total
     ay[i] = ay_total
     
    ax_soleil = 0
    ay_soleil = 0 
#accélération du Soleil due aux planètes
    for i in range(len(planetes)):
        
        dx = x[i] - x_soleil
        dy = y[i] - y_soleil

        distance = math.sqrt(dx**2 + dy**2)

        ax_soleil += G * masses[i] * dx / distance**3
        ay_soleil += G * masses[i] * dy / distance**3
 
 
 # modifier toutes les vitesses des planètes    
    for i in range(len(planetes)) :
         vx[i] = vx[i] + ax[i] * dt 
         vy[i] = vy[i] + ay[i] * dt
    
    # modifier toutes les vitesses du soleil 
    vx_soleil = vx_soleil + ax_soleil * dt
    vy_soleil = vy_soleil + ay_soleil * dt
     
 # modifier toutes les positions des planètes
    for i in range(len(planetes)) :
         x[i] = x[i] + vx[i] * dt
         y[i] = y[i] + vy[i] * dt
        
 #modifier les postions du soleil   
    x_soleil = x_soleil + vx_soleil * dt
    y_soleil = y_soleil + vy_soleil * dt   
    print(x_soleil, y_soleil)
    
    
      
    for i in range(len(planetes)) :      
         plt.text(x[i], y[i], planetes[i]) #il nomme et place les planète  
 
    
    plt.scatter(x_soleil, y_soleil, s=500, label="Soleil") #s pour size
    plt.text(x_soleil, y_soleil, "Soleil")   
    plt.scatter(x,y, s=1000)
    plt.xlim(-32, 32)
    plt.ylim(-32, 32)
    plt.grid() #ajt la grille au graphique
    plt.pause(0.001)
    plt.clf() #efface les anciennes prositions avant de dessiner une nouvelle position
    



plt.show() #Pour montrer
 