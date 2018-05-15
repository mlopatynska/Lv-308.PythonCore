import pygame
import random

Background = (20, 20, 20)


class Rectangle:
    def __init__(self):
        self.x = random.randrange(1680)
        self.y = random.randrange(1050)
        self.height = random.randrange(20, 70)
        self.width = random.randrange(20, 70)
        self.red = random.randrange(0, 255)
        self.green = random.randrange(0, 255)
        self.blue = random.randrange(0, 255)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)

    def draw(self):
        pygame.draw.rect(screen, (self.red, self.green, self.blue),
                         (self.x, self.y, self.height, self.width))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Rectangle):

    def draw(self):
        pygame.draw.ellipse(screen, (self.red, self.green, self.blue),
                            (self.x, self.y, self.height, self.width))


pygame.init()

screen_size = (1680, 1050)
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)

pygame.display.set_caption("Crazy shapes")

done = False

clock = pygame.time.Clock()

# rectan = Rectangle(random.randrange(0, 800),
#                    random.randrange(0, 600),
#                    random.randrange(20, 70),
#                    random.randrange(20, 70),
#                    random.randrange(0, 255),
#                    random.randrange(0, 255),
#                    random.randrange(0, 255),
#                    random.randrange(-3, 3),
#                    random.randrange(-3, 3))
#
#
# ellipse = Ellipse(random.randrange(0, 800),
#                   random.randrange(0, 600),
#                   random.randrange(20, 70),
#                   random.randrange(20, 70),
#                   random.randrange(0, 255),
#                   random.randrange(0, 255),
#                   random.randrange(0, 255),
#                   random.randrange(-3, 3),
#                   random.randrange(-3, 3))

my_list = []
for i in range(800):
    my_list.append(Rectangle())

for j in range(800):
    my_list.append(Ellipse())


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or\
           event.type == pygame.KEYDOWN:
            done = True

    screen.fill(Background)

    for z in range(0, 1600):
        my_list[z].draw()
        my_list[z].move()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
