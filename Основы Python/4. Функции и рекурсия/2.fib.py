def fib(n):
    if (n == 1) or (n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


try:
    n = int(input("Введите число n: "))
except:
    print("Введите корректные данные!")
else:
    if n < 0:
        print("Введите натуральное число!")
    else:
        print(fib(n))
