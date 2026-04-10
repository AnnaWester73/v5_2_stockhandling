from behave import given, when, then
from src.stock import Stock, StockItem


@given('ett tomt lager')
def step_given_empty_stock(context):
    context.stock = Stock()


@given('att lagret innehåller produkten "{name}" med antal {amount:d}')
def step_given_stock_with_product(context, name, amount):
    context.stock = Stock()
    context.stock.add_product(StockItem(name, amount))


@when('jag lägger till produkten "{name}" med antal {amount:d}')
def step_when_add_product(context, name, amount):
    context.stock.add_product(StockItem(name, amount))


@when('jag minskar antalet för produkten "{name}" med {amount:d}')
def step_when_decrease_product(context, name, amount):
    context.stock.decrease_product(name, amount)


@then('ska produkten finnas i lagret med namn "{name}" och antal {amount:d}')
def step_then_product_exists(context, name, amount):
    product = next((item for item in context.stock.items if item.name == name), None)

    assert product is not None, "Produkten finns inte i lagret"
    assert product.name == name, "Fel namn på produkten"
    assert product.amount == amount, "Fel antal på produkten"


@then('ska produkten "{name}" ha antal {amount:d}')
def step_then_product_has_amount(context, name, amount):
    product = next((item for item in context.stock.items if item.name == name), None)

    assert product is not None, "Produkten finns inte i lagret"
    assert product.amount == amount, "Fel antal på produkten"