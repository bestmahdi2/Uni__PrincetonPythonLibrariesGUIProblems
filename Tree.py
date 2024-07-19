import stddraw
import math


def draw_tree(n, x, y, a, branch_radius, m, pen):
    bend_angle = math.radians(15)

    branch_angle = math.radians(37)

    branch_ratio = 0.65

    cx = x + math.cos(a) * branch_radius

    cy = y + math.sin(a) * branch_radius

    stddraw.setPenRadius(0.0001 * pen)

    stddraw.line(x, y, cx, cy)

    if not m:
        return

    draw_tree(n, cx, cy, a + bend_angle - branch_angle, branch_radius * branch_ratio, m - 1, pen - 10)
    draw_tree(n, cx, cy, a + bend_angle + branch_angle, branch_radius * branch_ratio, m - 1, pen - 10)
    draw_tree(n, cx, cy, a + bend_angle, branch_radius * (1 - branch_ratio), m - 1, pen - 10)


if __name__ == '__main__':
    n = 8
    pen = 10 * n

    draw_tree(n, 0.5, 0, math.pi / 2, 0.3, n, pen)

    stddraw.show()
