import pytest
from staff import pxl


@pytest.mark.parametrize("pixel1, pixel2, expected_red, expected_green, expected_blue", [
    (pxl.Pixel(100, 150, 200), pxl.Pixel(50, 70, 100), 50, 80, 100),
    (pxl.Pixel(100, 100, 100), pxl.Pixel(200, 200, 200), 0, 0, 0),
    (pxl.Pixel(0, 0, 0), pxl.Pixel(0, 0, 0), 0, 0, 0),
    (pxl.Pixel(255, 255, 255), pxl.Pixel(255, 255, 255), 0, 0, 0),
], ids=["In range", "Exceeding range", "Lower bound", "Upper bound"])
def test_add_invalid(pixel1, pixel2, expected_red, expected_green, expected_blue):
    pixel1 = pxl.Pixel(100, 255, 100)
    with pytest.raises(ValueError):
        result = pixel1 - pxl.Pixel(300, 255, 0)


if __name__ == "__main__":
    pytest.main()
