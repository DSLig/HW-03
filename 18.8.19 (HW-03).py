#От 18 до 25 лет — 990 руб.
a = 990
#От 25 лет — полная стоимость 1390 руб.
b = 1390
#больше трёх человек на конференцию, то дополнительно получает 10%
p = 10
#запрашивается количество билетов, которые пользователь хочет приобрести на мероприятие.
try:
    num_of_tickets = int(input('Количество билетов: '))
except ValueError as error:
    print('Вы ввели неправильное число')
finally:
    N = num_of_tickets
#запрашивается возраст посетителя
per = []
for i in range(1,N+1):
    try:
        S = int(input(f'Введите возраст для билета {i}: '))
    except ValueError as error:
        print('Вы ввели неправильное число')
    finally:
        if 0 < S < 110:
            per.append(S)
        else:
            print('Неверный возраст!')
pr = 0
for s in per[:]:
    if 18>s:
        pr += 0
    elif 18 <= s <25:
        pr += a
    else:
        pr += b
if N > 3:
    pc = p / 100
    su = pr * pc 
    price = pr - su
else:
    price = pr

print("Сумма равна: ", price, 'руб.')