import streamlit as st
import pygame
import random
import sys

st.set_page_config(page_title="Nokia Snake Game", layout="centered")

st.title("🐍 Nokia Style Snake Game")
st.write("Click **Start Game** to play. Use Arrow Keys!")

# Button to start the game
start = st.button("Start Game")

if start:

    pygame.init()

    # Game constants
    WIDTH, HEIGHT = 400, 400
    BLOCK = 20
    SPEED = 10

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 25)

    # Colors (Retro Nokia feel)
    BLACK = (10, 10, 10)
    GREEN = (0, 255, 70)
    FOOD_COLOR = (255, 60, 60)

    def draw_snake(snake):
        for block in snake:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK, BLOCK))

    def message(text):
        msg = font.render(text, True, GREEN)
        screen.blit(msg, [WIDTH / 6, HEIGHT / 3])

    def game_loop():

        x = WIDTH // 2
        y = HEIGHT // 2

        dx = 0
        dy = 0

        snake = []
        snake_length = 1

        food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
        food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

        score = 0
        game_over = False
        game_close = False

        while not game_over:

            while game_close:
                screen.fill(BLACK)
                message(f"Game Over! Score: {score} | Press Q-Quit or C-Play Again")
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -BLOCK
                        dy = 0
                    elif event.key == pygame.K_RIGHT:
                        dx = BLOCK
                        dy = 0
                    elif event.key == pygame.K_UP:
                        dy = -BLOCK
                        dx = 0
                    elif event.key == pygame.K_DOWN:
                        dy = BLOCK
                        dx = 0

            # Wall collision
            if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
                game_close = True

            x += dx
            y += dy

            screen.fill(BLACK)

            pygame.draw.rect(screen, FOOD_COLOR, (food_x, food_y, BLOCK, BLOCK))

            snake_head = [x, y]
            snake.append(snake_head)

            if len(snake) > snake_length:
                del snake[0]

            # Self collision
            for block in snake[:-1]:
                if block == snake_head:
                    game_close = True

            draw_snake(snake)

            score_text = font.render(f"Score: {score}", True, GREEN)
            screen.blit(score_text, [10, 10])

            pygame.display.update()

            # Eating food
            if x == food_x and y == food_y:
                food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
                food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)
                snake_length += 1
                score += 10

            clock.tick(SPEED)

        pygame.quit()
        sys.exit()

    game_loop()
