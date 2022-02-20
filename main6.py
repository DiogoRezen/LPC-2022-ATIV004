#Import the pygame library and initialise the game engine
import pygame
#Let's import the Paddle Class & the Ball Class
from paddle_v2 import Paddle
from ball_v3 import Ball
from brick import Brick
from random import randint

#======================================Brick class==============================================
BLACK = (0,0,0)
 
class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

#======================================Ball class==============================================
BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        vx = randint(4,8)
        vy = 0
        while vy == 0:
            vy = randint(-8,8)
        
        self.velocity = [vx,vy]#[randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        vy = 0
        while vy == 0:
            vy = randint(-8,8)
        self.velocity[1] = vy


#======================================Paddle class==============================================
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
 
 
    def moveLeft(self, pixels, w, x_size_paddle):
        self.rect.x -= pixels
	    #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
 
    def moveRight(self, pixels, w, x_size_paddle):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > w - x_size_paddle:
          self.rect.x = w - x_size_paddle


#======================================End class declaration====================================

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
lives = 4
 
# Open a new window
WIDTH = 600
HEIGHT = 800
size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
#Create the Paddle
#paddle = Paddle(LIGHTBLUE, 100, 10)
x_size_paddle = 100
y_size_paddle = 10
paddle = Paddle(LIGHTBLUE, x_size_paddle, y_size_paddle)
paddle.rect.x = 350
paddle.rect.y = HEIGHT - 50
 
#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 300
ball.rect.y = 400

#Create the Bricks 
all_bricks = pygame.sprite.Group()
n_bricks = 14
dx = 10
brick_width = (WIDTH - (n_bricks + 1) * dx) / n_bricks

start_line_bricks = 150
y_inf_lim = 60
brick_height = 20

dy = 5

for i in range(14):
    brick = Brick(RED,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 1 * dy + 0 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(RED,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 2 * dy + 1 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(ORANGE,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 3 * dy + 2 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(ORANGE,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 4 * dy + 3 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(GREEN,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 5 * dy + 4 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)      
for i in range(14):
    brick = Brick(GREEN,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 6 * dy + 5 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(YELLOW,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 7 * dy + 6 * brick_height
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(YELLOW,brick_width,20)
    brick.rect.x = (i + 1) * dx + i * brick_width
    brick.rect.y = start_line_bricks + 8 * dy + 7 * brick_height
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
    speed_paddle = 15
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(speed_paddle,WIDTH,x_size_paddle)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(speed_paddle,WIDTH,x_size_paddle)
 
    # --- Game logic should go here
    all_sprites_list.update()
 
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= WIDTH - 2 * dx:
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = WIDTH - 2 * dx
        wall_sound.play()
    if ball.rect.x <= 2 * dx:
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 2 * dx
        wall_sound.play()
    if ball.rect.y > HEIGHT - 2 * dx:
        ball.velocity[1] = ball.velocity[1]
        ball.rect.x = WIDTH // 2 - 5
        ball.rect.y = HEIGHT // 2 - 5        
        wall_sound.play()
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font('DSEG14Classic-Bold.ttf', 44)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (WIDTH/2 - 150,HEIGHT/2 + 100))
            pygame.display.flip()
            pygame.time.wait(2000)
 
            #Stop the Game
            carryOn=False
 
    if ball.rect.y < y_inf_lim:
        ball.rect.y = y_inf_lim
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
            font = pygame.font.Font('DSEG14Classic-Bold.ttf', 44)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (WIDTH/2 - 100,HEIGHT/2 + 100))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            carryOn=False
 
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(BLACK)

    # Drawing the boards
    # Horizontal boards
    pygame.draw.line(screen, WHITE, [0, 50], [WIDTH, 50], 2 * dx)
    pygame.draw.line(screen, WHITE, [0, HEIGHT], [WIDTH, HEIGHT], 3 * dx)
    # Vertical boards
    pygame.draw.line(screen, WHITE, [0,0],[0,HEIGHT], 4 * dx)
    pygame.draw.line(screen, WHITE, [WIDTH,0],[WIDTH,HEIGHT], 4 * dx)
    # Vertical boards effect
    pygame.draw.line(screen, LIGHTBLUE, [0,paddle.rect.y - 0.5 * y_size_paddle],[0,paddle.rect.y + 1.5 * y_size_paddle], 4 * dx)
    pygame.draw.line(screen, LIGHTBLUE, [WIDTH,paddle.rect.y - 0.5 * y_size_paddle],[WIDTH,paddle.rect.y + 1.5 * y_size_paddle], 4 * dx)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font('DSEG14Classic-Bold.ttf', 34)
    text = font.render("SCORE: " + str(score), 1, WHITE)
    screen.blit(text, (4*dx,1))
    text = font.render("LIVES: " + str(lives), 1, WHITE)
    screen.blit(text, (WIDTH/2 + 50,1))

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
