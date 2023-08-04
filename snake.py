import pygame, sys, random

pygame.init()

SW, SH = 800, 800
BLOCK_SIZE = 50

FONT = pygame.font.Font("retro.ttf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        # Snake will move to the right when the game stars
        self.xdir = 1
        self.ydir = 0

        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False


def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


drawGrid()

snake = Snake()

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the snake; head first and then body
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    pygame.display.update()
    clock.tick(10)
