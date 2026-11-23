from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def make_bun(name="black bun", price=100):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun


def make_ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="hot sauce", price=100):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient


@pytest.fixture
def burger():
    return Burger()


class TestBurger:

    def test_new_burger_has_no_bun_and_no_ingredients(self, burger):
        assert (burger.bun, burger.ingredients) == (None, [])

    def test_set_buns_sets_bun(self, burger):
        bun = make_bun()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_appends_ingredient_to_list(self, burger):
        ingredient = make_ingredient()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self, burger):
        first, second = make_ingredient(name="hot sauce"), make_ingredient(name="cutlet")
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.remove_ingredient(0)

        assert burger.ingredients == [second]

    @pytest.mark.parametrize("index, new_index, expected_order", [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2]),
    ])
    def test_move_ingredient_moves_ingredient_to_new_index(
            self, burger, index, new_index, expected_order
    ):
        ingredients = [make_ingredient(name=f"ingredient {i}") for i in range(3)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredients[i] for i in expected_order]

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [], 200),
        (100, [50], 250),
        (200.5, [100, 300], 801),
    ])
    def test_get_price_sums_two_buns_and_all_ingredients(
            self, burger, bun_price, ingredient_prices, expected_price
    ):
        burger.set_buns(make_bun(price=bun_price))
        for price in ingredient_prices:
            burger.add_ingredient(make_ingredient(price=price))

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_receipt(self, burger):
        burger.set_buns(make_bun(name="black bun", price=100))
        burger.add_ingredient(make_ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50))
        burger.add_ingredient(make_ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150))
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )

        assert burger.get_receipt() == expected_receipt
