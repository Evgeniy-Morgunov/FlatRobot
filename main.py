# pygame and sys libraries importing
import pygame as pg

import sys

pg.init()

# import an integers from one of flat.txt lines
def parceline(f):
    return list(map(int, f.readline()[:-1].split()))


if __name__ == "__main__":
    # flat render scale
    scale = 20.0

    # importing flat.txt for flatmap
    filename = "flat.txt" # sys.argv[1]
    f = open(filename)
    # width and height of imported flat
    m, n = parceline(f)
    flat = list()
    for i in range(m):
        flat.append(parceline(f))
    print(*flat)

    # creating a pygame window
    screen = pg.display.set_mode((1280, 720))

    # cleaner cords import
    y, x = parceline(f)

    # creating a surface for flat render
    view_flat = vx, vy = int(screen.get_width() * 2/3), int(screen.get_height() * 2/3)
    sf = pg.Surface((vx, vy))
    sf.fill((110, 110, 110))

    w = 1280 * 2 // 3
    h = 720 * 2 // 3

    score = 0

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
            if event.type == pg.KEYDOWN:

              # robot's controls
              if event.key == pg.K_w:
                  if y > 0 and flat[x][y-1] != 2:
                     y -= 1
              if event.key == pg.K_s:
                  if y < n-1 and flat[x][y+1] != 2:
                     y += 1
              if event.key == pg.K_a:
                  if x > 0 and flat[x-1][y] != 2:
                     x -= 1
              if event.key == pg.K_d:
                  if x < m-1 and flat[x+1][y] != 2:
                     x += 1
              if event.key == pg.K_SPACE:
                  if flat[x][y] == 1:
                    flat[x][y] = 0
                    score += 1
            # Click LMB for create dirt and click RMB for create obstacles
            if event.type == pg.MOUSEBUTTONDOWN:
                posx = int(event.pos[0] // 100)
                posy = int(event.pos[1] // 100)
                if event.button == 1:
                    if posx <= n and posy <= m and flat[posx][posy] != 2:
                        flat[posx][posy] = 1
                if event.button == 3:
                    if posx != x or posy != y:
                        flat[posx][posy] = 2


        # checking for scale changes
        if keys[pg.K_p]:
            scale += 0.1
        if keys[pg.K_o]:
            scale -= 0.1

        # drawing flat
        for i, line in enumerate(flat):
            for j, quad in enumerate(line):
                if not quad:
                    pg.draw.polygon(sf, (255, 255, 255), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)
                elif quad == 1:
                    pg.draw.polygon(sf, (160, 160, 160), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)
                else:
                    pg.draw.polygon(sf, (255, 99, 71), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)

        # drawing robot
        pg.draw.circle(sf, (220, 0, 0), [(x + 0.5) * scale * 5, (y + 0.5) * scale * 5], scale * 2.5)
        
        # Counter removed dirt
        f = pg.font.Font(None, 72)
        text = f.render(str(score) + " грязи убрано",True,[255,0,0])

        pg.draw.polygon(screen, (80, 80, 80), [[0, 0], [vx, 0], [vx, vy], [0, vy]], 1)

        screen.blit(sf, (0, 0))
        screen.blit(text, (n * 100 + 80, m * 100 - 100))

        pg.display.flip()
