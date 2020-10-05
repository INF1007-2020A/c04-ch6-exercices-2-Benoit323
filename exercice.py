#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    mydict = dict()
    for index, elem in enumerate(some_list):
        mydict[elem] = index
    return mydict


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    mylist = []
    for i in colors:
        hex_colors = matplotlib.colors.cnames[i]
        mylist.append(tuple([i, hex_colors]))
    return mylist


def create_list() -> list:
    my_list = []
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    my_list = [i for i in range(1, 10000) if i < 15 or i > 350]
    """for i in range(1,10000):
        if i < 15 or i > 350:
            my_list.append(i)
        else:
            continue"""
    return my_list


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    MSE = dict()
    for key, elem in model_dict.items():
        MSE_valeur = 0
        for valeurs in elem:
            MSE_valeur += ((valeurs[0] - valeurs[1]) ** 2)
        MSE[key] = MSE_valeur / len(elem)
    return MSE


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1, 2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
