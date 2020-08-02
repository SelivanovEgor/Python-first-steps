geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
num = 1
geo_logs_filtr = []
for visit in geo_logs:
    if visit.get('visit' + str(num))[1] == 'Россия':
        geo_logs_filtr.append(visit)
    num += 1
print("Отфильтрованный список geo_logs:")
for visit in geo_logs_filtr:
    print(visit)