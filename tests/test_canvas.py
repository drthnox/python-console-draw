from ConsoleDraw.Canvas import Canvas

def test_create():
    canvas = Canvas(10, 20)
    assert canvas.rows == 10
    assert canvas.columns == 20
