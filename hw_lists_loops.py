# 1

numbers = [1, 5, 2, 8, 3, 7]

max_number = max(numbers)
min_number = min(numbers)
sum_numbers = sum(numbers)

print("Завдання 1")
print("Список чисел:", numbers)
print("Найбільше число:", max_number)
print("Найменше число:", min_number)
print("Сума всіх чисел:", sum_numbers)


# 2

grades = [10, 8, 12, 7, 9]

average_grade = sum(grades) / len(grades)

print()
print("Завдання 2")
print("Оцінки учня:", grades)
print("Середній бал:", average_grade)

print("Оцінки вище середнього:")

for grade in grades:
    if grade > average_grade:
        print(grade)