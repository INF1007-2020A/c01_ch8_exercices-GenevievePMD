#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
# Exercice 1
def comparer_fichiers(nom_fichier_1 : str, nom_fichier_2 : str):
    with open(nom_fichier_1, "r") as f1, open(nom_fichier_2, "r") as f2:
        pareille = True

        while pareille:
            a = f1.read(1)  # 1 = pour lire un caractère à la fois
            b = f2.read(1)

            pareille = a == b
        '''
        # Équivalent
        if a!=b
            pareille = False
         '''
        return -1 if pareille else f1.tell()

# Exercice 2
def tripler_espace(nom_fichier_base, nouveau_fichier):
    with open(nom_fichier_base, "r") as data, open(nouveau_fichier, "w") as result:
        result.write(data.read().replace(' ', '   '))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # Définir nos fichiers
    nom_fichier_1 = "fichiertexte1.txt"
    nom_fichier_2 = "fichiertexte2.txt"

    # Exercice 1
    print(comparer_fichiers(nom_fichier_1,nom_fichier_2))

    # Exercice 2
    tripler_espace(nom_fichier_2, "nouveaufichier.txt")

    # Exercice 3


    pass
