import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 7
PADDLE_SPEED = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

font = pygame.font.Font(None, 74)

# Load sound effects
hit_sound = pygame.mixer.Sound("audio/hit.mp3")
score_sound = pygame.mixer.Sound("audio/score.mp3")

def home_screen():
    screen.fill(BLACK)
    title = font.render("Pong Game", True, WHITE)
    option1 = font.render("1. Play against CPU", True, WHITE)
    option2 = font.render("2. Play against Human", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, HEIGHT // 2))
    screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, HEIGHT // 2 + 100))
    pygame.display.flip()

def pause_game():
    paused = True
    line1 = font.render("Paused. Press ESC to Resume", True, WHITE)
    line2 = font.render("Press Q to Quit to Home", True, WHITE)
    
    screen.fill(BLACK)  # Clear the screen before drawing the pause text
    screen.blit(line1, (WIDTH // 2 - line1.get_width() // 2, HEIGHT // 2 - line1.get_height()))
    screen.blit(line2, (WIDTH // 2 - line2.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_q:
                    return "home"

def game_over(winner):
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! {winner} Wins!", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

def main(game_mode):
    paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

    score1, score2 = 0, 0

    countdown = 0
    ball_visible = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main(game_mode)
                if event.key == pygame.K_ESCAPE:
                    if pause_game() == "home":
                        return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s]:
            paddle1.y += PADDLE_SPEED

        if game_mode == "human":
            if keys[pygame.K_UP]:
                paddle2.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN]:
                paddle2.y += PADDLE_SPEED
        else:
            if ball.centery < paddle2.centery:
                paddle2.y -= PADDLE_SPEED - 3.8 
            if ball.centery > paddle2.centery:
                paddle2.y += PADDLE_SPEED - 3.8 

        paddle1.y = max(0, min(paddle1.y, HEIGHT - PADDLE_HEIGHT))
        paddle2.y = max(0, min(paddle2.y, HEIGHT - PADDLE_HEIGHT))

        if countdown <= 0:
            ball.x += ball_dx
            ball.y += ball_dy
            ball_visible = True

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        if ball.colliderect(paddle1):
            ball_dx *= -1
            ball_dy = random.randint(-BALL_SPEED, BALL_SPEED)
            hit_sound.play()  # Play hit sound

        if ball.colliderect(paddle2):
            ball_dx *= -1
            ball_dy = random.randint(-BALL_SPEED, BALL_SPEED)
            hit_sound.play()  # Play hit sound

        if ball.left <= 0:
            score2 += 1
            score_sound.play()  # Play score sound
            if score2 == 10:  # Example winning score
                game_over("Player 2" if game_mode == "human" else "CPU")
                main(game_mode)
            countdown = random.uniform(3, 5) * 60  # Convert seconds to frames
            ball_visible = False
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -BALL_SPEED
            ball_dy = random.randint(-BALL_SPEED, BALL_SPEED)

        if ball.right >= WIDTH:
            score1 += 1
            score_sound.play()  # Play score sound
            if score1 == 10:  # Example winning score
                game_over("Player 1")
                main(game_mode)
            countdown = random.uniform(3, 5) * 60  # Convert seconds to frames
            ball_visible = False
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = BALL_SPEED
            ball_dy = random.randint(-BALL_SPEED, BALL_SPEED)

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        if ball_visible:
            pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        text1 = font.render(str(score1), True, WHITE)
        screen.blit(text1, (WIDTH // 4, 20))
        text2 = font.render(str(score2), True, WHITE)
        screen.blit(text2, (WIDTH // 4 * 3, 20))

        if game_mode == "human":
            player1_label = font.render("Player 1", True, WHITE)
            player2_label = font.render("Player 2", True, WHITE)
            screen.blit(player1_label, (100, HEIGHT - 60))
            screen.blit(player2_label, (WIDTH - 300, HEIGHT - 60))
        else:
            player1_label = font.render("Player", True, WHITE)
            player2_label = font.render("CPU", True, WHITE)
            screen.blit(player1_label, (100, HEIGHT - 60))
            screen.blit(player2_label, (WIDTH - 250, HEIGHT - 60))

        if countdown > 0:
            countdown -= 1

        pygame.display.flip()
        pygame.time.Clock().tick(60)

while True:
    home_screen()
    mode = None

    while mode is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "cpu"
                if event.key == pygame.K_2:
                    mode = "human"

    main(mode)
