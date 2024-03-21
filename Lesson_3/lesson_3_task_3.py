from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Неизвестная улица", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Улица Ленина", "20", "15")
mailing = Mailing(to_address, from_address, 100, "ABC123")

print(f"Отправление {mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} "
      f"в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
