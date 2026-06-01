from pywebio.input import input, select, slider
from pywebio.output import put_text, put_success, put_error, put_table, put_markdown
from pywebio import start_server
import math


def school_trip():
    put_markdown("## 🚌 Організація шкільної поїздки")

    students = input(
        "Введіть кількість учнів:",
        type="number"
    )

    teachers = input(
        "Введіть кількість вчителів:",
        type="number"
    )

    transport = select(
        "Оберіть тип транспорту:",
        options=["Автобус", "Поїзд"]
    )

    days = slider(
        "Оберіть кількість днів:",
        min_value=0,
        max_value=14,
        value=1
    )

    if students == 0:
        put_error("Помилка: кількість учнів не може дорівнювати 0")
        return

    total_people = students + teachers

    transport_price = 0
    buses_count = 0

    if transport == "Автобус":
        buses_count = math.ceil(total_people / 40)
        transport_price = buses_count * 5000
    elif transport == "Поїзд":
        transport_price = total_people * 300

    if days == 0:
        hotel_price = 0
    else:
        hotel_price = total_people * 400 * days

    total_price = transport_price + hotel_price

    discount = 0

    if total_people > 30:
        discount = total_price * 0.10

    final_price = total_price - discount

    put_markdown("## 📌 Результат розрахунку")

    result_table = [
        ["Показник", "Значення"],
        ["Кількість учнів", students],
        ["Кількість вчителів", teachers],
        ["Загальна кількість людей", total_people],
        ["Тип транспорту", transport],
        ["Кількість днів", days],
    ]

    if transport == "Автобус":
        result_table.append(["Потрібно автобусів", buses_count])

    result_table.extend([
        ["Вартість транспорту", f"{transport_price} грн"],
        ["Вартість проживання", f"{hotel_price} грн"],
        ["Сума без знижки", f"{total_price} грн"],
        ["Знижка", f"{discount} грн"],
        ["До сплати", f"{final_price} грн"]
    ])

    put_table(result_table)

    if total_people > 30:
        put_success("Застосовано знижку 10%, тому що людей більше ніж 30.")

    if days == 0:
        put_text("Проживання не враховується, тому що кількість днів = 0.")

    if transport == "Автобус" and total_people > 40:
        put_text("Оскільки людей більше 40, потрібно кілька автобусів.")


start_server(school_trip, port=8080, debug=True)