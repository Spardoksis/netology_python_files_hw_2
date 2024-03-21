import os


# Task_0, create_cook_book
def create_cook_book(file_name='recipes.txt'):
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ],
        'Фахитос': [
            {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
            {'ingredient_name': 'Перец сладкий', 'quantity': 1,
             'measure': 'шт'},
            {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Винный уксус', 'quantity': 1,
             'measure': 'ст.л'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ]
    }

    with open(file_name, 'w', encoding='utf-8') as file:
        for dish, ingredients in cook_book.items():
            file.write(f'{dish}\n')
            file.write(f'{len(ingredients)}\n')
            for ingredient in ingredients:
                file.write(f'{ingredient["ingredient_name"]} | '
                           f'{ingredient["quantity"]} | '
                           f'{ingredient["measure"]}\n')
            file.write('\n')


# Task_1, get_cook_book
def get_cook_book_from_file(file_name='recipes.txt'):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = \
                    file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()
        return cook_book


def test_get_cook_book_from_file():
    create_cook_book()
    cook_book = get_cook_book_from_file()
    cook_book_predict = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ],
        'Фахитос': [
            {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
            {'ingredient_name': 'Перец сладкий', 'quantity': 1,
             'measure': 'шт'},
            {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Винный уксус', 'quantity': 1,
             'measure': 'ст.л'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ]
    }
    assert cook_book == cook_book_predict
    print('test_get_shop_list - OK')


# Task_2, shop_list
def get_shop_list(dishes, person_count):
    cook_book = get_cook_book_from_file()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                new_shop_list_item = {}
                new_shop_list_item['measure'] = ingredient['measure']
                new_shop_list_item['quantity'] = \
                    ingredient['quantity'] * person_count
                shop_list[ingredient['ingredient_name']] = new_shop_list_item
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += \
                    new_shop_list_item['quantity'] * person_count
    return shop_list


def test_get_shop_list():
    shop_list = get_shop_list(['Запеченный картофель', 'Омлет'], 2)
    shop_list_predict = {
        'Картофель': {'measure': 'кг', 'quantity': 2},
        'Молоко': {'measure': 'мл', 'quantity': 200},
        'Помидор': {'measure': 'шт', 'quantity': 4},
        'Сыр гауда': {'measure': 'г', 'quantity': 200},
        'Яйцо': {'measure': 'шт', 'quantity': 4},
        'Чеснок': {'measure': 'зубч', 'quantity': 6}
    }
    assert shop_list == shop_list_predict
    print('test_get_shop_list - OK')


# Task_3, sorted_files
def sort_files():
    files = ['1.txt', '2.txt', '3.txt']
    result_file = 'sorted.txt'

    files_data = []
    for file in files:
        with open(os.path.join('sorted', file), 'r', encoding='utf-8') as f:
            data = f.readlines()
            files_data.append((file, len(data), data))

    files_data = sorted(files_data, key=lambda x: x[1])

    with open(os.path.join('sorted', result_file), 'w', encoding='utf-8') as f:
        for file, data_len, data in files_data:
            f.write(f'{file}\n')
            f.write(f'{data_len}\n')
            f.writelines(data)
            f.write('\n')


def test_sorted_files():
    files = ['1.txt', '2.txt', '3.txt']
    files_data = []
    for file in files:
        with open(os.path.join('sorted', file), 'r', encoding='utf-8') as f:
            data = f.readlines()
            files_data.append((file, len(data), data))

    data_predict = []
    predict_files_positions = [1, 0, 2]
    for i in predict_files_positions:
        row = [f'{files_data[i][0]}\n', f'{files_data[i][1]}\n',
               *files_data[i][2]]
        row[-1] = row[-1] + '\n'
        data_predict.extend(row)

    sort_files()
    with open(os.path.join('sorted', 'sorted.txt'), 'r', encoding='utf-8') as f:
        data = f.readlines()
    assert data == data_predict
    print('test_sorted_files - OK')


# Tests
test_get_cook_book_from_file()
test_get_shop_list()
test_sorted_files()
