#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
from cmath import polar


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64) #array avec 64 valeurs, répartis entre -1.3 et 2.5


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    a = np.zeros([len(cartesian_coordinates), 2]) # crée un array vide de 0
    
    for i in range(len(cartesian_coordinates)): # pour chaque coordonnée des coordonnées tu trouve un rho 
        rho = np.sqrt(cartesian_coordinates[i][0] ** 2 + cartesian_coordinates[i][1] ** 2)
        phi = np.arctan2(cartesian_coordinates[i][1], cartesian_coordinates[i][0])
        polar_coordinate = (rho, phi)
        a[i] = polar_coordinate

    return a 
    #aurait pu aussi utiliser la librairie c math 

#utilisation de cmath -> convertis en polar direct 
def coordinate_conversion_cmath(cartesian_coordinates: np.ndarray) -> np.ndarray:
    #a = np.zeros([len(cartesian_coordinates), 2]) # crée un array vide de 0
    result = []

    for coord in cartesian_coordinates: # itère sur les éléments de la collection 
        result.append(polar(coord))

    #ce demander si c mieux de intérer sur l'index ou sur les éléments -> comment?
    #for i in range(len(cartesian_coordinates)): # vs ici on itère sur les indexes   
        #a[i] = polar(cartesian_coordinates[i])

    return result

#version boosté
def find_closest_index(values: np.ndarray, number: float) -> int:
    return sorted([(i,values[i]for i in range(value.size))], key= lambda element: abs(element[1]- number))[0][0]
    #très pythonique 
    #values est un tableau numpy, soustraction d'un entier de sur tableau numpy vas faire une soustraction sur chacun des éléments de values 
    #wtf j'ai rien compris 

def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values-number).argmin() #argmin donne index plus petite valeur, np.abs donne tableau avec valeur abs
    #on crée un tableau des différences
    #values est un tableau numpy, soustraction d'un entier de sur tableau numpy vas faire une soustraction sur chacun des éléments de values 
    #prends la valeur abs et vas chercher argmin = index de la plus petite valeur 

#EXERCISE 4 
#trouver chaque point, en 250 points entre 1 et -1, pour chaqu'un de ces points, lui trouver son y, et le mettre dans une figure vide
# = prends fontcion, génère les x et après gère les y 
def samples_from_fonction(func:Callable, start: float, end:float, nb_samples:int) -> tuple:
    x = np.linespace(start, end, num=nb_samples, endpoint=true)
    y = np.array([func(x_i) for x_i in x])
    y2 = sinusoid_np(x)

def graph_sinusoid_sample(x:np.ndarry, y:np.ndarray):
    plt.plot(x,y, 'o' , markersize= 2,5)
    plt.legend(['data'], loc='best')
    plt.show()

def exercie_sin() -> None:
    graph_sinusoid_sample(*samples_from_fonction(sinusoid, -1, 1, 250))

def sinusoid_np(x:np.ndarray) ->np.ndarray:
    #si la fonciton sin, à un seul scalaire, on doit calculer l'image avec math.sin = pas efficace, mieux avec np.sin
    return x**2 np.sin(1/x**2) + x # vas retourner un array 

#EXERCISE 5 - DESSINE FONCITON + CALCULE L'AIRE SOUS LA COURBE 
#pour évlauer une intégrale infini, il faut faire de -infini à 0 et de 0 à l'infini
#ensuite additionne les deux intégrales 
from scipy.intergrate import quad #quad = intégrer des fonctions
def integral(a, b): # 
    def f(x): #defini une fonciton python pour representer la fonciton à interet
        return math.e ** (-1 * x ** 2)

    Ih, err = quad(f, a, b) # dit d'intégrer la fonction entre deux bornes 
    return Ih, err

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    Ih, err = integral(-math.inf, 0) #-infini à 0, trouve l'intégrake de lui grâce à la fonciton integrale qui à quad
    Ih_2, err_2 = integral(0, math.inf) # zero + ininfo, trouve l'integrale de lui aussi
    Ih_tot = Ih + Ih_2
    err_tot = err + err_2
    print(Ih_tot, err_tot)

#commence a calcule x avec linspace, fait un tableay avec les sommets pour traver un polygone, avec mathplot
#trace fonction et le polygone avec plot.setplot 
def draw_integral():
    #calcule des points
    #crée une figure avec mathplot 
    #mettre des polygomes sur cette figue 
    # set la legande 
    a,b = -4, 4 
    x = np.linespace(a,b,100) # cent points, calcule les points bornée entre a et b (100), pour approcher plus
    y= integral(x) # a l'intégral de x 

    _, ax = plt.subplots()
    ax.plot(x,y, 'r', linewidth = 2) # le "r" = rouge, dessiner la serie de points x,y -> dessiner la courbe fonction, dessine ine ligne avec points
    ax.set_ylim(bottom = 0) 
    ax.set_xlim((c-a, b+1))

    ix = np.linespace(a,b) #dessiner l'aire sous la courbe (polygones) 
    iy = integral(ix) 
    verts = [(a, 0), *zip(ix, iy), (b,0)] #*zip = zip = fonciton qui permet d'itérer sur deux lists simultanement ???? comment étais suposé savor ça
    poly = polygone(verts, facecolor= '0.9', edgecolor = '0.5' )
    ax.add_patch(poly)



#EXAMPLE DE FLASK 
@app.route("/", methods = ["GET"])
def home() -> str:
    return f"<h1>{message}</h1>"

@app.route("/update", methodes= ["POST"])
def update() -> str:
    gloabl message
    message = request.json["message"]
    print(f"message received:{message}")

    return "updated"



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
