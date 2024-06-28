from staff import pxl


def test_subtraction():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)
    pxl.pixel2 = pxl.Pixel(50, 75, 100)
    result = pxl.pixel1 - pxl.pixel2
    assert result.red == 50
    assert result.green == 75
    assert result.blue == 100
