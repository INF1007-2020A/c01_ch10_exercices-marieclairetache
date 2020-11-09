#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
from cmath import polar


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    a = np.zeros([len(cartesian_coordinates), 2]) # crée un array vide de 0

    for i in range(len(cartesian_coordinates)): # pour chaque coordonnée des coordonnées tu trouve un rho 
        rho = np.sqrt(cartesian_coordinates[i][0] ** 2 + cartesian_coordinates[i][1] ** 2)
        phi = np.arctan2(cartesian_coordinates[i][1], cartesian_coordinates[i][0])
        polar_coordinate = (rho, phi)
        a[i] = polar_coordinate

    return a 
     #aurait pu aussi utiliser la librairie c math 

def coordinate_conversion_cmath(cartesian_coordinates: np.ndarray) -> np.ndarray:
    #a = np.zeros([len(cartesian_coordinates), 2]) # crée un array vide de 0
    result = []
    for coord in cartesian_coordinates: # itère sur les éléments de la collections 
        result.append(polar(coord))

    #for i in range(len(cartesian_coordinates)): # vs ici on itère sur les indexes   
        #a[i] = polar(cartesian_coordinates[i])

    return result
#version boosté
def find_closest_index(values: np.ndarray, number: float) -> int:
    return sorted([(i,values[i]for i in range(value.size))], key= lambda element: abs(element[1]- number))[0][0]
    #très pythonique 
    #wtf j'ai rien compris 

def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values-number).argmin() 
    #values = tableay nompy, lorsque on fait soustraction sur tableau, ça soustrait les éléments (ex tab=1,1 tab-1 = 0,0)
    #prends la valeur abs et vas chercher argmin = index de la plus petite valeur 
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
