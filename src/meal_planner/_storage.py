import json
from dataclasses import asdict
from pathlib import Path

from meal_planner._models import Ingredient, NutritionFacts, Recipe, RecipeIngredient


class JsonRepository:
    def __init__(self, data_dir: Path = Path(__file__).parents[2] / "data"):
        self.ingredients_path = data_dir / "ingredients.json"
        self.recipes_path = data_dir / "recipes.json"

    def load_ingredients(self) -> list[Ingredient]:
        if not self.ingredients_path.exists():
            return []

        text = self.ingredients_path.read_text(encoding="utf-8")
        if not text.strip():
            return []

        raw = json.loads(text)
        return [Ingredient(name=name, per_100g=NutritionFacts(**values)) for name, values in raw.items()]

    def save_ingredients(self, ingredients: list[Ingredient]) -> None:
        existing = self.load_ingredients()

        for ingredient in ingredients:
            existing.append(ingredient)

        raw = {ingredient.name: asdict(ingredient.per_100g) for ingredient in existing}
        self._write(self.ingredients_path, raw)

    def load_recipes(self) -> list[Recipe]:
        if not self.recipes_path.exists():
            return []

        ingredients = self.load_ingredients()
        raw = json.loads(self.recipes_path.read_text(encoding="utf-8"))
        recipes = []

        for recipe_data in raw:
            recipe_ingredients = []
            for entry in recipe_data["ingredients"]:
                name = entry["ingredient"]
                if name not in ingredients:
                    raise KeyError(
                        f"Unknown ingredient '{name}' in recipe '{recipe_data['name']}'",
                    )
                recipe_ingredients.append(
                    RecipeIngredient(
                        ingredient=ingredients[name],
                        quantity_in_g=entry["quantity_in_g"],
                    ),
                )

            recipes.append(
                Recipe(
                    name=recipe_data["name"],
                    ingredients=recipe_ingredients,
                    cooking_time_in_min=recipe_data["cooking_time_in_min"],
                    difficulty=recipe_data["difficulty"],
                    servings=recipe_data.get("servings", 1),
                    tags=recipe_data.get("tags", []),
                    guide=recipe_data.get("guide", ""),
                ),
            )

        return recipes

    def save_recipes(self, recipes: list[Recipe]) -> None:
        raw = [
            {
                "name": recipe.name,
                "servings": recipe.servings,
                "cooking_time_in_min": recipe.cooking_time_in_min,
                "difficulty": recipe.difficulty,
                "tags": recipe.tags,
                "guide": recipe.guide,
                "ingredients": [
                    {
                        "ingredient": entry.ingredient.name,
                        "quantity_in_g": entry.quantity_in_g,
                    }
                    for entry in recipe.ingredients
                ],
            }
            for recipe in recipes
        ]
        self._write(self.recipes_path, raw)

    @staticmethod
    def _write(path: Path, data) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
