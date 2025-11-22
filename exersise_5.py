class Vehicle:
    def __init__(self , brand , year):
        self.brand=brand
        self.year=year
    def display_info(self):
        print(f"hello the information about this car is its {self.brand} car and this car use for {self.year} year")
    
class Car(Vehicle):
    def __init__(self, brand, year , numDore):
        super().__init__(brand, year)
        self.numDore = numDore
    def display_info(self):
        super().display_info()
        print(f"and have {self.numDore} dore")


class Motorcycle(Vehicle):
    def __init__(self, brand, year , has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    def display_info(self):
        super().display_info()
        print(f"nad have {self.has_sidecar} ")

vealceCre = Vehicle("bmw" , 3 )
vealceCre.display_info()


care1 = Car("benz" , 5 , 2)
care1.display_info()

motor1 = Motorcycle("honda" , 3 , False)
motor1.display_info()