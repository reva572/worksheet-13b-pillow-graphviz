from PIL import Image

im = Image.new("RGB", (400, 300), "lavender")
im.save("my_image.png")

image = Image.open("my_image.png")

print("Format:", image.format)
print("Size:", image.size)
print("Mode:", image.mode)

