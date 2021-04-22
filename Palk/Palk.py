"""palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
Найти:
Добавить еще несколько человек и зарплат(кол-во говорит пользователь),
Удалить человека и его зарплату,
Самую большую зарплату и кто ее получает,
Кто получает самую маленькую зарплату и какую именно,
Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,
Узнать, кто получает одинаковую зарплату,
Сделать поиск зарплаты по имени человека,
Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма.

Top3() - 3 самых бедных и самых богатых человека
Keskmine() - Среднюю зарплату и имя человека ее получающего
Tulumaks() - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.

Sort_nimi_jargi() - Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)
Kustutamine() - Находить тех кто получает зарплату ниже средней и удалить их из списков."""

import string

palgad = {"A": 1200, "B": 2550, "C": 750, "D": 395, "E": 1200}  # основной массив
palk = [1200, 2550, 750, 395, 1200]
STRpalk = ["1200", "2550", "750", "395", "1200"]
inimesed = ["A", "B", "C", "D", "E"]


def add(dict, xlist, ylist, qlist):

    name = str(input("Введите имя: "))
    palk = str(input("Введите зарплату: "))

    dict[str(name)] = int(palk)
    xlist.append(str(palk))
    ylist.append(int(palk))
    qlist.append(str(name))
    return {name: dict[name]}


def delit(dict, xlist, ylist, qlist):
    name = str(input("Введите имя: "))

    palgad.pop(name)
    index = qlist.index(name)
    ylist.pop(index)
    xlist.pop(index)
    qlist.pop(index)

    return f"delit: {name}"


def maxx(dict, xlist, ylist, qlist):

    x = str(max(ylist))
    q = xlist.index(x)
    y = max(xlist)
    return qlist[q], ylist[q]


def minn(dict, xlist, ylist, qlist):

    x = str(min(ylist))
    q = xlist.index(x)
    y = min(xlist)
    return qlist[q], ylist[q]


def sortmax(dict, xlist, ylist, qlist):

    xdict = []
    for i in range(len(ylist) - 1):
        for i in range(len(ylist) - 1):
            if ylist[i] > ylist[i + 1]:
                ylist[i], ylist[i + 1] = ylist[i + 1], ylist[i]
                qlist[i], qlist[i + 1] = qlist[i + 1], qlist[i]

    for i in range(len(dict)):
        xdict.append({qlist[i]: ylist[i]})

    return xdict


def sortmin(dict, xlist, ylist, qlist):

    xdict = []
    for i in range(len(ylist) - 1):
        for i in range(len(ylist) - 1):
            if ylist[i] > ylist[i + 1]:
                ylist[i], ylist[i + 1] = ylist[i + 1], ylist[i]
                qlist[i], qlist[i + 1] = qlist[i + 1], qlist[i]

    for i in range(len(dict)):
        xdict.append({qlist[i]: ylist[i]})
    xdict.reverse()

    return xdict


def countt(dict, xlist, ylist, qlist):

    xdict = []
    for i in dict:
        for j in dict:
            if [j, dict.get(j)] in xdict:
                continue
            if ylist.count(dict.get(j)) != 1:
                if dict[i] == dict[j]:
                    xdict.append([j, dict.get(j)])
    return xdict


def palkmorethen():
    palkw = int(input("Больше чем: "))

    palklist = []
    for i in palgad:
        x = palgad.get(i)
        if palkw < x:
            palklist.append({i: x})
    return palklist


def palklessthen():
    palkw = int(input("Меньше чем: "))

    palklist = []
    for i in palgad:
        x = palgad.get(i)
        if palkw > x:
            palklist.append({i: x})
    return palklist


def top3rich(dict, xlist, ylist, qlist):

    for i in range(len(ylist) - 1):
        for i in range(len(ylist) - 1):
            if ylist[i] > ylist[i + 1]:  # можно было просто стрелку повернуть
                ylist[i], ylist[i + 1] = ylist[i + 1], ylist[i]
                qlist[i], qlist[i + 1] = qlist[i + 1], qlist[i]

    if len(dict) >= 3:
        xdict = []
        for i in range(3):
            xdict.append({ylist[::-1][:3][i]: qlist[::-1][:3][i]})  # ну и бредь я придумал
        return xdict
    else:
        return "----> Недостаток людей"


def top3hobo(dict, xlist, ylist, qlist):

    for i in range(len(ylist) - 1):
        for i in range(len(ylist) - 1):
            if ylist[i] > ylist[i + 1]:
                ylist[i], ylist[i + 1] = ylist[i + 1], ylist[i]
                qlist[i], qlist[i + 1] = qlist[i + 1], qlist[i]

    if len(dict) >= 3:
        xdict = []
        for i in range(3):
            xdict.append({ylist[:3][i]: qlist[:3][i]})
        return xdict
    else:
        return "----> Недостаток людей"


def keskminie(dict):
    summ = 0
    for i in dict:
        summ += dict.get(i)

    result = summ / len(dict)
    return result


def Tulumaks(dict):
    hash = []
    for i in dict:

        if int(dict.get(i)) <= 500:
            hash.append({i: dict.get(i)})

        elif int(dict.get(i)) <= 1200 and int(dict.get(i)) >= 501:
            summ = dict.get(i) - 500  # 500 евро не облагается налогом
            summ = summ - summ * 0.3  # от остальной суммы минус налог(в 30%) по Эстонии
            summ += 500  # прибавить к сумме с вычетом налога остальные 500 евро
            hash.append({i: summ})

        elif int(dict.get(i)) >= 1201 and int(dict.get(i)) <= 2099:
            nalog = 500 - 0.55556 * (int(dict.get(i)) - 1200)
            summ = int(dict.get(i)) - nalog
            summ = summ - summ * 0.30 + nalog
            hash.append({i: summ})

        elif int(dict.get(i)) >= 2100:
            summ = int(dict.get(i)) - int(dict.get(i)) * 0.30
            hash.append({i: summ})

    return hash


def Sort_nimi_jargi_min(dict):
    latters = []

    for i in dict.keys():
        latters.append(i)

    return sorted(latters)


def Sort_nimi_jargi_max(dict):
    latters = []

    for i in dict.keys():
        latters.append(i)

    return sorted(latters, reverse=1)


def Kustutamine(dict, xlist, ylist, qlist):
    morethenkeskpalk = []
    dictcopy = dict.copy()
    for i in dictcopy:
        if keskminie(dict) < float(dict[i]):
            morethenkeskpalk.append({i: dict[i]})
        else:
            index = qlist.index(i)
            xlist.pop(index)
            ylist.pop(index)
            qlist.pop(index)
    return morethenkeskpalk


print(f"0.dictt - Показать список \n"
      f"1.add - добавить человека в список\n"
      f"2.delit - удалить человека из списка\n"
      f"3.maxx - показать макс. зарплату\n"
      f"4.minn - показать минимальную\n"
      f"5.sortmax - отсортировать по убыванию \n"
      f"6.sortmin - отсортировать по возростанию\n"
      f"7.countt - посмотреть людей с одинаковой зарплатой\n"
      f"8.palkmorethen - список зарплат от значения 'more then' \n"
      f"9.palklessthen список зарплат от значения 'less then' \n"
      f"10.top3rich - топ3 богачей \n"
      f"11.top3hobo - топ3 бомжей \n"
      f"12.keskmine - средная зарплата\n"
      f"13.tulumaks - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.\n"
      f"14.sortnimimin - Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я\n"
      f"15.sortnimimax - Осуществить сортировку по имени (можно предостваит пользователю выбор от Я до А\n"
      f"16.Kustutamine - Находить тех кто получает зарплату ниже средней и удалить их из списков.\n"
      f"17.nimi - узнать зарплату человека")


while True:

    valik = str(input("Введите функцию: "))

    try:
        if valik == "dictt":
            print(palgad)

        elif valik == "add":
            print(add(palgad, STRpalk, palk, inimesed))

        elif valik == "delit":
            print(delit(palgad, STRpalk, palk, inimesed))

        elif valik == "maxx":
            print(maxx(palgad, STRpalk, palk, inimesed))

        elif valik == "minn":
            print(minn(palgad, STRpalk, palk, inimesed))

        elif valik == "sortmax":
            print(sortmax(palgad, STRpalk, palk, inimesed))

        elif valik == "sortmin":
            print(sortmin(palgad, STRpalk, palk, inimesed))

        elif valik == "countt":
            print(countt(palgad, STRpalk, palk, inimesed))

        elif valik == "nimi":
            nimi = str(input("nimi: "))
            print(palgad[nimi])

        elif valik == "palkmorethen":
            print(palkmorethen())

        elif valik == "palklessthen":
            print(palklessthen())

        elif valik == "top3rich":
            print(top3rich(palgad, STRpalk, palk, inimesed))

        elif valik == "top3hobo":
            print(top3hobo(palgad, STRpalk, palk, inimesed))

        elif valik == "keskmine":
            print(keskminie(palgad))

        elif valik == "tulumaks":
            print(Tulumaks(palgad))

        elif valik == "sortnimimin":
            print(Sort_nimi_jargi_min(palgad))

        elif valik == "sortnimimax":
            print(Sort_nimi_jargi_max(palgad))

        elif valik == "sortminx":
            print(Sort_nimi_jargi_min(palgad))

        elif valik == "sortmaxn":
            print(Sort_nimi_jargi_max(palgad))

        elif valik == "Kustutamine":
            print(Kustutamine(palgad, STRpalk, palk, inimesed))

    except StopAsyncIteration:
        pass

