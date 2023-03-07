cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        dish = line.strip()
        for _ in range(int(input_file.readline())):
            ingredient_name, quantity, measure = input_file.readline().strip().split(' | ')
            cook_book[dish] = cook_book.get(dish, []) + [{'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}]
        input_file.readline()

for k, v in cook_book.items():
    print(k)
    print(*v, sep='\n')
    print()
