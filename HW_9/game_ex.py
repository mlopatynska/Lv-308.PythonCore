import pygame
import random

# Define some colors
diapazon = range(256)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_height = 800
screen_width = 800

class Rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], 0)

class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.r, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    my_rect = Rectangle(random.randint(0, screen_width), random.randint(0, screen_height),
                       random.randint(0, screen_width/4), random.randint(0, screen_height/4))
    my_rect.draw()
    my_circ = Circle(random.randint(0, screen_width), random.randint(0, screen_height), random.randint(0, screen_width / 5))
    my_circ.draw()
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(8)

# Close the window and quit.
pygame.quit()