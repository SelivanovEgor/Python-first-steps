def preobr(spisok: list):
    if len(spisok) == 1:
        return spisok[0]
    return {spisok[0]: preobr(spisok[1:])}


spisok = ['2018-01-01', 'yandex', 'cpc', 100, 400, 'google']
print(preobr(spisok))
