
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VÉGÉTARIENNE"
        print(f"PIZZA {self.nom} : {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}")
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients)*self.PRIX_PAR_INGREDIENT


pizzas = [
    Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Hawai", 9.5, ("tomate", "ananas", "oignons")),
    Pizza("4 saisons", 11, ("oeuf", "emmental", "tomate", "jambon", "olives")),
    Pizza("Végétarienne", 7.8, ("champignons", "tomate", "oignons", "poivrons"), True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
]


def tri(e):
    return len(e.ingredients)


# pizzas.sort(key=tri)

for i in pizzas:
    i.Afficher()
