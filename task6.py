a = int(input('Сколько километров пробежал спортсмен в первый день?: '))
b = int(input('Сколько всего километров нужно пробежать спортсмену?: '))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
    print(f'В {day} день пробежал {a:.2f} километров')
print(f'Спортсмен пробежит {b} километров на {day} день')
