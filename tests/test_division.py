import pytest
from staff import pxl


@pytest.mark.xfail(reason="training")
def test_division():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)
    pxl.pixel2 = pxl.Pixel(2, 2, 2)

    result = pxl.pixel1 / pxl.pixel2
    assert result.red == 100
    assert result.green == 100
    assert result.blue == 100
