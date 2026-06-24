from abc import ABC, abstractmethod


class Transport(ABC):
    MIN_WORKING_CONDITION = 30

    def __init__(self, fuel: float, condition: float):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self) -> bool:
        """Повертає True, якщо транспорт придатний до роботи."""
        return self.condition >= self.MIN_WORKING_CONDITION

    @property
    @abstractmethod
    def fuel_consumption(self) -> float:
        """Витрата пального на 1 кілометр."""
        pass

    @property
    @abstractmethod
    def condition_wear(self) -> float:
        """Погіршення технічного стану на 1 кілометр."""
        pass

    def move(self, distance: float) -> bool:
        """Переміщує транспорт на вказану відстань."""

        if distance <= 0:
            print("Відстань повинна бути більшою за 0.")
            return False

        if not self.is_working:
            print(f"{self}: рух неможливий — транспорт несправний.")
            return False

        required_fuel = distance * self.fuel_consumption

        if self.fuel < required_fuel:
            print(
                f"{self}: рух неможливий — недостатньо пального. "
                f"Потрібно {required_fuel:.2f} л, доступно {self.fuel:.2f} л."
            )
            return False

        self.fuel -= required_fuel
        self.condition -= distance * self.condition_wear

        # Значення не повинні бути меншими за нуль
        self.fuel = max(0, self.fuel)
        self.condition = max(0, self.condition)

        print(
            f"{self}: успішно подолано {distance} км. "
            f"Витрачено {required_fuel:.2f} л пального."
        )
        return True

    @abstractmethod
    def __str__(self) -> str:
        pass


class Car(Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100)
        self.model = model

    @property
    def fuel_consumption(self) -> float:
        return 0.08

    @property
    def condition_wear(self) -> float:
        return 0.05

    def __str__(self) -> str:
        return (
            f"Автомобіль {self.model} | "
            f"пальне: {self.fuel:.2f} л | "
            f"стан: {self.condition:.2f}%"
        )


class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100)
        self.name = name

    @property
    def fuel_consumption(self) -> float:
        return 0.25

    @property
    def condition_wear(self) -> float:
        return 0.08

    def __str__(self) -> str:
        return (
            f"Вантажівка {self.name} | "
            f"пальне: {self.fuel:.2f} л | "
            f"стан: {self.condition:.2f}%"
        )


class Motorcycle(Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20, condition=100)
        self.brand = brand

    @property
    def fuel_consumption(self) -> float:
        return 0.04

    @property
    def condition_wear(self) -> float:
        return 0.04

    def __str__(self) -> str:
        return (
            f"Мотоцикл {self.brand} | "
            f"пальне: {self.fuel:.2f} л | "
            f"стан: {self.condition:.2f}%"
        )


class ServiceStation:
    def repair(self, transport_unit: Transport) -> None:
        """Покращує технічний стан транспорту на 25 одиниць."""

        if transport_unit.condition >= 100:
            print(f"{transport_unit}: ремонт не потрібний.")
            return

        old_condition = transport_unit.condition
        transport_unit.condition = min(100, transport_unit.condition + 25)

        print(
            f"Транспорт відремонтовано: "
            f"{old_condition:.2f}% → {transport_unit.condition:.2f}%."
        )


car = Car("Toyota Corolla")
truck = Truck("Volvo FH")
motorcycle = Motorcycle("Yamaha")


print("1. Початкова інформація")
print(car)
print(truck)
print(motorcycle)


print("\n2. Перевірка руху")
car.move(100)
truck.move(200)
motorcycle.move(50)


print("\n3. Перевірка is_working")
print(f"Автомобіль працює: {car.is_working}")
print(f"Вантажівка працює: {truck.is_working}")
print(f"Мотоцикл працює: {motorcycle.is_working}")


print("\n4. Перевірка __dict__")
print("Car:", car.__dict__)
print("Truck:", truck.__dict__)
print("Motorcycle:", motorcycle.__dict__)


print("\n5. Перевірка відсутності пального")
car.fuel = 0
car.move(10)


print("\n6. Перевірка поганого технічного стану")
truck.condition = 10
print(f"Вантажівка працює: {truck.is_working}")
truck.move(10)


print("\n7. Створення станції технічного обслуговування")
service_station = ServiceStation()


print("\n8. Ремонт працюючого транспорту")
motorcycle.condition = 70
print("До ремонту:", motorcycle)
service_station.repair(motorcycle)
print("Після ремонту:", motorcycle)


print("\n9. Ремонт повністю зламаного транспорту")
truck.condition = 0
print("До ремонту:", truck)
service_station.repair(truck)
print("Після ремонту:", truck)
print(f"Вантажівка працює: {truck.is_working}")


print("\n10. Кілька ремонтів поспіль")
service_station.repair(truck)
service_station.repair(truck)
service_station.repair(truck)

print("Підсумковий стан:", truck)
print(f"Вантажівка працює: {truck.is_working}")


print("\n11. Ремонт повністю справного транспорту")
motorcycle.condition = 100
service_station.repair(motorcycle)