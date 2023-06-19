from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    # a classe pode ser instanciada corretamente de acordo com a assinatura esperada
    ingredient_name = "queijo mussarela"
    ingredient = Ingredient(ingredient_name)
    assert ingredient.name == ingredient_name

    # o método mágico __repr__ funcione como esperado

    assert ingredient.__repr__() == "Ingredient('queijo mussarela')"

    # o método mágico __hash__ funcione como esperado.
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("farinha")
    assert hash(ingredient1) != hash(ingredient2)
    assert hash(ingredient1) == hash(ingredient3)

    # o método mágico __eq__ funcione como esperado

    assert ingredient1.__eq__(ingredient2) == False
    assert ingredient1.__eq__(ingredient1) == True
    # o atributo conjunto restrictions é populado como esperado
    expected_restrictions = {Restriction.ANIMAL_DERIVED, Restriction.LACTOSE}

    assert ingredient.restrictions == expected_restrictions
