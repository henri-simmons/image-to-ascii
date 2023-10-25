from PIL import Image
import sys

text = sys.argv[1]


# Load the image and print out its size
im = Image.open(text)
rgb_im = im.convert("RGB")
print("Successfully loaded image!")
print(f"Image size: {im.size[0]} x {im.size[1]}")

def split(list_a, chunk):
    for i in range(0, len(list_a), chunk):
        yield list_a[i:i + chunk]

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Create a matrix for each pixel
matrix = []

# Iterate through the image
for y in range(im.size[1]):
    matrix.append([])
    for x in range(im.size[0]):
        pixel = im.getpixel((x, y))
        brightness = (pixel[0] + pixel[1] + pixel[2]) // 3
        brightness = brightness // 4
        matrix[y].append(chars[brightness])

# Convert the matrix to a list of strings
ascii_art = [''.join(row) for row in matrix]

# Print the ASCII art
for line in ascii_art:
    print(line)

count = 0
for i in matrix:
	for x in i:
		count += 1
print(count)
