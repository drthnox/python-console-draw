class Canvas():

    def __init__(self, height=1, width=1):
        self.height = height
        self.width = width

    def contains_point(self, row, col):
        incols = True if (col >= 0 and col < self.width) else False
        inrows = True if (row >= 0 and row < self.height) else False
        result = incols and inrows
        return result

    def render(self):
        s = ""
        for row in range(0, self.height):
            for col in range(0, self.width):
                s += "+-"
            s += "+\n"
            for col in range(0, self.width):
                s += "| "
            s += "|\n"
        for col in range(0, self.width):
            s += "+-"
        s += "+\n"
        return s
