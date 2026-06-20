class Car:
    def __init__(
        self,
        model: str,
        age: int,
        owner: str | None = None,
        fuel: float = 0
    ) -> None:
        self.model = model
        self.age = age
        self.owner = owner
        self.fuel = fuel

    def __str__(self) -> str:
        owner_info = self.owner if self.owner else "власник не вказаний"

        return (
            f"Автомобіль: {self.model}, "
            f"вік: {self.age} років, "
            f"власник: {owner_info}, "
            f"бензин: {self.fuel} л"
        )

    @property
    def condition(self) -> str:
        if self.age <= 3:
            return "Нове авто"
        elif self.age <= 10:
            return "Середній стан"
        else:
            return "Старе авто"

    @property
    def fuel_status(self) -> str:
        if self.fuel < 10:
            return "Потрібно заправитись"
        elif self.fuel < 30:
            return "Достатньо бензину"
        else:
            return "Можна їхати далеко"


car_1 = Car("Toyota Camry", 2, "Максим", 15)
car_2 = Car("BMW X5", 12)

print(car_1.__dict__)
print(car_2.__dict__)

print(car_1)
print(car_2)

car_1.fuel = 35
car_2.fuel = 7

print(f"\nПісля зміни кількості бензину:")
print(car_1)
print(car_2)

print(f"\nСтан першого авто: {car_1.condition}")
print(f"Стан другого авто: {car_2.condition}")

print(f"Запас пального першого авто: {car_1.fuel_status}")
print(f"Запас пального другого авто: {car_2.fuel_status}")

if car_1.fuel > car_2.fuel:
    print(f"\nУ автомобілі {car_1.model} більше бензину.")
elif car_2.fuel > car_1.fuel:
    print(f"\nУ автомобілі {car_2.model} більше бензину.")
else:
    print("\nВ автомобілях однакова кількість бензину.")