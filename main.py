# pygame and sys libraries importing
import pygame as pg
import sys
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

class Environment:
    def __init__(self,x,y,flat):
        m, n = (random.randint(3,20), random.randint(3,20))
        flat = list()
        for i in range(m):
            k = []
            for j in range(n):
                if random.random() < 0.3:
                    k.append(command.dirt)
                else:
                    k.append(command.cl)
        flat.append(k)
        y, x = random.randint(0,n-1),random.randint(0,m-1)
    
    def type(self,x,y):
        return flat[x][y]

def do(event):
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
    
    m, n = (random.randint(3,20), random.randint(3,20))
    flat = list()
    for i in range(m):
        k = []
        for j in range(n):
            if random.random() < 0.3:
                k.append(command.dirt)
            else:
                k.append(command.cl)
        flat.append(k)
    scale = 150 / (max(m,n))
    # creating a pygame window
    screen = pg.display.set_mode((1280, 720))

    # cleaner coords import
    y, x = random.randint(0,n-1),random.randint(0,m-1)

    # creating a surface for flat render
    view_flat = vx, vy = int(screen.get_width() * 2/3), int(screen.get_height() * 2/3)
    sf = pg.Surface((vx, vy))
    sf.fill((110, 110, 110))

    # main cycle
    while True:
        # surfaces cleaning
        screen.fill((140, 140, 140))
        sf.fill((110, 110, 110))
        
        # checking for keyboard, window, mouse inputs or events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            f = do(event)
            
            if f == command.up:
                y -= 1
            if f == command.down:
                y += 1
            if f == command.left:
                x -= 1
            if f == command.right:
                x += 1
            if f == command.clean:
                flat[x][y] = command.cl
                
        # checking for scale changes
        if keys[pg.K_p]:
            scale += 0.1
        if keys[pg.K_o]:
            scale -= 0.1

        # drawing flat
        for i, line in enumerate(flat):
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

        # drawing robot
        pg.draw.circle(sf, (220, 0, 0), [(x + 0.5) * scale * 5, (y + 0.5) * scale * 5], scale * 2.5)

        pg.draw.polygon(screen, (80, 80, 80), [[0, 0], [vx, 0], [vx, vy], [0, vy]], 1)

        screen.blit(sf, (0, 0))

        pg.display.flip()
