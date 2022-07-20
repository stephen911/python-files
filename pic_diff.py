from PIL import Image, ImageChops
img1 = Image.open("screenshot711.png")
img2 = Image.open("screenshot94.png")
diff = ImageChops.difference(img1, img2)
if diff.getbbox():
    diff.show()