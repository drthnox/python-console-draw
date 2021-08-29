from ConsoleDraw.Canvas import Canvas


def test_create():
    canvas = Canvas(height=10, width=20)
    assert canvas.height == 10
    assert canvas.width == 20


def test_contains_point():
    canvas = Canvas(10, 20)
    assert canvas.contains_point(1, 1) == True
    assert canvas.contains_point(11, 1) == False
    assert canvas.contains_point(1, 21) == False


def test_render():
    canvas = Canvas(3, 3)
    s = canvas.render()
    print("\nchecking[" + str(s) +"]\n\n\n")
    expected = "+-+-+-+\n" \
               "| | | |\n" \
               "+-+-+-+\n" \
               "| | | |\n" \
               "+-+-+-+\n" \
               "| | | |\n" \
               "+-+-+-+"
    print("expected["+str(expected)+"]")
    assert str(s).strip() == str(expected).strip()