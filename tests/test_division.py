import pytest
from staff import pxl


@pytest.mark.parametrize("pixel1, pixel2, expected_red, expected_green, expected_blue", [
    (pxl.Pixel(50, 100, 150), 1.5, 33, 66, 100),
    (pxl.Pixel(25, 50, 75), 3, 8, 16, 25),
    ], ids=["Float value", "Integer value"])
def test_multiplication(pixel1, pixel2, expected_red, expected_green, expected_blue):
    result = pixel1 / pixel2
    assert result.red == expected_red
    assert result.green == expected_green
    assert result.blue == expected_blue


if __name__ == "__main__":
    pytest.main()
