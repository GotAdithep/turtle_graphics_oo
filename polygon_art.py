import turtle
import random


class Polygon:
    def __init__(self):
        self.choice = int(input("Enter number: "))

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class draw_polygon(Polygon):
    def Run_by_Choices(self):
        if self.choice == 1:
            num_sides = 3
            for _ in range(10):  # Draw 5 triangles
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 2:
            num_sides = 4
            for _ in range(10):  # Draw 5 squares
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 3:
            num_sides = 5
            for _ in range(10):  # Draw 5 pentagon
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 4:
            num_sides = 3
            for _ in range(5):  # Draw 5 triangles
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            num_sides = 4
            for _ in range(5):  # Draw 5 squares
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            num_sides = 5
            for _ in range(5):  # Draw 5 pentagon
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 5:
            num_sides = 3
            for _ in range(10):  # Draw 5 triangles
                color = self.get_new_color()
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)


# Setup turtle
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# Create an instance of draw_polygon and run it
polygon_drawer = draw_polygon()
polygon_drawer.Run_by_Choices()

turtle.update()  # Updates the screen with the drawn polygons
turtle.done()
