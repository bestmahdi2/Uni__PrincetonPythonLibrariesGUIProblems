import math
import random
import color
import stddraw


class Ball:
    def __init__(self, center_x, center_y, r, vx, vy, color=color.BLACK):
        self.center = [center_x, center_y]
        self.radius = r
        self.vx = vx
        self.vy = vy
        self.color = color

        self.minX = -1
        self.minY = -1
        self.maxX = +1
        self.maxY = +1

    def move(self, reverse=False):
        x_value = self.center[0]
        y_value = self.center[1]

        if reverse:
            self.vx = -self.vx
            self.vy = -self.vy
            return

        self.center[0] += self.vx
        self.center[1] += self.vy

        if x_value + self.radius + self.vx > self.maxX:
            self.vx = -self.vx

        elif x_value - self.radius + self.vx < self.minX:
            self.vx = -self.vx

        if y_value + self.radius + self.vy > self.maxY:
            self.vy = -self.vy

        elif y_value - self.radius + self.vy < self.minY:
            self.vy = -self.vy

    def collision(self, b2):
        center_dist = math.hypot(self.center[0] - b2.center[0], self.center[1] - b2.center[1])

        if center_dist <= b2.radius + self.radius:
            return True

        else:
            return False

    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.center[0], self.center[1], self.radius)


class BouncingBall:
    BALL_COUNT = 10
    DT = 15.0
    RADIUS = 0.05
    vx, vy = 0.015, 0.013
    WINDOW_MAX = 1.0

    def __init__(self):
        stddraw.setXscale(-self.WINDOW_MAX, +self.WINDOW_MAX)
        stddraw.setYscale(-self.WINDOW_MAX, +self.WINDOW_MAX)

        stddraw.clear(stddraw.GRAY)

        ball = []
        for i in range(self.BALL_COUNT):
            ball.append(self.create_random_ball())

        last_collision = []

        while True:
            stddraw.clear(stddraw.GRAY)

            for b in ball:
                b.move()
                b.draw()

            stddraw.show(self.DT)

            collision = self.check_collisions(ball)
            if collision:
                if last_collision != collision:
                    last_collision = collision
                    stddraw.show(self.DT)
                    print(collision)
                    ball[collision[0]].move(True)
                    ball[collision[1]].move(True)
                    ball[collision[0]].draw()
                    ball[collision[1]].draw()

    def create_random_ball(self):
        min_pos = -self.WINDOW_MAX + self.RADIUS
        max_pos = self.WINDOW_MAX - self.RADIUS

        rx = random.uniform(min_pos, max_pos)
        ry = random.uniform(min_pos, max_pos)

        b = Ball(rx, ry, self.RADIUS, self.vx, self.vy)

        return b

    def check_collisions(self, b):
        for i in range(len(b) - 1):
            j = i + 1
            while j < len(b):
                if j == 0:
                    return False

                if b[i].collision(b[j]):
                    return [i, j]

                j += 1

        return False


B = BouncingBall()
