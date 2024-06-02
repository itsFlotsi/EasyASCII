import sys
from sys import argv
from PIL import Image

# Import the image_path

OUTPUT = "output.txt"

CHARSET = " .:-=+*#%@"


def create_string(img):
    string = ""
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            index = int(pixel / 255 * (len(CHARSET) - 1))
            string += CHARSET[index]
            string += CHARSET[index]

        string += "\n"
    return string


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit()
    img = Image.open(argv[1])
    img = img.convert("L")

    output = create_string(img)

    with open(OUTPUT, "w") as file:
        file.write(output)
