import pygame as pg
import random
import sys

#consts
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
FPS = 10  #first speed

#Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake!")
clock = pg.time.Clock()

#font
font_path = "media/Minecraft.ttf" 
font = pg.font.Font(font_path, 36)

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.dx, self.dy = 1, 0

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.dx, head[1] + self.dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, dx, dy):
        #Lock to turn back
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx, self.dy = dx, dy

    def check_collision(self):
        head = self.body[0]
        #Checking for borders
        if (head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
                head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE):
            return True
        #Self-collision check
        if head in self.body[1:]:
            return True
        return False

    def draw(self):
        for i, segment in enumerate(self.body):
            color = DARK_GREEN if i == 0 else GREEN
            pg.draw.rect(screen, color,
                             (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Food:
    def __init__(self, snake_body, walls):
        self.position = self.generate_position(snake_body, walls)

    def generate_position(self, snake_body, walls):
        while True:
            pos = (random.randint(0, WIDTH // CELL_SIZE - 1),
                   random.randint(0, HEIGHT // CELL_SIZE - 1))
            if pos not in snake_body and pos not in walls:
                return pos

    def draw(self):
        pg.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Game:
    def __init__(self):
        self.snake = Snake()
        self.walls = []
        self.food = Food(self.snake.body, self.walls)
        self.score = 0
        self.level = 1
        self.speed = FPS

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.game_over()

        #Is food eaten?
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food = Food(self.snake.body, self.walls)
            self.score += 1

            # For every 4 point - new lvl
            if self.score % 4 == 0:
                self.level += 1
                self.speed += 2

    def draw_grid(self):
        for x in range(0, WIDTH, CELL_SIZE):
            pg.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pg.draw.line(screen, BLACK, (0, y), (WIDTH, y))

    def draw_ui(self):
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        level_text = font.render(f"Level: {self.level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

    def draw(self):
        screen.fill(WHITE)
        self.draw_grid()
        self.snake.draw()
        self.food.draw()
        self.draw_ui()
        pg.display.flip()

    def game_over(self):
        print("Game over! Счет:", self.score)
        pg.quit()
        sys.exit()


#main loop
def main():
    game = Game()

    while True:
        clock.tick(game.speed)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    game.snake.change_direction(0, -1)
                elif event.key == pg.K_DOWN:
                    game.snake.change_direction(0, 1)
                elif event.key == pg.K_LEFT:
                    game.snake.change_direction(-1, 0)
                elif event.key == pg.K_RIGHT:
                    game.snake.change_direction(1, 0)

        game.update()
        game.draw()


if __name__ == "__main__":
    main()
