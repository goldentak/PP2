import pygame as pg
from sys import exit

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

W, H = 800, 600

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Paint!")
clock = pg.time.Clock()
font_path = "media/Minecraft.ttf" 
font = pg.font.Font(font_path, 24)

shapes = []
brushSize = 2
color = BLACK
tool = "circle"

guide = True
drawing = False
start_pos = (0, 0)
current_pos = (0, 0)

def draw_ui():
    info = f"Tool: {tool.upper()} | Color: {color}"
    help = """R-red  G-green  B-blue  C-circle  T-rect  E-eraser  ESC-guide off"""
    text = font.render(info, True, BLACK)
    text2 = font.render(help, True, BLACK)
    screen.blit(text, (10, 10))
    if(guide):
        screen.blit(text2, (10, 30))

def draw_shape(shape):
    if shape['type'] == 'rect':
        x1, y1 = shape['start']
        x2, y2 = shape['end']
        x, y = min(x1, x2), min(y1, y2)
        w, h = abs(x2 - x1), abs(y2 - y1)
        pg.draw.rect(screen, shape['color'], (x, y, w, h), 0)
    elif shape['type'] == 'circle':
        x1, y1 = shape['start']
        x2, y2 = shape['end']
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        pg.draw.circle(screen, shape['color'], shape['start'], radius)
    elif shape['type'] == 'eraser':
        x1, y1 = shape['start']
        x2, y2 = shape['end']
        x, y = min(x1, x2), min(y1, y2)
        w, h = abs(x2 - x1), abs(y2 - y1)
        pg.draw.rect(screen, WHITE, (x, y, w, h), 0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                color = RED
            elif event.key == pg.K_g:
                color = GREEN
            elif event.key == pg.K_b:
                color = BLUE
            elif event.key == pg.K_c:
                tool = "circle"
            elif event.key == pg.K_t:
                tool = "rect"
            elif event.key == pg.K_e:
                tool = "eraser"
            elif event.key == pg.K_ESCAPE:
                guide = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = pg.mouse.get_pos()

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if drawing:
                end_pos = pg.mouse.get_pos()
                draw_color = WHITE if tool == "eraser" else color
                shapes.append({
                    'type': tool,
                    'start': start_pos,
                    'end': end_pos,
                    'color': draw_color
                })
                drawing = False

        elif event.type == pg.MOUSEMOTION:
            if drawing:
                current_pos = pg.mouse.get_pos()

    screen.fill(WHITE)

    for shape in shapes:
        draw_shape(shape)

    if drawing:
        temp_shape = {
            'type': tool,
            'start': start_pos,
            'end': current_pos,
            'color': WHITE if tool == "eraser" else color
        }
        draw_shape(temp_shape)

    draw_ui()
    pg.display.flip()
    clock.tick(60)

