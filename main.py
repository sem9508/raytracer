import math
import time

from vector import *
from sphere import *
from light import *
from utils import *
from floor import *
from rendering import *

if __name__ == "__main__":
    res = input('840 or 4k? ')
    if res == '4k':
        print('rendering in 4k')
        width, height = 3840, 1920
    else:
        print('rendering in 840')
        width, height = 840, 460
        
    image = render(width, height)
    print(f'It took: {round(time.process_time())} seconds.')
    save_image(image, width, height, "output.png", "PNG")