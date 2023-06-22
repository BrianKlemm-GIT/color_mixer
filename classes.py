class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def print_colors(self):  # I used this method for debugging
        return (f"Red = {self.red}, Green = {self.green}, Blue = {self.blue}")

    def return_red_value(self):
        return self.red

    def return_green_value(self):
        return self.green

    def return_blue_value(self):
        return self.blue
