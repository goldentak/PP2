import pygame as pg
import datetime as dt
import time
from sys import exit

pg.mixer.init()
pg.init()

W = 500
H = 500

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Music")

imgs = [
    pg.transform.scale(pg.image.load("mus/505cover.jpg"), (W, H)),
    pg.transform.scale(pg.image.load("mus/Tame_Impala_-_Currents.png"), (W, H)),
    pg.transform.scale(pg.image.load("mus/wallows.jpg"), (W, H)),
    pg.transform.scale(pg.image.load("mus/marcdemarco.jpg"), (W, H))
]
musics = [
    "mus/Arctic Monkeys - 505.mp3",
    "mus/Tame Impala - Let It Happen.mp3",
    "mus/wallows.mp3",
    "mus/Marc.mp3"
]

playnum = 0
isplaying = False
lens = len(musics)

def play_music():
    global isplaying
    pg.mixer.music.load(musics[playnum])
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)
    isplaying = True

def stop():
    global isplaying
    pg.mixer.stop()
    isplaying = False

def playnext():
    global playnum
    playnum = (playnum + 1) % lens
    play_music()

def playprev():
    global playnum
    if playnum - 1 < 0:
        playnum = 2
    else:
        playnum = (playnum - 1) % lens
    
    play_music()

status = True
while status:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            status = False
    
    screen.fill((15,15,15))
    screen.blit(imgs[playnum], (0,0))

    key = pg.key.get_pressed()

    if(key[pg.K_LEFT]):
        playprev()
        time.sleep(1)
    elif key[pg.K_RIGHT]:
       playnext()
       time.sleep(1)
    elif key[pg.K_SPACE]:
        if isplaying:
            pg.mixer.music.pause()
            isplaying = False
        else:
            pg.mixer.music.unpause()
            isplaying = True
        time.sleep(1)
    elif key[pg.K_s]:
        stop()
    pg.display.update()
   
pg.quit()