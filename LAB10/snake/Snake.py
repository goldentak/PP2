import pygame as pg
import random
import sys
import time  # For handling the timer for food expiration

#Psycopg changes----
import psycopg2

conn = psycopg2.connect(database = "snake", 
                        user = "postgres",
                        host= 'localhost',
                        password = "3245",
                        port = 5433)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE IF NOT EXISTS score_table
            (id SERIAL PRIMARY KEY,
            name VARCHAR(25) NOT NULL,
            score INT NOT NULL)""")
#-----

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
FPS = 10  # initial speed

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake!")
clock = pg.time.Clock()

# Font
font_path = "media/Minecraft.ttf"
font = pg.font.Font(font_path, 24)

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

        cur.execute("UPDATE score_table SET score = %s WHERE name = %s", (len(self.body), player_name))


    def change_direction(self, dx, dy):
        # Lock to turn back
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx, self.dy = dx, dy

    def check_collision(self):
        head = self.body[0]
        # Checking for borders
        if (head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
                head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE):
            return True
        # Self-collision check
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
        self.weight = random.randint(1, 3)  # Random food weight (points)
        self.creation_time = time.time()  # Time when food was created
        self.lifetime = 10  # Food lifetime in seconds before disappearing

    def generate_position(self, snake_body, walls):
        while True:
            pos = (random.randint(0, WIDTH // CELL_SIZE - 1),
                   random.randint(0, HEIGHT // CELL_SIZE - 1))
            if pos not in snake_body and pos not in walls:
                return pos

    def is_expired(self):
        # Check if food has expired based on its lifetime
        return time.time() - self.creation_time > self.lifetime

    def draw(self):
        if not self.is_expired():  # Only draw food if it hasn't expired
            pg.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        else:
            return None  # Return None if food is expired


class Game:
    def __init__(self):
        self.snake = Snake()
        self.walls = []
        self.food = Food(self.snake.body, self.walls)
        self.score = 0
        self.level = 1
        self.speed = FPS
        self.is_paused = False  # Flag for pause state

    def update(self):
        if self.is_paused:
            return  # Skip update if the game is paused

        self.snake.move()
        if self.snake.check_collision():
            self.game_over()

        # Is food eaten?
        if self.snake.body[0] == self.food.position and not self.food.is_expired():
            self.snake.grow()
            self.score += self.food.weight  # Add food weight to score
            self.food = Food(self.snake.body, self.walls)  # Generate new food

            # For every 4 points, level up
            if self.score % 4 == 0:
                self.level += 1
                self.speed += 2
                self.change_level()

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

        #postgres score board
        ys = 10
        cur.execute("SELECT name, score FROM score_table ORDER BY score DESC LIMIT 5")
        rows = cur.fetchall()
        if len(rows):
            for i, row in enumerate(rows):
                name, score = row
                text = f"{i+1}. {name} - {score}"
                if(player_name == name):
                    score_board = font.render(text, True, (0, 200, 0))
                else:
                    score_board = font.render(text, True, (0, 0, 0))
                screen.blit(score_board, (400, ys))
                ys += 30

    def draw(self):
        screen.fill(WHITE)
        self.draw_grid()
        self.snake.draw()
        if self.food.draw() is not None:  # Only draw the food if it's still valid
            self.food.draw()
        self.draw_ui()
        pg.display.flip()

    def game_over(self):
        print(f"Game over! Score: {self.score}")
        pg.quit()
        sys.exit()

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Game Paused")
        else:
            print("Game Resumed")

#Name entering before game starts
player_name = ""
input_act = True

while input_act:
    screen.fill((0, 0, 0))

    prompt = font.render("Enter your name then press Enter:", True, (255, 255, 255))
    screen.blit(prompt, (50, 200))

    name_text = font.render(player_name, True, (0, 255, 0))
    screen.blit(name_text, (50, 260))

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN and player_name.strip() != "":
                input_act = False
            elif event.key == pg.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                if len(player_name) < 15:
                    player_name += event.unicode
    clock.tick(30)

cur.execute("INSERT INTO score_table(name, score) VALUES(%s, %s)", (player_name, 0))

# Main loop
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
                elif event.key == pg.K_p:  # Press "P" to pause/resume the game
                    game.pause()
        # Make the changes to the database persistent if game is paused
        if game.is_paused:
            cur.execute("UPDATE score_table1 SET score = %s, level = %s WHERE name = %s", 
                        (game.score, game.level, player_name))
            conn.commit()

        game.update()
        game.draw()


if __name__ == "__main__":
    main()


# Close cursor and communication with the database
cur.close()
conn.close()