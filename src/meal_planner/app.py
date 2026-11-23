from meal_planner._storage import JsonRepository

my_data = JsonRepository()

# Create and save a new ingredient
# Example:
# chicken_breast = Ingredient("chicken_breast", NutritionFacts(102.0, 0.0, 0.7, 22.0))
# jasmine_rice = Ingredient("jasmine_rice", NutritionFacts(350.0, 78.0, 0.7, 7.1))
# broccoli = Ingredient("broccoli", NutritionFacts(34.0, 2.7, 0.3, 3.4))
# my_data.save_ingredients([chicken_breast, jasmine_rice, broccoli])
