import pygame as pg
import datetime
from datetime import datetime as dt
from sys import exit

pg.init()

W = 800
H = 600

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
bg = pg.image.load("img/clock.png")

minHand = pg.image.load("img/min_hand.png")
secHand = pg.image.load("img/sec_hand.png")

def rotate(surf, img, times):
    rotImg = pg.transform.rotate(img, -(times % 60) * 6 - 45)
    newImg = rotImg.get_rect(center = img.get_rect(center = (400, 300)).center)
    print(newImg)
    surf.blit(rotImg, newImg)


pg.display.set_caption("Clock!")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    curtime = dt.now()
    min = curtime.minute
    sec = curtime.second

    screen.fill("BLACK")
    screen.blit(bg, (0,0))
     
    rotate(screen, secHand, sec)
    rotate(screen, minHand, min)


    pg.display.update()
    clock.tick(60)