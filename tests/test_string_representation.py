import pytest
from staff import pxl


@pytest.mark.skip(reason="to practice skip")
def test_str_method():
    pixel1 = pxl.Pixel(255, 128, 64)
    assert str(pixel1) == "Pixel:\t\nRed: 255, Green: 128, Blue: 64"


def test_repr_method():
    pixel2 = pxl.Pixel(255, 128, 64)
    assert repr(pixel2) == "Pixel(255, 128, 64)"


if __name__ == "__main__":
    pytest.main()
