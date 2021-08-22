from ConsoleDraw.Canvas import Canvas


def test_create():
    canvas = Canvas(rows=10, columns=20)
    assert canvas.rows == 10
    assert canvas.columns == 20


def test_contains_point():
    canvas = Canvas(10, 20)
    assert canvas.contains_point(1, 1) == True
    assert canvas.contains_point(11, 1) == False
    assert canvas.contains_point(1, 21) == False


def test_render():
    canvas = Canvas(3, 3)
    assert canvas.render() == "+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n"
