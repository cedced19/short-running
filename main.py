

import math

# Input

v1=12.5 # vitesse haute
v2=10 # vitesse basse
n1=3 # temps à la vitesse haute par section
n2=3 # temps à la vitesse basse par section
t3=2 # temps de repos par section
k=0.25 # kilomètre par tour
Ttot=30 # temps total de la session


r1=60/v1
r2=60/v2

t1=r1*k
t2=r2*k

Nombre=int(Ttot/(n1*t1+n2*t2+t3))+1

def n_to_min(n):
    frac, whole = math.modf(n)
    return str(int(whole)) + '\'' +str(int(frac*60))

print('Vous devez courir à la vitesse haute un tour en ' + n_to_min(t1) + ' min ('+ str(n1) +' par section)')
print('Vous devez courir à la vitesse basse un tour en ' + n_to_min(t2) + ' min ('+ str(n2) +' par section)')
print('Nombre de section : ' + str(Nombre))
print('Cela fait')
print(n_to_min(n1*t1*Nombre) + ' min à vitesse haute')
print(n_to_min(n2*t2*Nombre) + ' min à vitesse basse')
print(n_to_min(t3*Nombre)+ ' min de repos')