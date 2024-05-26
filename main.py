from PIL import Image

im = Image.open(input("Enter the path of the image: "))

print("Succesfull loaded the image")
print("Image size: ", im.size)

width, height = im.size

all_pixels = []
for x in range(width):
    for y in range(height):
        pixel = im.getpixel((x, y))
        all_pixels.append(pixel)


average_hue = []

for x in all_pixels:
    sum = 0
    for y in x:
        sum += y
    sum = sum / 3
    average_hue.append(sum)

ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

result = []
for x in average_hue:
    result.append(ASCII_CHARS[(int(x / 255 * len(ASCII_CHARS) - 1))])


for x in range(height):
    for y in range(width):
        print(result[x * y], end="")
