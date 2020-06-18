# Improting Image class from PIL module
from PIL import Image
import cv2
import numpy as np
import json
import sys
# 1275 × 1753
# 150 x 150
d = {}

if len(sys.argv) != 2:
    print("Invalid Aruguments")
    exit(-1)
# Opens a image in RGB mode
im = Image.open(sys.argv[1])

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size


# Cropped image of above dimension
# (It will not change orginal image)

# left top right bottom
# 1st
im1 = im.crop((1086, 403, 1151, 467))
im2 = im.crop((1150, 403, 1205, 467))
im1.save("1y.png")
im2.save("1n.png")

# 2nd
im1 = im.crop((1086, 468, 1151, 530))
im2 = im.crop((1151, 468, 1205, 530))
im1.save("2y.png")
im2.save("2n.png")

# 3rd
im1 = im.crop((1086, 530, 1149, 594))
im2 = im.crop((1149, 531, 1205, 594))
im1.save("3y.png")
im2.save("3n.png")


# 4th
im1 = im.crop((1086, 594, 1151, 635))
im2 = im.crop((1151, 594, 1207, 635))
im1.save("4y.png")
im2.save("4n.png")

# 5th
im1 = im.crop((1086, 637, 1150, 677))
im2 = im.crop((1150, 637, 1206, 677))
im1.save("5y.png")
im2.save("5n.png")

# 6th
im1 = im.crop((1086, 677, 1150, 740))
im2 = im.crop((1150, 677, 1206, 740))
im1.save("6y.png")
im2.save("6n.png")

# 7th
im1 = im.crop((1086, 741, 1150, 805))
im2 = im.crop((1150, 741, 1206, 805))
im1.save("7y.png")
im2.save("7n.png")

# 8th
im1 = im.crop((1086, 805, 1150, 868))
im2 = im.crop((1150, 805, 1206, 868))
im1.save("8y.png")
im2.save("8n.png")

for i in range(1, 9):
    img = cv2.imread("%dy.png" % (i))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    yes = np.sum(mask == 255)

    img = cv2.imread("%dn.png" % (i))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([110, 50, 50])
    upper_range = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    no = np.sum(mask == 255)

    if yes > no:
        d[i] = "Yes"
    else:
        d[i] = "No"


print(json.dumps(d, indent=4))

