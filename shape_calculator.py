class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        formatString = f"Rectangle(width={self.width}, height={self.height})"
        return formatString

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        result = self.width * self.height
        return result

    def get_perimeter(self):
        result = 2 * self.width + 2 * self.height
        return result

    def get_diagonal(self): 
        result = (self.width ** 2 + self.height ** 2) ** .5
        return result

    def get_picture(self): 
        width_line = self.width*"*"
        height_line = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else :
            for i in range(self.height-2):
                height_line = height_line + width_line + "\n"
            picture = width_line + "\n" + height_line + width_line + "\n"
            return picture

    def get_amount_inside(self, anatherShape):
        width_count = 0
        heigh_count = 0
        if anatherShape.width < self.width and anatherShape.height < self.height:
            for i in range(1, self.width + 1):
                if i*anatherShape.width <= self.width:
                    width_count = i
            for i in range(1, self.height + 1):
                if i*anatherShape.height <= self.height:
                    heigh_count = i
        return width_count*heigh_count


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        formatString = f"Square(side={self.width})"
        return formatString

    def set_side(self, side):
        self.width = side
        self.height = side
