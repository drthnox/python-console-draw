from ConsoleDraw.AbstractDrawable import AbstractDrawable


class Line(AbstractDrawable):

    def __init__(self, row1, col1, row2, col2):
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2

    def is_valid(self):
        return self.row1 == self.row2 or self.col1 == self.col2

    def draw(self, canvas):
        if self.row1 <= 0 or self.row1 > canvas.width:
            return canvas
        elif self.row2 <= 0 or self.row2 > canvas.width:
            return canvas
        elif self.col1 <= 0 or self.col1 > canvas.height:
            return canvas
        elif self.col2 <= 0 or self.col2 > canvas.height:
            return canvas
        # TODO: draw the line on the canvas
        return canvas
