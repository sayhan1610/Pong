# **Workshop: Building a Pong Game with Pygame**

### **Objective**
By the end of this workshop, participants will have built a fully functional Pong game with:
- Single-player (CPU) and two-player modes
- Score tracking
- Sound effects
- A pause menu

---

## **1. Setup & Installation**
### **Step 1: Install Pygame**
Before starting, make sure you have Python installed. Then, install Pygame by running:

```sh
pip install pygame
```

### **Step 2: Create a New Python File**
Create a file named `pong.py` and open it in a code editor (VS Code, PyCharm, etc.).

---

## **2. Setting Up the Game Window**
### **Step 3: Initialize Pygame**
At the top of your `pong.py` file, add the following:

```python
import pygame
import sys
import random
import time

pygame.init()
```

### **Step 4: Define Game Variables**
```python
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
```

This sets up the game window and defines colors, ball speed, and paddle sizes.

---

## **3. Creating the Game Menu**
### **Step 5: Display a Home Screen**
Create a function to display the menu where players choose between single-player and two-player modes:

```python
def home_screen():
    screen.fill(BLACK)
    title = font.render("Pong Game", True, WHITE)
    option1 = font.render("1. Play against CPU", True, WHITE)
    option2 = font.render("2. Play against Human", True, WHITE)
    
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, HEIGHT // 2))
    screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, HEIGHT // 2 + 100))
    
    pygame.display.flip()
```

---

## **4. Implementing the Pause Menu**
### **Step 6: Add a Pause Function**
```python
def pause_game():
    paused = True
    line1 = font.render("Paused. Press ESC to Resume", True, WHITE)
    line2 = font.render("Press Q to Quit to Home", True, WHITE)
    
    screen.fill(BLACK)
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
```

This allows players to pause the game and return to the home menu.

---

## **5. Adding the Game Over Screen**
### **Step 7: Implement the Game Over Screen**
```python
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
```

---

## **6. Coding the Main Game Logic**
### **Step 8: Creating Paddles and Ball**
Inside the `main(game_mode)` function:

```python
def main(game_mode):
    paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

    score1, score2 = 0, 0
```

---

## **7. Implementing Player and CPU Controls**
### **Step 9: Moving the Paddles**
```python
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
```

---

## **8. Implementing Ball Movement & Collision**
### **Step 10: Ball Movement and Collision**
```python
    if countdown <= 0:
        ball.x += ball_dx
        ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1
        ball_dy = random.randint(-BALL_SPEED, BALL_SPEED)
```

---

## **9. Implementing Scoring System**
### **Step 11: Scoring Logic**
```python
    if ball.left <= 0:
        score2 += 1
        if score2 == 10:
            game_over("Player 2" if game_mode == "human" else "CPU")
            main(game_mode)

    if ball.right >= WIDTH:
        score1 += 1
        if score1 == 10:
            game_over("Player 1")
            main(game_mode)
```

---

## **10. Running the Game**
### **Step 12: Start the Game from the Menu**
```python
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
```

---

## **Final Notes**
- Run `pong.py` to start the game.
- Use **W/S** for Player 1 and **UP/DOWN** for Player 2.
- **Escape (ESC)** pauses the game.
- First to **10 points** wins.

