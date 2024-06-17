persent = 0.1
def bank (deposit, year):
    for i in range(year):
        deposit = deposit + (deposit * persent)
    return print(deposit)
bank(1000, 10)