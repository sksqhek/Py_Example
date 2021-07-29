import sys
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <FLIP|FLOP>'.format(sys.argv[0]))
    sys.exit()

original_path = sys.argv[1]
mode =  str.upper(sys.argv[2])

with Image(filename=original_path) as image:
    with image.clone() as clone:
        if mode == 'FLIP': # LEFT-RIGHT
            clone.flip()
        elif mode == 'FLOP': # TOP-BOTTOM
            clone.flop()
        else:
            print('UNKNOWN MODE : {0}'.format(mode))
            sys.exit()

        clone.save(filename=mode + '_' + original_path)