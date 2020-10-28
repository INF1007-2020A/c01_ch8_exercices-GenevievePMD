#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import json     # fichiers json
import string

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

# Exercice 3
def grades(note_file, target_file):
    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}
    #results = []

    with open(note_file, 'r') as note_data, open(target_file, 'w') as target:
        for line in note_data.readlines():
            note = float(line)
            for grade in correspondances.keys():
                if grade == 85 and note > grade:
                    #results.append("A* \n")
                    target.write(f'{note} : ' +"A*\n")
                if note <= grade:
                    #results.append(correspondances[grade]+'\n')
                    target.write(f'{note} : ' + correspondances[grade] +'\n')
                    break

        #target.writelines(results)

# Exercice 4
def creer_livre_recettes(fichier_recette):
    reponse_recette = "o"
    reponse_ingredient = "o"
    recettes_ingredients = {}
    ingredients = []

    with open(fichier_recette, 'w') as livre_recettes:
        while reponse_recette == "o" or reponse_recette == "O":
            recette = input("Entrez le nom d'une recette : ")

            while reponse_ingredient == "o" or reponse_ingredient == "O":
                ingredients.append(input("Écrire un ingrédient de la recette : "))
                reponse_ingredient = input("Voulez-vous ajouter un autre ingrédient? (o/n) ")
            recettes_ingredients[recette] = ingredients
            reponse_recette = input("Voulez-vous ajouter une nouvelle recette? (o/n) ")
            reponse_ingredient = "o"
            ingredients = []
        json.dump(recettes_ingredients, livre_recettes, indent=4)

def supprimer_recettes(fichier_recette, recette_a_retirer):
    with open(fichier_recette, 'r') as f:
        livre_recettes = json.load(f)
        for recette, ingredient in livre_recettes.items():
            if recette == recette_a_retirer:
                del livre_recettes[recette]
                print(f'Recette retirée: {recette_a_retirer}')
                break
        with open(fichier_recette, 'w') as livre_recettes_final:
            json.dump(livre_recettes, livre_recettes_final, indent=4)

# Exercice 5
def trouver_nombre_et_ordonner(fichier_texte):
    liste_nombre = []
    with open(fichier_texte, 'r') as contenu:
        for ligne in contenu :
            for mots in ligne.split():
                if mots.isdigit():
                    liste_nombre.append(int(mots))
    return sorted(liste_nombre)


# Exercice 5 - Autre méthode
def nombre_croissant(fichier_texte):
    with open(fichier_texte, 'r') as texte:
        return sorted([int(word) for word in texte.read().split() if word.isdigit()])



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
    correspondance = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}
    grades('notes.txt', "resultats_notes_lettres.txt")

    # Exercice 4
    #creer_livre_recettes("livre_recettes.txt")  # Ajouter des recettes
    #recette_a_retirer = "poutine"
    #supprimer_recettes("livre_recettes.txt", recette_a_retirer) # Retirer recette

    # Exercice 5
    print(trouver_nombre_et_ordonner("exemple.txt"))    # Ma méthode
    print(nombre_croissant("exemple.txt")) # Méthode 2 - plus vite

    pass
