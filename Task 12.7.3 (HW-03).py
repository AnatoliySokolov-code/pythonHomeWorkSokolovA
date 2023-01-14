money = int(input("Введите сумму, которую Вы планируете положить под проценты ,без копеек:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(money*per_cent['ТКБ']/100)
deposit.append(money*per_cent['СКБ']/100)
deposit.append(money*per_cent['ВТБ']/100)
deposit.append(money*per_cent['СБЕР']/100)
print("Макисмальная сумма, которую Вы можете заработать:", max(deposit))
