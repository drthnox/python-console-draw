from ConsoleDraw.Canvas import Canvas
from ConsoleDraw.Line import Line


def test_create():
    canvas = Canvas(height=10,width=10)
    line = Line(canvas=canvas, row1=1, col1=1, row2=10, col2=1)
    assert line.is_valid() == True

    line = Line(canvas,1, 1, 1, 10)
    assert line.is_valid() == True

    line = Line(canvas,1, 1, 2, 2)
    assert line.is_valid() == False


def test_draw():
    canvas = Canvas(height=4, width=5)
    line = Line(canvas, 1, 1, 3, 1)
    expected = "+-+-+-+-+-+\n" \
               "|x| | | | |\n" \
               "+-+-+-+-+-+\n" \
               "|x| | | | |\n" \
               "+-+-+-+-+-+\n" \
               "|x| | | | |\n" \
               "+-+-+-+-+-+\n" \
               "| | | | | |\n" \
               "+-+-+-+-+-+"
    canvas.add(line)
    s = canvas.render()
    print("OUTPUT:\n\n" + s)
    assert str(s).strip() == str(expected).strip()
