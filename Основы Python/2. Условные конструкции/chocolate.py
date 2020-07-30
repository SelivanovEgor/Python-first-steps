try:
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))
    k = int(input("Введите число k: "))
except:
    print("Вы ввели не числа!")
else:
    if k > n * m:
        print("NO")
    else:
        try:
            if (k % n == 0) or (k % m == 0):
                print("YES")
            else:
                print("NO")
        except:
            print("Введите корректные данные!")
