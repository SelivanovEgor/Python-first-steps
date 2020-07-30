n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Введите число k: "))
if k > n * m:
    print("NO")
else:
    if (k % n == 0) or (k % m == 0):
        print("YES")
    else:
        print("NO")
