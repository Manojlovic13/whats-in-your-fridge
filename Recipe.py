from Ingredient import Ingredient

class Recipe:
    def __init__(self, id, name, picture, used_ingredients_count = 0, missed_ingredients_count = 0,
     used_ingredients = [], missed_ingredients = [], ingredients_count = 0):
        self.id = id
        self.name = name
        self.picture = picture
        self.used_ingredients_count = used_ingredients_count
        self.missed_ingredients_count = missed_ingredients_count
        self.used_ingredients = used_ingredients
        self.missed_ingredients = missed_ingredients
        self.ingredients_count = self.missed_ingredients_count + self.used_ingredients_count

        if (len(self.used_ingredients) > 0):
            used_ingredient_temp = []

            for x in range(len(self.used_ingredients)):
                used_ingredient_temp.append(Ingredient(self.used_ingredients[x]["name"], self.used_ingredients[x]["id"],
                self.used_ingredients[x]["aisle"], self.used_ingredients[x]["originalString"], self.used_ingredients[x]["image"]))
            
            self.used_ingredients = used_ingredient_temp
        
        if (len(self.missed_ingredients) > 0):
            missed_ingredients_temp = []

            for x in range(len(self.missed_ingredients)):
                missed_ingredients_temp.append(Ingredient(self.missed_ingredients[x]["name"], self.missed_ingredients[x]["id"],
                self.missed_ingredients[x]["aisle"], self.missed_ingredients[x]["originalString"], self.missed_ingredients[x]["image"]))

            self.missed_ingredients = missed_ingredients_temp