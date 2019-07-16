print("Введите размеры таблицы:")
n, m = map(int, input().split())  # n - колличество столбцов, m - строк
s = list(list(0 for q in range(n)) for w in range(m))
columns = list()
lines = list()

print("Введите описание строк:")
for q in range(m):
    lines.append(list(map(int, input().split())))
print("Введите описание столбцов:")
for w in range(n):
    columns.append(list(map(int, input().split())))


def statue_of_liberty(x, n, new, liberty, pos=0, num=0):
    if num >= len(x):
        return [new]
    else:
        returned = list()
        for q in range(liberty + 1):
            if pos + q >= n - x[num] + 1:
                break
            else:
                new_n = new.copy()
                for w in range(x[num]):
                    new_n[w + pos + q] = 1
                for element in statue_of_liberty(x, n, new_n, liberty, pos + q + x[num] + 1, num + 1):
                    returned.append(element)
        return returned


def solve(number, is_line, x, n, m):
    global s
    if is_line:
        liberty = n - sum(x) - len(x) + 1
        spisok = statue_of_liberty(x, n, list(0 for q in range(n)), liberty)
        new_spisok = list(set() for q in range(n))
        for element in spisok:
            flag = True
            for q in range(n):
                if (s[number][q] == 2 and element[q] == 1) or (s[number][q] == 1 and element[q] == 0):
                    flag = False
                    break
            if flag:
                for q in range(n):
                    new_spisok[q].add(element[q])
        for q in range(n):
            if len(new_spisok[q]) == 1:
                if 1 in new_spisok[q]:
                    s[number][q] = 1
                else:
                    s[number][q] = 2
    else:
        liberty = m - sum(x) - len(x) + 1
        spisok = statue_of_liberty(x, m, list(0 for q in range(m)), liberty)
        new_spisok = list(set() for q in range(m))
        for element in spisok:
            flag = True
            for q in range(m):
                if (s[q][number] == 2 and element[q] == 1) or (s[q][number] == 1 and element[q] == 0):
                    flag = False
                    break
            if flag:
                for q in range(m):
                    new_spisok[q].add(element[q])
        for q in range(m):
            if len(new_spisok[q]) == 1:
                if 1 in new_spisok[q]:
                    s[q][number] = 1
                else:
                    s[q][number] = 2


def check(n, m):
    global s
    for q in range(m):
        count = 0
        for w in range(n):
            if s[q][w] == 1:
                count += 1
        if sum(lines[q]) != count:
            return False
    for q in range(n):
        count = 0
        for w in range(m):
            if s[w][q] == 1:
                count += 1
        if sum(columns[q]) != count:
            return False
    return True


def cout(n, m):
    global s
    for q in range(m):
        for w in range(n):
            if s[q][w] == 1:
                print('■', end='')
            elif s[q][w] == 0:
                print('☐', end='')
            else:
                print('☒', end='')
        print('\n', end='')


def round(n, m):
    global rounds
    for q in range(m):
        solve(q, True, lines[q], n, m)
    for q in range(n):
        solve(q, False, columns[q], n, m)
    rounds += 1
    cout(n, m)
    print(rounds)
    if check(n, m):
        return
    else:
        round(n, m)


rounds = 0
round(n, m)
