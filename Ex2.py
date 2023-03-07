def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in result:
                result[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count
            else:
                result[ingr['ingredient_name']] = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
    return result


cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        dish = line.strip()
        for _ in range(int(input_file.readline())):
            ingredient_name, quantity, measure = input_file.readline().strip().split(' | ')
            cook_book[dish] = cook_book.get(dish, []) + [{'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}]
        input_file.readline()


# for k, v in cook_book.items():
#     print(k)
#     print(*v, sep='\n')
#     print()


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 5)

for k, v in shop_list.items():
    print(k, v['quantity'], v['measure'])
