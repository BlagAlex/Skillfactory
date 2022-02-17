field = [['-'] * 3 for _ in range(3)]


def show_field(f):
    num = '  0 1 2'
    print(num)
    # zip
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")


def users_input(f, user):
    while True:
        place = input(f" Ходит {user}. \n Введите координаты \n по вертикале и горизонтале: ").split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        # is digit str
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Введите числа: ')
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('Вышли из диапазона: ')
            continue
        if f[x][y] != '-':
            print('Клетка занята!')
            continue
        break
    return x, y


def win_position(f, user):
    f_list = []

    for L in f:
        f_list += L

    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start(field):
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = users_input(field, user)
            field[x][y] = user

        elif count == 9:
            print('Ничья')
            break
        if win_position(field, user):
            print(f"Выиграл {user}")
            break
        count += 1


start(field)
