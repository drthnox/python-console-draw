class Canvas():

    def __init__(self, rows=1, columns=1):
        self.rows = rows
        self.columns = columns

    def contains_point(self, row, col):
        incols = True if (col >= 0 and col < self.columns) else False
        inrows = True if (row >= 0 and row < self.rows) else False
        result = incols and inrows
        return result

    def render(self):
        s = ""
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                s += "+-"
            s += "+\n"
            for col in range(0, self.columns):
                s += "| "
            s += "|\n"
        for col in range(0, self.columns):
            s += "+-"
        s += "+\n"
        return s
