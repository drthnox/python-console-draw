from ConsoleDraw.Canvas import Canvas
from ConsoleDraw.Line import Line


def test_create():
    line = Line(1, 1, 10, 1)
    assert line.is_valid() == True

    line = Line(1, 1, 1, 10)
    assert line.is_valid() == True

    line = Line(1, 1, 2, 2)
    assert line.is_valid() == False


def test_draw():
    canvas = Canvas(4, 5)
    line = Line(1, 1, 3, 1)
    expected = str("""
    +-+-+-+
    | | | |
    +-+-+-+
    | | | |
    +-+-+-+
    | | | |
    +-+-+-+
    """)

    canvas = line.draw(canvas)
