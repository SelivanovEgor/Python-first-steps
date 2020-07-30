print("Введите четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, "
      "потом для второй клетки: ", sep="\n")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8):
    if x1 - 2 == x2:
        if (y1 - 1 == y2) or (y1 + 1 == y2):
            print("YES")
        else:
            print("NO")
    elif x1 - 1 == x2:
        if (y1 - 2 == y2) or (y1 + 2 == y2):
            print("YES")
        else:
            print("NO")
    elif x1 + 1 == x2:
        if (y1 - 2 == y2) or (y1 + 2 == y2):
            print("YES")
        else:
            print("NO")
    elif x1 + 2 == x2:
        if (y1 - 1 == y2) or (y1 + 1 == y2):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("Введены некорректные данные!")