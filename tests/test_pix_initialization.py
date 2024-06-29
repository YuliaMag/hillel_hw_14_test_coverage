import pytest
from staff import pxl


@pytest.mark.parametrize("red, green, blue, expected_error", [
    (100, 150, 200, None),
    (256, 150, 200, ValueError),
    (100, -1, 200, ValueError),
    (100, 150, 300, ValueError)
], ids=["correct values", "red is incorrect", "green is incorrect", "blue is incorrect"])
def test_pix_initialization(red, green, blue, expected_error):
    if expected_error:
        with pytest.raises(expected_error):
            pxl.Pixel(red, green, blue)
    else:
        pixel = pxl.Pixel(red, green, blue)
        assert pixel.red == red
        assert pixel.green == green
        assert pixel.blue == blue


if __name__ == "__main__":
    pytest.main()
    