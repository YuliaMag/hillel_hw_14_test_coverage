import pytest
from staff import pxl


@pytest.mark.parametrize("pixel1, pixel2, expected_red, expected_green, expected_blue", [
    (pxl.Pixel(50, 100, 150), 1.5, 33, 66, 100),
    (pxl.Pixel(25, 50, 75), 3, 8, 16, 25),
    ], ids=["Float value", "Integer value"])
def test_multiplication_invalid_type(pixel1, pixel2, expected_red, expected_green, expected_blue):
    pixel = pxl.Pixel(100, 150, 200)
    with pytest.raises(TypeError):
        pixel / "invalid"


if __name__ == "__main__":
    pytest.main()
