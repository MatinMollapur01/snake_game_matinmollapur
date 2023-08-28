import pygame
import random

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20

# Directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        delta_x, delta_y = self.direction
        new_head = ((head_x + delta_x) % (SCREEN_WIDTH // BLOCK_SIZE),
                    (head_y + delta_y) % (SCREEN_HEIGHT // BLOCK_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def collides_with_itself(self):
        return self.body[0] in self.body[1:]

    def get_head_position(self):
        return self.body[0]

class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1),
                         random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1))

    def respawn(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1),
                         random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1))

def draw_snake(screen, snake):
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), border_radius=5)

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (food.position[0] * BLOCK_SIZE, food.position[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                if event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                if event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN

        snake.move()
        if snake.get_head_position() == food.position:
            snake.grow()
            food.respawn()

        if snake.collides_with_itself():
            snake = Snake()  # reset the game

        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        pygame.display.flip()

        clock.tick(10)  # 10 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
