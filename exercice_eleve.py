
import json

class LivreDeRecettes():

    def __init__(self):
        self.filename = "recettes.json"
        self.id = 0
        with open(self.filename, mode="w") as fichier:
            json.dump({"recettes": []}, fichier, indent=4)

    def ajouter_une_recette(self, nom: str, ingredients: list) -> int:
        with open(self.filename, "r") as fichier:

            recettes = json.load(fichier)
            recettes_liste = recettes["recettes"]
            recettes_liste.append({
                "id": self.id,
                "nom": nom,
                "ingredients": ingredients
            })
        
        with open(self.filename, "w") as fichier:
            json.dump(recettes, fichier, indent=4)
        
        self.id += 1
    
    def recuperer_une_recette(self, recette_id: int) -> tuple:
        with open(self.filename, mode="r") as fichier:

            recettes = json.load(fichier)
            for recette in recettes["recettes"]:
                if recette["id"] == recette_id:
                    return recette["nom"], recette["ingredients"]
            return ("La recette n'existe pas", None)


    

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    livre_de_recettes = LivreDeRecettes()
    livre_de_recettes.ajouter_une_recette("Bouillon", ["Tomates", "ails", "persils"])
    livre_de_recettes.ajouter_une_recette("Boeuf", ["Viande", "sel", "poivre"])
    print(livre_de_recettes.recuperer_une_recette(1))
    pass
