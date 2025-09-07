from abc import ABC, abstractmethod


class SystemBase(ABC):
    @abstractmethod
    def show(self):
        pass

class BenzCoup(SystemBase):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        return f"Car Name: {self.name}, Car Color: {self.color}, Car price: {self.price}$."

class BenzSuv(SystemBase):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        return f"Car Name: {self.name}, Car Color: {self.color}, Car price: {self.price}$."

class BmwCoup(SystemBase):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        return f"Car Name: {self.name}, Car Color: {self.color}, Car price: {self.price}$."

class BmwSuv(SystemBase):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        return f"Car Name: {self.name}, Car Color: {self.color}, Car price: {self.price}$."


class CarFactory(ABC):
    @abstractmethod
    def create_suv(self, name, color, price):
        pass
    @abstractmethod
    def create_coupe(self, name, color, price):
        pass

class BenzFactory(CarFactory):
    def create_suv(self, name, color, price):
        return BenzSuv(name, color, price)
    def create_coupe(self, name, color, price):
        return BenzCoup(name, color, price)

class BmwFactory(CarFactory):
    def create_suv(self, name, color, price):
        return BmwSuv(name, color, price)
    def create_coupe(self, name, color, price):
        return BmwCoup(name, color, price)


if __name__ == "__main__":
    benz_factory = BenzFactory()
    bmw_factory = BmwFactory()

    cars = [
        benz_factory.create_suv("Benz SUV", "Yellow", 5000),
        benz_factory.create_coupe("Benz Coup", "White", 3000),
        bmw_factory.create_suv("BMW SUV", "Dark Red", 4000),
        bmw_factory.create_coupe("BMW Coup", "Black", 5000)
    ]

    for car in cars:
        print(car.show())
