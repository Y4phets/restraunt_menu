from meals.models import Meals


def get_order_info(data):
    total_price = 0
    allergens = set()
    order = []
    for key in list(data.keys()):
        if key == "csrfmiddlewaretoken":
            continue

        meal = Meals.objects.get(name=key)
        total_price += meal.price
        order.append(meal.name)
        for item in meal.allergens.all():
            allergens.add(item.name)

    return {"price": total_price, "order": order, "allergens": allergens}
