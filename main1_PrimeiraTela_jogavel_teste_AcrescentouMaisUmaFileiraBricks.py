#Import the pygame library and initialise the game engine
import pygame
#Let's import the Paddle Class & the Ball Class
from paddle_v2 import Paddle
from ball_v3 import Ball
from brick import Brick

 
pygame.init()
pygame.mixer.init()
 
brick_sound = pygame.mixer.Sound('brick.wav')
paddle_sound = pygame.mixer.Sound('paddle.wav')
wall_sound = pygame.mixer.Sound('wall.wav')

# Define some colors
#WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
#RED = (255,0,0)
#ORANGE = (255,100,0)
#YELLOW = (255,255,0)

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)
 
score = 0
lives = 3
 
# Open a new window
WIDTH = 600
HEIGHT = 800
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
#Create the Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
all_bricks = pygame.sprite.Group()
for i in range(14):
    brick = Brick(RED,45,10)
    brick.rect.x = 30 + i* 50
    brick.rect.y = 30
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(RED,45,10)
    brick.rect.x = 30 + i* 50
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)    
for i in range(14):
    brick = Brick(ORANGE,45,10)
    brick.rect.x = 30 + i* 50
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(YELLOW,45,10)
    brick.rect.x = 30 + i* 50
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
 
# Add the paddle and the ball to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
    #Moving the paddle when the use uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)
 
    # --- Game logic should go here
    all_sprites_list.update()
 
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
        wall_sound.play()
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
        wall_sound.play()
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        wall_sound.play()
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
        wall_sound.play()
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      paddle_sound.play()
 
    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      brick_sound.play()
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
 
    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
