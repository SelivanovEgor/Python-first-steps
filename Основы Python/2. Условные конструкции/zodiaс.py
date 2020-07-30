try:
    month = str(input("Введите месяц (словом): "))
    num = int(input("Введите число (числом): "))
except:
    print("Невозможно обработать данные! Пожалуйста, введите данные, удовлетворяющие условиям!")
else:
    if month == "март":
        if (num >= 21) and (num <= 31):
            print("Овен")
        elif (num >= 1) and (num < 21):
            print("Рыбы")
    elif month == "апрель":
        if (num >= 1) and (num < 21):
            print("Овен")
        elif (num >= 21) and (num <= 30):
            print("Телец")
    elif month == "май":
        if (num >= 1) and (num < 22):
            print("Телец")
        elif (num >= 22) and (num <= 31):
            print("Близнецы")
    elif month == "июнь":
        if (num >= 1) and (num < 22):
            print("Близнецы")
        elif (num >= 22) and (num <= 30):
            print("Рак")
    elif month == "июль":
        if (num >= 1) and (num < 23):
            print("Рак")
        elif (num >= 23) and (num <= 31):
            print("Лев")
    elif month == "август":
        if (num >= 1) and (num < 24):
            print("Лев")
        elif (num >= 24) and (num <= 31):
            print("Дева")
    elif month == "сентябрь":
        if (num >= 1) and (num < 23):
            print("Дева")
        elif (num >= 23) and (num <= 30):
            print("Весы")
    elif month == "октябрь":
        if (num >= 1) and (num < 23):
            print("Весы")
        elif (num >= 23) and (num <= 31):
            print("Скорпион")
    elif month == "ноябрь":
        if (num >= 1) and (num < 23):
            print("Скорпион")
        elif (num >= 23) and (num <= 30):
            print("Стрелец")
    elif month == "декабрь":
        if (num >= 1) and (num < 22):
            print("Стрелец")
        elif (num >= 22) and (num <= 31):
            print("Козерог")
    elif month == "январь":
        if (num >= 1) and (num < 21):
            print("Козерог")
        elif (num >= 21) and (num <= 31):
            print("Водолей")
    elif month == "февраль":
        if (num >= 1) and (num < 20):
            print("Водолей")
        elif (num >= 20) and (num <= 29):
            print("Рыбы")
    else:
        print("Введены некорректные данные!")