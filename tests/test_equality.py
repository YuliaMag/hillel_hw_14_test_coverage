import pytest
from staff import pxl


def test_equality_ok():
    pixel1 = pxl.Pixel(100, 150, 200)
    pixel2 = pxl.Pixel(100, 150, 200)
    pixel3 = pxl.Pixel(50, 75, 100)

    assert pixel1 == pixel2


def test_equality_not_ok():
    pixel1 = pxl.Pixel(100, 150, 200)
    pixel2 = pxl.Pixel(100, 150, 200)
    pixel3 = pxl.Pixel(50, 75, 100)

    assert pixel1 != pixel3


if __name__ == "__main__":
    pytest.main()