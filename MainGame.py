import pygame, sys, random

pygame.init()
pygame.mixer.init() 

# Load and play background music
pygame.mixer.music.load('Roku Snake OST - Main Theme.mp3')  
pygame.mixer.music.play(-1) 

WIDTH, HEIGHT, BLOCK = 720, 480, 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Eater')
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 20)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake & Food
snake = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
food = [random.randrange(1, WIDTH // BLOCK) * BLOCK, random.randrange(1, HEIGHT // BLOCK) * BLOCK]
score = 0

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

def show_score():
    text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = pygame.font.SysFont('times new roman', 72).render('YOU DIED', True, RED)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            if event.key in [pygame.K_w, pygame.K_UP] and direction != 'DOWN': direction = 'UP'
            if event.key in [pygame.K_s, pygame.K_DOWN] and direction != 'UP': direction = 'DOWN'
            if event.key in [pygame.K_a, pygame.K_LEFT] and direction != 'RIGHT': direction = 'LEFT'
            if event.key in [pygame.K_d, pygame.K_RIGHT] and direction != 'LEFT': direction = 'RIGHT'

    # Move Snake
    head = snake[0][:]
    if direction == 'UP': head[1] -= BLOCK
    if direction == 'DOWN': head[1] += BLOCK
    if direction == 'LEFT': head[0] -= BLOCK
    if direction == 'RIGHT': head[0] += BLOCK
    snake.insert(0, head)

    # Eat food
    if head == food:
        score += 1
        food = [random.randrange(1, WIDTH // BLOCK) * BLOCK, random.randrange(1, HEIGHT // BLOCK) * BLOCK]
    else:
        snake.pop()

    # Check collisions
    if (head in snake[1:] or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT):
        game_over()

    # Draw
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    show_score()
    pygame.display.update()
    clock.tick(15)
