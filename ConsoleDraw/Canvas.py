class Canvas():

    def __init__(self, rows=1, columns=1):
        self.rows = rows
        self.columns = columns

    def contains_point(self, row, col):
        print(str(self.rows))
        print(str(self.columns))
        print("checking " + str(row) + ":" + str(col))
        incols = True if (col >= 0 and col < self.columns) else False
        print("incols="+str(incols))
        inrows = True if (row >= 0 and row < self.rows) else False
        print("inrows="+str(inrows))
        result = incols and inrows
        print("result: " + str(result))
        return result

    def render(self):
        s = ""
        for row in range(0, self.rows):
            print("row:"+str(row))
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
