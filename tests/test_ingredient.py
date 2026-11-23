import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

INGREDIENTS = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 250.5),
]


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS)
    def test_get_type_returns_type_passed_to_constructor(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS)
    def test_get_name_returns_name_passed_to_constructor(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS)
    def test_get_price_returns_price_passed_to_constructor(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
