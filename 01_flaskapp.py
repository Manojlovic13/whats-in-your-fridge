from flask import Flask, redirect, url_for, render_template,request
import requests
import json
import csv
from Ingredient import Ingredient
from Recipe import Recipe
import Components

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    ret_values = []

    if request.method == "GET":
        file = open("top-1k-ingredients.csv")
        csvreader = csv.reader(file)
        most_used_ingredients = []

        for row in csvreader:
            ingredient, id = row[0].split(";")
            most_used_ingredients.append(Ingredient(ingredient, id))

        ret_values.append(most_used_ingredients)

        return render_template("index.html", data = ret_values)
    else:
        # POST METODA
        file = open("top-1k-ingredients.csv")
        csvreader = csv.reader(file)
        most_used_ingredients = []

        for row in csvreader:
            ingredient, id = row[0].split(";")
            most_used_ingredients.append(Ingredient(ingredient, id))
        
        ret_values.append(most_used_ingredients)

        # preuzimanje podataka sa forme
        ingredients = request.form["ingredients"].split(",")[:-1]
        
        url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="

        # append-ovanje na url, kreiranje url-a za API call
        for x in range(len(ingredients)):
            url += ingredients[x]
            if (x != len(ingredients) - 1):
             url += ",+"
        
        url += "&apiKey=" + Components.SPOONACULAR_API_KEY

        # spoonacular API call, i preuzimanje JSON podataka
        response = requests.get(url)
        json_data = json.loads(response.text)


        # parsing JSON u Recipe i Ingredient objekte
        recipes = []
        for x in range(len(json_data)):
            recipes.append(Recipe(json_data[x]["id"], json_data[x]["title"], json_data[x]["image"], json_data[x]["usedIngredientCount"], json_data[x]["missedIngredientCount"],
            json_data[x]["usedIngredients"], json_data[x]["missedIngredients"]))

        ret_values.append(recipes)

        return render_template("index.html", data = ret_values)
        

if __name__ == "__main__":
    app.run(debug=True)