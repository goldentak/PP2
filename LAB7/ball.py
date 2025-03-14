import pygame as pg
from sys import exit

W = 800
H = 600

x = W /2 
y = H / 2
R = 25
speed = 20

RED = (255, 0, 0)
WHITE = (255, 255, 255)
clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))

def drawcircle(x = 0, y = 0):
    ball = pg.draw.circle(screen, RED, (x,y), R)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    key = pg.key.get_pressed()
    if(key[pg.K_LEFT]):
        x -= speed
    if(key[pg.K_RIGHT]):
        x += speed 
    if(key[pg.K_UP]):
        y -= speed
    if(key[pg.K_DOWN]):
        y += speed
    
    if y < R:
        y = R
    if y > H - R:
        y = H - R
    if x < R:
        x = R
    if x > W - R:
        x = W - R


    screen.fill(WHITE)

    


    drawcircle(x, y)



    
    pg.display.update()
    clock.tick(60)


pg.quit()