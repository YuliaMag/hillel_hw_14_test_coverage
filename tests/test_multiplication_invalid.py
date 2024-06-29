import pytest
from staff import pxl
import sys


@pytest.mark.parametrize("pixel1, pixel2, expected_red, expected_green, expected_blue", [
    (pxl.Pixel(50, 100, 150), 1.5, 75, 150, 225),
    (pxl.Pixel(25, 50, 75), 3, 75, 150, 225),
], ids=["Invalid type with integer values", "Invalid type with float values"])
def test_multiplication_invalid_type(pixel1, pixel2, expected_red, expected_green, expected_blue):
    pixel = pxl.Pixel(100, 150, 200)
    with pytest.raises(TypeError):
        pixel * "invalid"


@pytest.mark.skipif(sys.platform == "win32", reason="To try to skip it conditionally")
@pytest.mark.parametrize("pixel1, pixel2, expected_red, expected_green, expected_blue", [
    (pxl.Pixel(50, 100, 150), 1.5, 75, 150, 225),
    (pxl.Pixel(25, 50, 75), 3, 75, 150, 225),
], ids=["Invalid value with integer values", "Invalid value with float values"])
def test_multiplication_invalid_value(pixel1, pixel2, expected_red, expected_green, expected_blue):
    pixel = pxl.Pixel(100, 150, 200)
    with pytest.raises(ValueError):
        pixel * 0


if __name__ == "__main__":
    pytest.main()
