from staff import pxl


def test_equality_ok():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)
    pxl.pixel2 = pxl.Pixel(100, 150, 200)
    pxl.pixel3 = pxl.Pixel(50, 75, 100)

    assert pxl.pixel1 == pxl.pixel2


def test_equality_not_ok():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)
    pxl.pixel2 = pxl.Pixel(100, 150, 200)
    pxl.pixel3 = pxl.Pixel(50, 75, 100)

    assert pxl.pixel1 != pxl.pixel3
