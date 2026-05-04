from messages import (
    MSG_INPUT_NAME,
    MSG_INPUT_AGE,
    MSG_INPUT_PHONE,
    MSG_NAME_OK,
    MSG_AGE_OK,
    MSG_PHONE_OK,
    MSG_FINISH,
)

name = input(MSG_INPUT_NAME)
name = name.strip()

if name.isalpha():
    name = name.title()
    print(MSG_NAME_OK.format(name=name))


age = input(MSG_INPUT_AGE)
age = age.strip()
age = age.lstrip("0")

if age.isdigit():
    print(MSG_AGE_OK.format(age=age))


phone = input(MSG_INPUT_PHONE)
phone = phone.strip()

if phone.isdigit():
    print(MSG_PHONE_OK.format(phone=phone))


print(MSG_FINISH)