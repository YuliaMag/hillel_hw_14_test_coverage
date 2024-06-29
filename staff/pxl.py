class Pixel:

    # The constructor that takes three arguments: red, green, and blue
    def __init__(self, red, green, blue):
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            raise ValueError("ValueError: pixel components must be in range [0, 255]!")
        self._red = red
        self._green = green
        self._blue = blue

    # Implemented property that allows read-only access to the private component field
    @property
    def red(self):
        return self._red

    # Implemented property that allows read-only access to the private component field
    @property
    def green(self):
        return self._green

    # Implemented property that allows read-only access to the private component field
    @property
    def blue(self):
        return self._blue

    # Adding two pixels results in a new Pixel object with components equal to the sum of the corresponding components
    def __add__(self, other):
        new_red = min(255, max(0, self.red + other.red))
        new_green = min(255, max(0, self.green + other.green))
        new_blue = min(255, max(0, self.blue + other.blue))
        return Pixel(new_red, new_green, new_blue)

    # Subtracting two pixels results in a new Pixel object with components equal to the difference of the
    # corresponding components
    def __sub__(self, other):
        new_red = min(255, max(0, self.red - other.red))
        new_green = min(255, max(0, self.green - other.green))
        new_blue = min(255, max(0, self.blue - other.blue))
        return Pixel(new_red, new_green, new_blue)

    # Multiplying two pixels results in a new Pixel object with components equal to the multiplied of the
    # corresponding components. Errors handled
    def __mul__(self, other):
        if isinstance(other, Pixel):
            new_red = min(255, max(0, int(self.red * other.red / 255)))
            new_green = min(255, max(0, int(self.green * other.green / 255)))
            new_blue = min(255, max(0, int(self.blue * other.blue / 255)))
            return Pixel(new_red, new_green, new_blue)
        elif isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("ValueError: multiplier must be greater than zero!")
            new_red = min(255, max(0, int(self.red * other)))
            new_green = min(255, max(0, int(self.green * other)))
            new_blue = min(255, max(0, int(self.blue * other)))
            return Pixel(new_red, new_green, new_blue)
        else:
            raise TypeError("TypeError: multiplier must be an integer or float!")

    def __rmul__(self, other):
        return self.__mul__(other)

    # Dividing two pixels results in a new Pixel object with components equal to the dividing of the
    # corresponding components. Errors handled
    def __truediv__(self, other):
        if isinstance(other, Pixel):
            new_red = min(255, max(0, int(self.red / other.red)))
            new_green = min(255, max(0, int(self.green / other.green)))
            new_blue = min(255, max(0, int(self.blue / other.blue)))
            return Pixel(new_red, new_green, new_blue)
        elif isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("ValueError: divider must be greater than zero!")
            new_red = min(255, max(0, int(self.red / other)))
            new_green = min(255, max(0, int(self.green / other)))
            new_blue = min(255, max(0, int(self.blue / other)))
            return Pixel(new_red, new_green, new_blue)
        else:
            raise TypeError("TypeError: divider must be an integer or float!")

    # Two Pixel objects are considered equal if their corresponding components are equal
    def __eq__(self, other):
        if isinstance(other, Pixel):
            return (self.red, self.green, self.blue) == (other.red, other.green, other.blue)
        return False

    def __str__(self):
        return f"Pixel:\t\nRed: {self.red}, Green: {self.green}, Blue: {self.blue}"

    def __repr__(self):
        return f"Pixel({self.red}, {self.green}, {self.blue})"

    # def __str__(self):
    #     if hasattr(self, "__repr__"):
    #         # return self.__repr__()
    #         return f"Pixel({self.red}, {self.green}, {self.blue})"
    #     else:
    #         return f"Pixel:\t\nRed: {self.red}, Green: {self.green}, Blue: {self.blue}"

