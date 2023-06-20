from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_name1 = "Strogonoff"
    dish_price1 = 22.50

    dish_name2 = "Carne de Panela"
    dish_price2 = 20.80

    dish1 = Dish(dish_name1, dish_price1)
    dish2 = Dish(dish_name2, dish_price2)
    dish1_copy = Dish(dish_name1, dish_price1)

    wrong_price = "33.40"
    wrong_price2 = 0
    wrong_price3 = -3

    # 2.1 - Será validado que seu teste falha caso
    # o atributo name de um prato seja diferente que o passado ao construtor.

    assert dish1.name == dish_name1
    # 2.2 - Será validado que seu teste falha caso
    # os hashes de dois pratos iguais sejam diferentes;

    assert dish1.__hash__() == dish1_copy.__hash__()
    # 2.3 - Será validado que seu teste falha caso
    # os hashes de dois pratos diferentes sejam iguais;

    assert dish1.__hash__() != dish2.__hash__()
    # 2.4 - Será validado que seu teste falha caso a comparação de igualdade de
    # dois pratos iguais (ou de um prato com ele mesmo) seja falsa;

    assert dish1 == dish1_copy
    # 2.5 - Será validado que seu teste falha caso
    # a comparação de igualdade de dois pratos diferentes seja verdadeira;

    assert dish1 != dish2
    # 2.6 - Será validado que seu teste falha caso
    # a implementação do método __repr__ retorne um valor inadequado;

    assert dish1.__repr__() == "Dish('Strogonoff', R$22.50)"
    # 2.7 - Será validado que seu teste falha caso
    # um TypeError não seja levantado ao criar um prato com um valor
    # de tipo inválido;

    with pytest.raises(TypeError) as excinfo:
        Dish(dish_name1, wrong_price)

    assert str(excinfo.value) == "Dish price must be float."
    # 2.8 - Será validado que seu teste falha caso
    # um ValueError não seja levantado ao criar um prato com um valor inválido;

    with pytest.raises(ValueError) as excinfo2:
        Dish(dish_name1, wrong_price2)

    assert str(excinfo2.value) == "Dish price must be greater then zero."

    with pytest.raises(ValueError) as excinfo3:
        Dish(dish_name1, wrong_price3)

    assert str(excinfo3.value) == "Dish price must be greater then zero."
    # 2.9 - Será validado que seu teste falha caso
    # o acesso a um valor do atributo recipe,
    # ao ser indexado com um ingrediente válidoretorne uma quantidade
    # inválida (dica: use o método get do dicionário, por exemplo
    # dish.recipe.get(ingredient));

    dish1.add_ingredient_dependency(Ingredient("queijo mussarela"), 19)
    assert dish1.recipe.get(Ingredient("queijo mussarela")) == 19
    # 2.10 - Será validado que seu teste falha caso
    # o método get_restrictions retorne um set de restrições
    # diferente do esperado;
    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # 2.11 - Será validado que seu teste falha caso
    # o método get_ingredients retorne um set de ingredientes
    # diferente do esperado;
    assert dish1.get_ingredients() == {Ingredient("queijo mussarela")}
