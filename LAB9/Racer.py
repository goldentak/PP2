import pygame as pg
import sys
import random, time

#Creating colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

pg.init()
 
#Setting up FPS
FPS = 60
clock = pg.time.Clock()
 
#Setting up resolutions
W = 640
H = 800
speed = 5
inc = True
 
#Create a white screen 
surface = pg.display.set_mode((W, H))
surface.fill(WHITE)
pg.display.set_caption("Racer!")

background_music = pg.mixer.music.load('media/background.wav')
crash_sound = pg.mixer.Sound('media/stuk.mp3')
#texts
font = pg.font.Font('media/Minecraft.ttf',60)
int_font = pg.font.Font('media/Minecraft.ttf', 30)
win = font.render("YOU WIN!",True,BLACK)
gameOver = font.render("Game Over", True, BLACK)

pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)

count=0 #coin


bg = pg.image.load("media/road.jpg")
bg = pg.transform.scale(bg, (W, H))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("media/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pg.key.get_pressed()
         
        if self.rect.left > 50:
              if pressed_keys[pg.K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < W-50:        
              if pressed_keys[pg.K_RIGHT]:
                  self.rect.move_ip(10, 0)
 
class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("media/car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,W-100), 0)    
 
      def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.top > H):
            self.rect.top = 0
            self.rect.center = (random.randint(100,W-100), 0)

class Coin(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("media/coin.png")
        self.image=pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60,W-60), 0)    
        self.weight = random.randint(1, 3)
 
      def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.top > H):
            self.rect.top = 0
            self.rect.center = (random.randint(60,W-60), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1=Coin()
enemies = pg.sprite.Group()
enemies.add(E1)

allSprites = pg.sprite.Group()
allSprites.add(P1)
allSprites.add(E1)
allSprites.add(C1)

coins=pg.sprite.Group()
coins.add(C1)


#Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
 
 
    surface.blit(bg, (0,0))
 
    #Moves and Re-draws all Sprites
    for entity in allSprites:
        surface.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollide(P1, enemies, dokill=False):
          pg.mixer.Sound('media/stukk.mp3').play()
          time.sleep(1)
          surface.fill(RED)

          pg.draw.rect(surface,BLACK,(W//2 -215,H//2-45-40,450,150),0,20)
          pg.draw.rect(surface,WHITE,(W//2 -190,H//2-20-40,400,100),0,10)

          pg.mixer.Sound('media/lose.mp3').play()
          pg.mixer.music.stop()
          lose_text = font.render("YOU LOSE!", True, (0, 0, 0))
          surface.blit(lose_text, (W//2 -170, H//2-40))
          pg.display.update()

          for entity in allSprites:
                entity.kill() 
          time.sleep(3)
          pg.quit()
          sys.exit()  

    #counting coins
    collect_coin= pg.sprite.spritecollide(P1, coins, dokill=True)
    if collect_coin:
        pg.mixer.Sound('media/coinsound.mp3').play()
        count += collect_coin[0].weight  # Добавляем вес монеты к счету
        new_coin = Coin()

        allSprites.add(new_coin)
        coins.add(new_coin)

        speed *= 1.05

    #win
    if count >= 100:  #win = player reaches 100 coins
        pg.mixer.Sound('media/win.mp3').play()
        surface.fill(GREEN)
        pg.draw.rect(surface,BLACK,(W//2 -215,H//2-45-40,450,150),0,20)
        pg.draw.rect(surface,WHITE,(W//2 -190,H//2-20-40,400,100),0,10)
        pg.mixer.music.stop()
        
        lose_text = font.render("YOU WIN!", True, (0, 0, 0))
        surface.blit(lose_text, (W//2 -170, H//2-40))


    pg.draw.rect(surface, BLACK, (W-160,10,120,70),0,20,20,20,20)
    pg.draw.rect(surface, WHITE, (W-150,20,100,50),0,10,10,10,10)

    score = int_font.render(str(count), True, BLACK)
    surface.blit(score, (W-120, 32))


    pg.display.update()
    clock.tick(FPS)
