import time
from random import randint
import os

def log(func):
    if not os.path.exists('./machine.log'):
        os.mknod('./machine.log')
    f = open('machine.log', 'r+')
    f.truncate(0)
    id = os.getlogin()
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        try:
            return func(self, *args, **kwargs)
        finally:
            exec_time = time.time() - start_time
            if exec_time < 1:
                time_unit = "ms"
            else:
                time_unit = "s"
            f = open('machine.log', 'a')
            action = str(func.__name__).replace("_", " ").title()
            f.write("({})Running: {:19}[ exec-time = {:.3f} {} ]".format(id, action, exec_time, time_unit))
            f.write("\n")
            f.close()
    return wrapper

class CoffeeMachine():

    water_level = 100

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
