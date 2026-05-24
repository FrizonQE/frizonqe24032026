import requests

url = "https://dummyjson.com/recipes"

response = requests.get(url)
data = response.json()

recipes = data["recipes"]

pizza_recipes = []

italian_count = 0

max_calories_recipe = recipes[0]

recipes_190 = []

total_reviews = 0

for recipe in recipes:
    if "pizza" in recipe["name"].lower():
        pizza_recipes.append(recipe["name"])

    if recipe["cuisine"] == "Italian":
        italian_count += 1

    if recipe["caloriesPerServing"] > max_calories_recipe["caloriesPerServing"]:
        max_calories_recipe = recipe

    first_instruction = recipe["instructions"][0]

    if "190°C" in first_instruction:
        recipes_190.append(recipe["name"])

    total_reviews += recipe["reviewCount"]


print(
    "Рецепти піци:",
    pizza_recipes,
    "\nКількість страв італійської кухні:",
    italian_count,
    "\nНайбільш калорійна страва:",
    max_calories_recipe["name"],
    "-",
    max_calories_recipe["caloriesPerServing"],
    "калорій",
    "\nСтрави, які готуються при температурі 190°C:",
    recipes_190,
    "\nЗагальна кількість переглядів / відгуків усіх рецептів:",
    total_reviews
)