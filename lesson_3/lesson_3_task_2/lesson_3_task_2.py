from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy S22", "+79041111111")
phone2 = Smartphone("Apple", "iPhone 7", "+79041725956")
phone3 = Smartphone("Xiaomi", "Mi12", "+79042222222")
phone4 = Smartphone("WindowsPhone", "6", "+79043333333")
phone5 = Smartphone("Nokia", "N 95", "+79044444444")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")