import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 32)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
gravity = 0.5
bird_velocity = 0
jump_strength = -10

# Pipe settings
pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

# Game state
score = 0
game_over = False

def create_pipe():
    height = random.randint(100, 400)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_rect = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top_rect, bottom_rect

def reset_game():
    global bird_y, bird_velocity, pipes, score, game_over
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes = []
    score = 0
    game_over = False

# Add first pipe
pipes.append(create_pipe())

# Game loop
while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity

        # Add pipes
        if pipes[-1][0].x < WIDTH - 200:
            pipes.append(create_pipe())

        # Move pipes and detect collision
        for pipe in pipes:
            pipe[0].x -= pipe_velocity
            pipe[1].x -= pipe_velocity

        # Remove off-screen pipes
        pipes = [p for p in pipes if p[0].x + pipe_width > 0]

        # Check collisions
        for top_pipe, bottom_pipe in pipes:
            if pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2).colliderect(top_pipe) or \
               pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2).colliderect(bottom_pipe):
                game_over = True

        # Check if bird hits ground or ceiling
        if bird_y > HEIGHT or bird_y < 0:
            game_over = True

        # Score
        for pipe in pipes:
            if pipe[0].x + pipe_width < bird_x and not hasattr(pipe, 'passed'):
                score += 1
                pipe.passed = True

    # Draw bird
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, GREEN, pipe[1])

    # Display score
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:
        msg = FONT.render("Game Over! Press R to restart", True, WHITE)
        screen.blit(msg, (20, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
