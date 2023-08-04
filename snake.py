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

    # For movement
    def update(self):
        # Move every square in our snake body one square forward
        # Temporarily add the head to the body to then remove it
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)


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

    # "Reset" the screen in order to remove old states of the snake
    screen.fill("black")
    drawGrid()

    # Draw the snake; head first and then body, and then add movement with the update method
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    snake.update()

    pygame.display.update()
    clock.tick(10)
