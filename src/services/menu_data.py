# Req 3
from models.dish import Dish
from models.ingredient import Ingredient
import csv

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish = Dish(row["dish"], float(row['price']))
                dish.add_ingredient_dependency(Ingredient(row["ingredient"]) , int(row["recipe_amount"]))
                self.dishes.add(dish) 

# menu = MenuData("data/menu_base_data.csv")
# print(menu.dishes)




