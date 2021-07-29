import sys
from wand.image import Image

if len(sys.argv) < 4:
    print('{0} <ORIGINAL PATH> <ROW> <COL>'.format(sys.argv[0]))
    sys.exit()

original_path = sys.argv[1]
row = int(sys.argv[2])
col = int(sys.argv[3])

with Image(filename=original_path) as image:
    print("Original : {0}, {1}".format(image.format, image.size))
    cropped_height = int(image.height/row)
    cropped_width = int(image.width/col)

    for i in range(0, row):
        for j in range(0, col):
            left = j*cropped_width
            right = left + cropped_width
            top = i*cropped_height
            bottom = top + cropped_height

            with image[left:right, top:bottom] as cropped:
                print("Cropped: {0}, {1}".
                      format(cropped.format, cropped.size))
                cropped.save(filename='{0}.{1}.{2}'.
                             format(i, j, original_path))