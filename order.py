from letter import LETTER_TEMPLATE


client_name = input("Введіть ім'я та прізвище: ")
trip_date = input("Введіть дату поїздки в Карпати: ")
persons = int(input("Введіть кількість осіб: "))

price_per_person = 15000

total_price = persons * price_per_person

if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0

final_price = total_price - discount

letter = LETTER_TEMPLATE.format(
    name=client_name,
    date=trip_date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=total_price,
    discount=discount,
    final_price=final_price
)

print(letter)