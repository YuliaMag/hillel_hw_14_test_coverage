import pxl


pix1 = pxl.Pixel(217, 225, 225)
pix2 = pxl.Pixel(225, 225, 225)
pix3 = pxl.Pixel(225, 225, 225)
print(pix1)
print(pix2.red)

print(pix2 + pix1)
print(pix1 - pix2)

print(pix1 * pix2)
print(pix1 / pix2)

print(pix1 == pix2)
print(pix2 == pix3)
