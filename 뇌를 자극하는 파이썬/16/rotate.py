import sys
from wand.color import Color
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <DEGREE> [BACKGROUND]'.format(sys.argv[0]))
    sys.exit()

original_path = sys.argv[1]
degree = int(sys.argv[2])
bgcolor = '#FFFFFF'

if len(sys.argv) > 3:
    bgcolor = sys.argv[3]

with Image(filename=original_path) as image:
    with image.clone() as rotated:
        rotated.rotate(degree, background=Color(bgcolor))
        rotated.save(filename=str(degree) + '_' + original_path)