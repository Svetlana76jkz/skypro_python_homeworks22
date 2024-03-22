
from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 12", "+7934567890"))
catalog.append(Smartphone("'Samsung", "Galaxy S21", "+7987654321"))
catalog.append(Smartphone("Google", "Pixel 5", "+7954321890"))
catalog.append(Smartphone("OnePlus", "8 Pro", "+7989456321"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+7976543290"))

for phone in catalog:
    print(f"{phone.brand}, {phone.model}, {phone.phone_number}")