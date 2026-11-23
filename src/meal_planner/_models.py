from dataclasses import dataclass, field


@dataclass(frozen=True)
class NutritionFacts:
    calories: float = 0.0
    carbohydrate: float = 0.0
    fat: float = 0.0
    protein: float = 0.0

    def __add__(self, other: NutritionFacts) -> NutritionFacts:
        return NutritionFacts(
            self.calories + other.calories,
            self.carbohydrate + other.carbohydrate,
            self.fat + other.fat,
            self.protein + other.protein,
        )

    def __mul__(self, factor: float) -> NutritionFacts:
        return NutritionFacts(
            self.calories * factor,
            self.carbohydrate * factor,
            self.fat * factor,
            self.protein * factor,
        )


@dataclass
class Ingredient:
    name: str
    per_100g: NutritionFacts


@dataclass
class RecipeIngredient:
    ingredient: Ingredient
    quantity_in_g: float

    @property
    def NutritionFacts(self) -> NutritionFacts:
        return self.ingredient.per_100g * (self.quantity_in_g / 100)


@dataclass
class Recipe:
    name: str
    ingredients: list[RecipeIngredient]
    cooking_time_in_min: int
    difficulty: int  # 1 = easy, 2 = medium, 3 = hard
    servings: int = 1
    tags: list[str] = field(default_factory=list)
    guide: str = ""

    @property
    def NutritionFacts_for_recipe(self) -> NutritionFacts:
        return sum((z.NutritionFacts for z in self.ingredients), start=NutritionFacts())

    @property
    def NutritionFacts_per_serving(self) -> NutritionFacts:
        return self.NutritionFacts_for_recipe * (1 / self.servings)

    def __post_init__(self) -> None:
        if self.difficulty not in (1, 2, 3):
            raise ValueError("difficulty must be 1, 2, or 3")
