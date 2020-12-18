#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import json     # fichiers json
import string

# TODO: Définissez vos fonction ici
# Prise 2 - Exercice 1
def comparer_deux_fichiers(nom_fichier1 : str, nom_fichier2:str):
    with open(nom_fichier1, "r", encoding="utf-8") as fichier1, open(nom_fichier2, "r", encoding="utf-8") as fichier2:
        est_pareille = True

        while est_pareille:
            a = fichier1.read(1)
            b = fichier2.read(1)
            est_pareille = a == b

        return fichier1.tell(), a, b

''' 2. Écrire un programme qui recopie un fichier texte en triplant tous les espaces entre les mots. 
(vous pouvez ouvrir deux fichiers avec l’instruction with). '''
def tripler_espace(nom_fichier1: str, nouveau_fichier: str):
    with open(nom_fichier1, "r", encoding="utf-8") as fichier1, open(nouveau_fichier, "w", encoding="utf-8") as nouveau_fichier:
        nouveau_fichier.write(fichier1.read().replace(' ', '   '))


'''3. Écrire un programme qui lit chaque ligne d’un fichier notes.txt (chaque ligne contient une note en pourcentage) 
et qui réécrit, dans un nouveau fichier, les notes avec, à coté, les mentions « A », « B », etc. en 
fonction d’un tableau de correspondance fourni. '''
def correspondance_notes(fichier_notes: str, nouveau_fichier:str):
    correspondances = {0: "E", 20: "F", 40: "D", 50: "C", 70: "B", 80: "A"}
    note_precedente = []

    with open(fichier_notes, "r", encoding="utf-8") as f_notes, open(nouveau_fichier, "w", encoding="utf-8") as f_nouveau:
        for ligne in f_notes:
            note = float(ligne)
            for note_bareme, lettre in correspondances.items():
                if note <= note_bareme:
                    f_nouveau.write(f'{note}% : {note_precedente[1]} \n')
                    break
                if note > 80:
                    if note > 90:
                        f_nouveau.write(f'{note}% : A* \n')
                    else:
                        f_nouveau.write(f'{note}% : A \n')
                    break
                note_precedente = [note_bareme, lettre]

''' 4. Reprenez l’exercice du livre de recettes et créer une base de données dans un fichier qui permet d’ajouter, 
    modifier, supprimer des recettes. Vous êtes libre de choisir le type de format de fichier.
'''
def creation_livre_recette(fichier_recette: str):
    livre_recettes = {}

    reponse = input("Voulez-vous écrire une nouvelle recette? (oui/non) ")

    while reponse == 'oui':
        ingredient = input("Quel est le premier ingrédient? ")
        recette = [ingredient]
        reponse_ingredient = input("Voulez-vous entrer un nouvel ingrédient? (oui/non) ")
        while reponse_ingredient == 'oui':
            ingredient = input("Quel est le nouvel ingrédient? ")
            recette.append(ingredient)
            reponse_ingredient = input("Voulez-vous entrer un nouvel ingrédient? (oui/non) ")

        nom_recette = input("Merci d'avoir partagé cette recette avec nous. Quel est son nom? ")
        livre_recettes[nom_recette] = recette
        reponse = input("Voulez-vous écrire une nouvelle recette? (oui/non) ")
    with open(fichier_recette, 'a', encoding="utf-8") as f_recette:
        json.dump(livre_recettes, f_recette, indent=4)

'''
5. Écrire un programme qui lit un fichier texte [exemple.txt](exemple.txt) et retourne une liste de tous 
les nombres présents dans le fichier, en ordre croissant. 
'''
def retourner_nombre(fichier:str):
    with open(fichier, 'r', encoding="utf-8") as f:
        nombres = []
        for ligne in f:
            liste_mots = ligne.split()
            for mot in liste_mots:
                if mot.isdigit():
                    nombres.append(int(mot))

    return sorted(nombres)

'''
6. Écrire un programme qui lit un fichier et qui recopie une ligne sur deux dans un autre fichier.
'''
def lire_une_ligne_sur_deux(nom_fichier: str):
    with open(nom_fichier, 'r', encoding="utf-8") as f:
        texte = []
        for ligne in f:
            texte.append(ligne.replace('\n', ''))

        for i in range(0, len(texte), 2):
            print(texte[i])


if __name__ == '__main__':
    nom_fichier1 = 'fichiertexte1.txt'
    nom_fichier2 = 'fichiertexte2.txt'
    nouveau_fichier = 'nouveau_fichier2.txt'
    fichier_notes = 'notes.txt'
    fichier_notes_resultats = 'notes_resultats.txt'
    fichier_recette = "livre_recettes.json"
    fichier_exemple = 'exemple.txt'

    # EX1
    print(comparer_deux_fichiers(nom_fichier1, nom_fichier2))

    # EX2
    tripler_espace(nom_fichier1, nouveau_fichier)

    # EX3
    correspondance_notes(fichier_notes, fichier_notes_resultats)

    # EX4
    #creation_livre_recette(fichier_recette)

    # EX5
    print(retourner_nombre(fichier_exemple))

    # EX6
    lire_une_ligne_sur_deux(fichier_exemple)














### ----------------------------------------------------------------------- #
'''
# Exercice 1
def comparer_fichiers(nom_fichier_1 : str, nom_fichier_2 : str):
    with open(nom_fichier_1, "r") as f1, open(nom_fichier_2, "r") as f2:
        pareille = True

        while pareille:
            a = f1.read(1)  # 1 = pour lire un caractère à la fois
            b = f2.read(1)

            pareille = a == b
       
        # Équivalent
        #if a!=b
        #    pareille = False
        
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

'''