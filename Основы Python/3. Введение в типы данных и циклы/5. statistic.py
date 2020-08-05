stats = {'facebook': 55, 'yandex': 120, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
maxim = max(stats.values())
max_stats = []
for canal in stats:
    if stats.get(canal) == maxim:
        max_stats.append(canal)
print("Каналы с максимальным объемом:")
for i in max_stats:
    
    print(i, end=" ")
