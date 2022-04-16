class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return self.height + self.height + self.width + self.width

  def get_diagonal(self):
    return ((self.height ** 2 + self.width ** 2) ** .5)

  def get_picture(self):
    pic = ""
    if self.width <= 50 and self.height <= 50:
      for w in range(self.height):
        pic += ("*" * self.width)  + "\n"
      return pic
    return "Too big for picture."

  def get_amount_inside(self, other):
    left_right = round(self.width / other.width)
    top_bottom = round(self.height / other.height)
    return left_right * top_bottom  

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side
