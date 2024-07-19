import color
import random
import stddraw
import sys

# n = 500000
n = int(sys.argv[1])

stddraw.setPenColor(color.DARK_GREEN)
stddraw.setPenRadius(0)

x, y = 0.0, 0.0

for i in range(n):
    new_x = 0
    new_y = 0
    r = random.randrange(1, 100)

    if r <= 2:
        new_x = 0.50
        new_y = 0.27 * y

    elif r <= 13:
        new_x = -0.139 * x + 0.263 * y + 0.57
        new_y = 0.246 * x + 0.224 * y - 0.036

    elif r <= 15:
        new_x = 0.170 * x - 0.215 * y + 0.408
        new_y = 0.222 * x + 0.176 * y + 0.0893

    # elif r <= 70:
    else:
        new_x = 0.781 * x + 0.034 * y + 0.1075
        new_y = -0.032 * x + 0.739 * y + 0.27

    x = new_x
    y = new_y

    stddraw.point(x, y)
    # stddraw.show(0)

stddraw.show()
