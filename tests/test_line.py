from ConsoleDraw.Line import Line


def test_create():
    line = Line(1, 1, 10, 1)
    assert line.is_valid() == True

    line = Line(1, 1, 1, 10)
    assert line.is_valid() == True

    line = Line(1, 1, 2, 2)
    assert line.is_valid() == False
