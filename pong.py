import pygame
import sys

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

paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

score1, score2 = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        paddle1.y += PADDLE_SPEED

    if keys[pygame.K_UP]:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        paddle2.y += PADDLE_SPEED

    paddle1.y = max(0, min(paddle1.y, HEIGHT - PADDLE_HEIGHT))
    paddle2.y = max(0, min(paddle2.y, HEIGHT - PADDLE_HEIGHT))

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1

    if ball.left <= 0:
        score2 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1

    if ball.right >= WIDTH:
        score1 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw the scores
    text1 = font.render(str(score1), True, WHITE)
    screen.blit(text1, (WIDTH // 4, 20))
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text2, (WIDTH // 4 * 3, 20))

    # Draw the player labels
    player1_label = font.render("Player 1", True, WHITE)
    player2_label = font.render("Player 2", True, WHITE)
    screen.blit(player1_label, (100, HEIGHT - 60))
    screen.blit(player2_label, (WIDTH - 300, HEIGHT - 60))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
