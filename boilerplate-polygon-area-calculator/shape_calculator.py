class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        height_shape = "*" * self.height
        width_shape = "*" * self.width

        shape = ""
        for i in range(len(height_shape)):
            shape += width_shape + "\n"

        return shape

    def get_amount_inside(self, rectangle):
        number = self.get_area() / rectangle.get_area()
        return int(number)


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super(Square, self).__init__(width=side, height=side)

    def __repr__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height