from functions import calculate, change_text, sum_numbers


# Завдання 1
print(calculate(10, 5, "sum"))

print(calculate(a=10, b=5, operation="sub"))

data1 = {
    "a": 20,
    "b": 7,
    "operation": "sum"
}
print(calculate(**data1))


# Завдання 2
print(change_text("hello world", True))

print(change_text(text="HELLO WORLD", upper=False))

data2 = {
    "text": "python programming",
    "upper": True
}
print(change_text(**data2))


# Завдання 3
print(sum_numbers("1,2,3", ","))

print(sum_numbers(numbers="10;20;30", separator=";"))
git
data3 = {
    "numbers": "5,15,25",
    "separator": ","
}
print(sum_numbers(**data3))