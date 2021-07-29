import sys
from wand.image import Image

types = ('undefined',
         'bilevel',
         'grayscale',
         'grayscalematte',
         'palette',
         'palettematte',
         'truecolor',
         'truecolormatte',
         'colorseparation',
         'colorseparationmatte',
         'optimize',
         'palettebilevelmatte')

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <TYPE>'.format(sys.argv[0]))
    sys.exit()
elif sys.argv[2] not in types:
    print('Available types are : ')
    print(types)
    sys.exit()
    

original_path = sys.argv[1]
type = sys.argv[2]

with Image(filename=original_path) as image:
    with image.clone() as clone:
        clone.type = type
        clone.save(filename= type + "_" + original_path)