
import pygame, random

pygame.init()

background = pygame.image.load("images/road.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
some_color = (150, 50, 90)
shooting_sound = pygame.mixer.Sound("sounds/car_start.wav")
screen_height = 600
screen_width = 685
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("First game")
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
font = pygame.font.Font(None, 42)






class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.background = pygame.image.load("images/road2.png")
        self.main_car = pygame.image.load("images/main_car.png")
        self.car_1 = pygame.image.load("images/car_2.png")
        self.car_2 = pygame.image.load("images/car_3.png")
        self.screen_height = 685
        self.screen_weight = 600
        self.currentImage = 0

    def render_main_car(self):
        screen.blit(self.main_car, (self.x, self.y))

    def render_car(self):
        screen.blit(self.main_car, (self.x, self.y))

    def update(self):
        # self.y += 1
        if self.y > screen_height:
            self.y = random.randrange(-10, -10)
            self.x = random.randrange(0, screen_width)

    def message(msg, color):
        text = font.render(msg, True, color)
        screen.blit(text, [screen_width / 2, screen_height / 4])


x = 0
y = 0
hold_right = False
hold_left = False
hold_down = False
hold_up = False
done = False
game_over = False
player1 = Sprite(120, 480)
player2 = Sprite(200, 400)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

            if event.key == pygame.K_w:
                hold_up = True
            if event.key == pygame.K_s:
                hold_down = True
            if event.key == pygame.K_d:
                hold_right = True
            if event.key == pygame.K_a:
                hold_left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hold_up = False
            if event.key == pygame.K_s:
                hold_down = False
            if event.key == pygame.K_d:
                hold_right = False
            if event.key == pygame.K_a:
                hold_left = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True
            shooting_sound.play()

    if hold_left:
        x -= 4
        # if x < -20:
        #     x = -20
    if hold_right:
        x += 4
        if x > 600:
            x = 600
    if hold_up:
        y -= 4
        # if y < -20:
        #     y = -20
    if hold_down:
        y -= 4
        # if y > 490:
        #     y = 490

    screen.fill(WHITE)

    if game_over:
        # If game over is true, draw game over
        text = font.render("Game Over", True, WHITE)

        text_x = 100
        text_y = 200
        screen.blit(screen, [text_x, text_y])
    scroll_y = y % background.get_rect().width
    screen.blit(background, (background.get_rect().height, 0))
    if scroll_y < screen_height:
        screen.blit(background, (0, -scroll_y))
    y -= 1


    player1.x = x
    # player.y = y

    player1.render_main_car()
    player2.render_car()

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
quit()

