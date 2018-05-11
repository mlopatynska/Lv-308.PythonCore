import pygame, random

pygame.init()

size_x = 1280
size_y = 720

colors = {
                'green': (0, 255, 0),
                'white': (255, 255, 255),
                'red': (255, 0, 0),
                'blue': (0, 0, 255),
                'black': (0, 0, 0)
}

screen = pygame.display.set_mode((size_x, size_y))
end = False


class Rectangle:
    def __init__(self):
        self.x = random.randint(0, 1280)
        self.y = random.randint(0, 720)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def draw(self):
        self.figure = pygame.draw.rect(screen, (self.r, self.g, self.b),
                                [self.x, self.y, self.height, self.width])

    def move(self):
        self.x = self.x + random.randint(-3, 3)
        self.y = self.y + random.randint(-3, 3)


class Ellipse(Rectangle):
    def draw(self):
        self.figure = pygame.draw.ellipse(screen, (self.r, self.g, self.b),
                    [self.x, self.y, self.height, self.width], 0)


rect_list = []
ell_list = []
#----------------------VAR CHAR--------------------


while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            end = True
    screen.fill(colors['black'])

    for x in range(0, 1000):
        rect_list.append(Rectangle())
        rect_list[x].draw()
        rect_list[x].move()

    for x_ell in range(0, 1000):
        ell_list.append(Ellipse())
        ell_list[x_ell].draw()
        ell_list[x_ell].move()

    pygame.display.update()
