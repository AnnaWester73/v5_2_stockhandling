from behave import given, when, then


@given('ett tomt lager')
def step_given_empty_stock(context):
    context.stock = []


@given('att lagret innehåller produkten "{name}" med antal {amount:d}')
def step_given_stock_with_product(context, name, amount):
    context.stock = [{"name": name, "amount": amount}]


@when('jag lägger till produkten "{name}" med antal {amount:d}')
def step_when_add_product(context, name, amount):
    context.stock.append({
        "name": name,
        "amount": amount
    })


@when('jag minskar antalet för produkten "{name}" med {amount:d}')
def step_when_decrease_product(context, name, amount):
    for item in context.stock:
        if item["name"] == name:
            item["amount"] -= amount
            return

    raise AssertionError("Produkten finns inte i lagret")


@then('ska produkten finnas i lagret med namn "{name}" och antal {amount:d}')
def step_then_product_exists(context, name, amount):
    product = next((item for item in context.stock if item["name"] == name), None)

    assert product is not None, "Produkten finns inte i lagret"
    assert product["amount"] == amount, "Fel antal på produkten"


@then('ska produkten "{name}" ha antal {amount:d}')
def step_then_product_has_amount(context, name, amount):
    product = next((item for item in context.stock if item["name"] == name), None)

    assert product is not None, "Produkten finns inte i lagret"
    assert product["amount"] == amount, "Fel antal på produkten"