#вариант 1
year = 2023
year = int(input())
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(year)
print (f'год {year}: {result}')

#вариант 2
def is_year_leap(year):
    return year % 4 == 0
print(is_year_leap(2024))
print(is_year_leap(2023))
print(is_year_leap(2022))