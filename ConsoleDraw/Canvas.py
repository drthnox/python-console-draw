import numpy as np

class Canvas():
    pixels = []
    drawables = list()

    def __init__(self, height=1, width=1):
        self.height, self.width = (height, width)
        # self.pixels = [[0]*self.width]*self.height
        self.pixels = np.zeros([height,width], int)
        # self.drawables = list(AbstractDrawable)

    def contains_point(self, row, col):
        incols = True if (col >= 0 and col < self.width) else False
        inrows = True if (row >= 0 and row < self.height) else False
        result = incols and inrows
        return result

    def render(self):
        for drawable in self.drawables:
            drawable.draw()
        s = ""
        for row in range(0, self.height):
            for col in range(0, self.width):
                s += "+-"
            s += "+\n"
            for col in range(0, self.width):
                s += "|"
                if self.pixels[row,col] == 0:
                    s += ' '
                else:
                    s += 'x'
            s += "|\n"
        for col in range(0, self.width):
            s += "+-"
        s += "+"
        return str(s).strip()

    def add(self, drawable):
        self.drawables.append(drawable)