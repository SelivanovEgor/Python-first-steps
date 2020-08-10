import codecs


def get_shop_list_by_dishes(dishes: list, person_count: int = 0):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for dictionary in cook_book.setdefault(dish):
                if dictionary.get('ingredient_name') not in result:
                    result[dictionary.get('ingredient_name')] = {
                        'quantity': int(dictionary.get('quantity')) * person_count,
                        'measure': dictionary.get('measure')}
                else:
                    quantity = result.get(dictionary.get('ingredient_name')).get('quantity')
                    result[dictionary.get('ingredient_name')]['quantity'] = quantity + int(dictionary.get('quantity')
                                                                                           ) * person_count
    print('{} {} {} {} {}'.format('Ингредиенты, нужные для приготовления блюд', dishes, 'для', person_count,
                                  'персон:'))
    print(result)


file_recipe = codecs.open('recipe.txt', 'r', 'utf-8')

lines = file_recipe.read().splitlines()
sort_lines = [[]]
l = 0
for i in lines:
    if i != '':
        sort_lines[l].append(i)
    else:
        l += 1
        sort_lines.append([])
ingredients = [[] for i in range(len(sort_lines))]
cook_book = {sort_lines[i][0]: ingredients[i] for i in range(0, len(sort_lines))}
for i in range(0, len(sort_lines)):
    l = 2
    for j in range(0, int(sort_lines[i][1])):
        res = sort_lines[i][l].split(' | ')
        ingredients[i].append({'ingredient_name': res[0], 'quantity': res[1], 'measure': res[2]})
        l += 1
print("Словарь из блюд:")
print(cook_book, '\n')
get_shop_list_by_dishes(["Омлет", "Оладьи"], 2)
file_recipe.close()
