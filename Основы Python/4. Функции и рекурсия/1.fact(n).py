def fact(n):
    factor = 1
    for i in range(2, n + 1):
        factor *= i
    return factor


def fact_1(n):
    if n == 0:
        return 1
    return fact_1(n - 1) * n

try:
    n = int(input("Введите число n: "))
except:
    print("Введите корректные данные!")
else:
    if n < 0:
        print("Введите натуральное число!")
    else:
        print(fact(n))
        print(fact_1(n))
