import turtle
import random


class Polygon:
    def __init__(self):
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

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
            reduction_ratio = 0.618
            for _ in range(10):  # Draw 10 triangles with smaller inner triangles
                color = self.get_new_color()  # Set color for all three triangles
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer triangle
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller triangles inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller triangle
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 6:
            num_sides = 4
            reduction_ratio = 0.618
            for _ in range(10):  # Draw 10 squares with smaller inner square
                color = self.get_new_color()  # Set color for all three square
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer square
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller square inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller square
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 7:
            num_sides = 5
            reduction_ratio = 0.618
            for _ in range(10):  # Draw 10 pentagon with smaller inner pentagon
                color = self.get_new_color()  # Set color for all three pentigon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer pentagon
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller pentagon inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller pentagon
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 8:
            num_sides = 3
            reduction_ratio = 0.618
            for _ in range(5):  # Draw 10 triangles with smaller inner triangles
                color = self.get_new_color()  # Set color for all three triangles
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer triangle
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller triangles inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller triangle
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            num_sides = 4
            reduction_ratio = 0.618
            for _ in range(5):  # Draw 10 squares with smaller inner square
                color = self.get_new_color()  # Set color for all three square
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer square
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller square inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller square
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            num_sides = 5
            reduction_ratio = 0.618
            for _ in range(5):  # Draw 10 pentagon with smaller inner pentagon
                color = self.get_new_color()  # Set color for all three pentigon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the large outer pentagon
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Draw two smaller pentagon inside with the same color
                for _ in range(2):
                    size *= reduction_ratio  # Reduce the size
                    turtle.penup()
                    # Move to the new position for the smaller pentagon
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    # Update location for the new position
                    location = [turtle.xcor(), turtle.ycor()]
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        if self.choice == 9:
            reduction_ratio = 0.618
            for _ in range(10):  # Draw 10 random shapes
                # Randomly choose between triangle, square, or pentagon
                num_sides = random.choice([3, 4, 5])
                color = self.get_new_color()  # Set color for the shape and its nested shapes
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                border_size = random.randint(1, 10)

                # Draw the main outer shape
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)

                # Randomly decide how many smaller shapes to draw inside (0, 1, or 2)
                num_inner_shapes = random.randint(0, 2)
                for _ in range(num_inner_shapes):
                    size *= reduction_ratio  # Reduce the size for each inner shape
                    turtle.penup()
                    # Reposition for the inner shape
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    location = [turtle.xcor(), turtle.ycor()]

                    # Draw the inner shape with the same color
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
