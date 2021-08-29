from ConsoleDraw.AbstractDrawable import AbstractDrawable


class Canvas():
    global pixels
    global drawables

    def __init__(self, height=1, width=1):
        self.height, self.width = (height, width)
        self.pixels = [[0]*width]*height
        # self.drawables = list(AbstractDrawable)

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
                # TODO draw pixel logic here
            s += "|\n"
        for col in range(0, self.width):
            s += "+-"
        s += "+"
        print("\n\nreturning[" + str(s) +"]\n\n\n")
        return str(s).strip()

    def draw(self, drawable):
        pass