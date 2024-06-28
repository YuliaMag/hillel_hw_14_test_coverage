import pytest
from staff import pxl


def test_multiplication_red():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)

    result = pxl.pixel1.red * 2
    assert result == 200


def test_multiplication_green():
    pxl.pixel2 = pxl.Pixel(100, 150, 200)

    result = pxl.pixel2.green * 2
    assert result == 300


def test_multiplication_blue():
    pxl.pixel3 = pxl.Pixel(100, 150, 200)

    result = pxl.pixel3.blue * 2
    assert result == 400
