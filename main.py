import pygame 
import math 
import random
import sys


pygame.init()

FPS = 60
cells = []

CELL_COUNT = 2000

WIDTH, HEIGHT = 1250, 720
MAP_SIZE = 2000

BACKGROUND_COLOR = (255, 255, 255)
OUTLINE_COLOR = (0, 0, 0)
OUTLINE_THICKNESS = 1

respawn_cells = True

MOVE_VEL = 40

COLORS = [
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (128, 0, 255),
    (255, 0, 255),
    (255, 0, 128),

]




WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Agario")



class Cell():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.status = random.randint(1, 8)
        self.radius = radius
        self.color = color
    def wander(self):
        pass
    def collide_check(self, player):
        global cells
        for cell in cells: 
            if math.sqrt(((player.x - (WIDTH/2) + cell.x) ** 2 + (player.y - (HEIGHT/2) + cell.y) ** 2 )) <= cell.radius + player.radius and cell.radius <= player.radius:
                player.radius += 0.25
                cells.remove(cell)
                if respawn_cells:
                    new_cell = Cell(random.randint(-MAP_SIZE, MAP_SIZE), random.randint(-MAP_SIZE, MAP_SIZE), 5, COLORS[random.randint(0, len(COLORS)-1)])
                    cells.append(new_cell)

    def draw_cell(self, surface, x, y):
        pygame.draw.circle(surface, self.color, (x, y), int(self.radius))
        




        



def main(window):
    global WIDTH, HEIGHT
    clock = pygame.time.Clock()
    run=True
    
    p1 = Cell(random.randint(100, 800), random.randint(100, 800), 20, COLORS[random.randint(0, len(COLORS)-1)])

    window.fill(BACKGROUND_COLOR)
    
    for i in range(CELL_COUNT):
        new_cell = Cell(random.randint(-MAP_SIZE, MAP_SIZE), random.randint(-MAP_SIZE, MAP_SIZE), 5, COLORS[random.randint(0, len(COLORS)-1)])
        cells.append(new_cell)
    
    
    

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
        
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        else: 
            mouse_x = WIDTH / 2
            mouse_y = HEIGHT / 2

        p1.collide_check(p1)
        p1.x += round(-((mouse_x - (WIDTH / 2)) / p1.radius / 2))
        p1.y += round(-((mouse_y - (HEIGHT / 2)) / p1.radius / 2))



                

            

        for cell in cells:
            cell.draw_cell(window, cell.x+p1.x, cell.y+p1.y)

        p1.draw_cell(window, WIDTH/2, HEIGHT /2)
        
        WIDTH, HEIGHT = pygame.display.get_surface().get_size()
        pygame.display.update()
        window.fill(BACKGROUND_COLOR)
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)