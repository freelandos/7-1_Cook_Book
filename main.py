def get_cook_book_by_file(file):
    with open(file, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients_count = int(f.readline())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            f.readline()
            cook_book[dish_name] = ingredients_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book_by_file('recipes.txt')
    shop_list = {}
    for dish_name in dishes:
        for ingredient in cook_book[dish_name]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return dict(sorted(shop_list.items()))


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
