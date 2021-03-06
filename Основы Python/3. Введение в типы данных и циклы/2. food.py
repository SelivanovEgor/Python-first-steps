cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ],
  ['запеканка',
      [
        ['картофель', 100, 'гр.'],
        ['мясо', 80, 'гр.'],
        ['лук', 10, 'гр.'],
        ['грибы', 20, 'гр.'],
      ]
  ]
]
try:
    person = int(input("Введите количество людей, на которых необходимо приготовить данные блюда: "))
except:
    print("Введите корректные данные!")
else:
    for i in range(0, len(cook_book)):
        print(cook_book[i][0] + ":")
        for j in range(0, len(cook_book[i][1])):
            for k in range(len(cook_book[i][1][j])):
                if k == 1:
                    print(cook_book[i][1][j][k] * person, end=" ")
                else:
                    print(cook_book[i][1][j][k], end=" ")
            print("")
        print("")