boys = list(map(str, input(
    "Введите имена мальчиков через пробел(или нажмите enter, чтобы использовать значения по умолчанию): ").split()))
girls = list(map(str, input(
    "Введите имена девочек через пробел(или нажмите enter, чтобы использовать значения по умолчанию): ").split()))
if len(boys) == 0:
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
if len(girls) == 0:
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print("Мы не будем никого знакомить, т.к. кто-то может остаться без пары! Пожалуйста, внесите изменения!")
else:
    boys.sort()
    girls.sort()
    res = list(zip(boys, girls))
    print("Идеальные пары:")
    for couple in res:
        print(couple[0] + ' и ' + couple[1])
