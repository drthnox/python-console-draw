from ConsoleDraw import Drawable
from ConsoleDraw.Canvas import Canvas


def test_create():
    canvas = Canvas(height=10,width=10)
    line = Drawable.Line(canvas, 1,1,10,1)
    assert line.is_valid() == True

    line = Drawable.Line(canvas,1, 1, 1, 10)
    assert line.is_valid() == True

    line = Drawable.Line(canvas,1, 1, 2, 2)
    assert line.is_valid() == False


def test_draw():
    canvas = Canvas(height=4, width=5)
    line = Drawable.Line(canvas, 1, 1, 3, 1)
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
    assert str(s).strip() == str(expected).strip()
    line = Drawable.Line(canvas, 1, 1, 1, 3)
    canvas.add(line)
    expected = "+-+-+-+-+-+\n" \
               "|x|x|x| | |\n" \
               "+-+-+-+-+-+\n" \
               "|x| | | | |\n" \
               "+-+-+-+-+-+\n" \
               "|x| | | | |\n" \
               "+-+-+-+-+-+\n" \
               "| | | | | |\n" \
               "+-+-+-+-+-+"
    s = canvas.render()
    assert str(s).strip() == str(expected).strip()
