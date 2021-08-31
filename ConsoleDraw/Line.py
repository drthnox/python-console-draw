from ConsoleDraw.AbstractDrawable import AbstractDrawable

class Line(AbstractDrawable):

    def __init__(self, canvas, row1, col1, row2, col2):
        super().__init__(canvas)
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2

    def is_valid(self):
        return self.row1 == self.row2 or self.col1 == self.col2

    def draw(self):
        r1 = self.row1
        r2 = self.row2
        c1 = self.col1
        c2 = self.col2
        if self.row1 < 0:
            r1 = 0
        if self.row2 < 0:
            r2 = 0
        if r1 > self.canvas.height:
            r1 = self.canvas.height
        if r2 > self.canvas.height:
            r2 = self.canvas.height
        if self.col1 < 0:
            c1 = 0
        if self.col2 < 0:
            c2 = 0
        if c1 > self.canvas.width:
            c1 = self.canvas.width
        if c2 > self.canvas.width:
            c2 = self.canvas.width
        for row in range(0, abs(r1-r2)+1):
            for col in range(0, abs(c1-c2)+1):
                self.canvas.pixels[row,col] = 1
        return self.canvas
