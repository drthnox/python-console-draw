from ConsoleDraw.Command import Command


class Line(Command):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        pass

    def is_valid(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def draw(self, canvas):
        if self.x1 <= 0 or self.x1 > canvas.width:
            return canvas
        elif self.x2 <= 0 or self.x2 > canvas.width:
            return canvas
        elif self.y1 <= 0 or self.y1 > canvas.height:
            return canvas
        elif self.y2 <= 0 or self.y2 > canvas.height:
            return canvas
        # TODO: draw the line on the canvas
        return canvas
