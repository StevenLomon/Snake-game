import pygame, sys, random

pygame.init()

SW, SH = 800, 800
BLOCK_SIZE = 50

FONT = pygame.font.Font("retro.ttf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()


class Apple:
    def __init__(self):
        # Scaled in order to fit the grid
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    # Will draw an apple on the screen
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)


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
        # Death condition
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
        if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
            self.dead = True

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
apple = Apple()

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # User input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.xdir, snake.ydir = 1, 0
            if event.key == pygame.K_LEFT:
                snake.xdir, snake.ydir = -1, 0
            if event.key == pygame.K_DOWN:
                snake.xdir, snake.ydir = 0, 1
            if event.key == pygame.K_UP:
                snake.xdir, snake.ydir = 0, -1

    # "Reset" the screen in order to remove old states of the snake
    screen.fill("black")
    drawGrid()

    # Draw the snake; head first and then body
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    # Add movement to the snake and spawn an apple
    snake.update()
    apple.update()

    # Eating logic
    if snake.head.x == apple.x and snake.head.y == apple.y:
        # Create a new square at the position of the head for the snake body
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        # Spawn a new apple
        apple = Apple()

    # If we die
    if snake.dead:
        # Create a new snake
        snake.x, snake.y = BLOCK_SIZE, BLOCK_SIZE
        # Snake will move to the right when the game stars
        snake.xdir = 1
        snake.ydir = 0

        snake.head = pygame.Rect(snake.x, snake.y, BLOCK_SIZE, BLOCK_SIZE)
        snake.body = [
            pygame.Rect(snake.x - BLOCK_SIZE, snake.y, BLOCK_SIZE, BLOCK_SIZE)
        ]
        snake.dead = False

    pygame.display.update()
    clock.tick(10)
