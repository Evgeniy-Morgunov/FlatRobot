# pygame and sys libraries importing
import pygame as pg
import random
import enum

'''def parceline(f):
    return list(map(int, f.readline()[:-1].split()))'''


class command(enum.Enum):
    right = 1
    left = 2
    up = 3
    down = 4
    clean = 5
    dirt = 6
    cl = 7
    none = 8


class obj:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Environment:

    def __init__(self):
        self.objects = []
        self.m, self.n = (random.randint(3, 20), random.randint(3, 20))
        self.flat = list()
        for i in range(self.m):
            k = []
            for j in range(self.n):
                if random.random() < 0.5:
                    k.append(command.dirt)
                else:
                    k.append(command.cl)
            self.flat.append(k)
        y, x = random.randint(0, self.n - 1), random.randint(0, self.m - 1)
        self.objects.append(obj(x, y))

    def check(self):
        for i in self.objects:
            if i.x > self.m - 1:
                i.x = self.m - 1
            if i.y > self.n - 1:
                i.y = self.n - 1
            if i.y < 0:
                i.y = 0
            if i.x < 0:
                i.x = 0

    def event(self, f):
        if f == command.up:
            e.objects[0].y -= 1
        if f == command.down:
            e.objects[0].y += 1
        if f == command.left:
            e.objects[0].x -= 1
        if f == command.right:
            e.objects[0].x += 1
        if f == command.clean:
            e.flat[e.objects[0].x][e.objects[0].y] = command.cl

    def type(self):
        k = [e.flat[e.objects[0].x][e.objects[0].y]]

        if e.objects[0].x + 1 > self.m - 1:
            k.append(command.none)
        else:
            k.append(e.flat[e.objects[0].x + 1][e.objects[0].y])

        if e.objects[0].x - 1 < 0:
            k.append(command.none)
        else:
            k.append(e.flat[e.objects[0].x - 1][e.objects[0].y])

        if e.objects[0].y + 1 > self.n - 1:
            k.append(command.none)
        else:
            k.append(e.flat[e.objects[0].x][e.objects[0].y + 1])

        if e.objects[0].y - 1 < 0:
            k.append(command.none)
        else:
            k.append(e.flat[e.objects[0].x][e.objects[0].y - 1])
        return k

class Agent:
    def __init__(self):
        self.n = None
        self.m = None
        self.i = 0
        self.j = 0

    def doAI(self,k):
        if k[4] != command.none and self.n == None:
            return command.up
        if k[4] == command.none:
            self.n = 1
        if self.n != None and k[3] != command.none:
            self.n += 1
            return command.down
        if k[1] != command.none and self.m == None:
            return command.right
        if k[1] == command.none:
            self.m = 1
        if self.m != None and k[2] != command.none:
            self.m += 1
            return command.left

    def doAII(self,k):
        if k[0] == command.dirt:
            return command.clean
        if self.j < self.n and self.i % 2 == 0:
            self.j += 1
            return command.up
        if self.j < self.n and self.i % 2 != 0:
            self.j += 1
            return command.down
        if self.j == self.n:
            self.j = 0
            self.i += 1
            return command.right

def do(event, k):
    if event.type != pg.KEYDOWN:
        return 0
    if event.key == pg.K_w:
        return command.up
    if event.key == pg.K_s:
        return command.down
    if event.key == pg.K_a:
        return command.left
    if event.key == pg.K_d:
        return command.right
    if event.key == pg.K_SPACE:
        return command.clean


if __name__ == "__main__":

    e = Environment()
    scale = 150 / (max(e.m, e.n))
    # creating a pygame window
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()

    # creating a surface for flat render
    view_flat = vx, vy = int(screen.get_width() * 2 / 3), int(screen.get_height() * 2 / 3)
    sf = pg.Surface((vx, vy))
    sf.fill((110, 110, 110))
    # main cycle
    a = Agent()
    while True:
        # surfaces cleaning
        screen.fill((140, 140, 140))
        sf.fill((110, 110, 110))

        # checking for keyboard, window, mouse inputs or events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        if a.n == e.n and a.m == e.m:
            f = a.doAII(e.type())
        else:
            f = a.doAI(e.type())

        e.event(f)

        # checking for scale changes
        if keys[pg.K_p]:
            scale += 1
        if keys[pg.K_o]:
            scale -= 1

        # drawing flat
        for i, line in enumerate(e.flat):
            for j, quad in enumerate(line):
                if quad == command.cl:
                    pg.draw.polygon(sf, (255, 255, 255), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)
                else:
                    pg.draw.polygon(sf, (160, 160, 160), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)

        e.check()
        pg.draw.circle(sf, (220, 0, 0), [(e.objects[0].x + 0.5) * scale * 5, (e.objects[0].y + 0.5) * scale * 5],
                       scale * 2.5)

        pg.draw.polygon(screen, (80, 80, 80), [[0, 0], [vx, 0], [vx, vy], [0, vy]], 1)

        screen.blit(sf, (0, 0))
        pg.display.flip()
        clock.tick(3)
