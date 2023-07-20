import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
        self.speed = 10

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:

            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed *= 1.5





