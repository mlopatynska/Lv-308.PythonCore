import pygame

WHITE = (255, 255, 255)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

screen_height = 685
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("images/road2.png")
pygame.display.set_caption("RACING")
clock = pygame.time.Clock()

main_car = pygame.image.load("images/main_car.png")


class Car(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface((screen_width, screen_height))
        self.image.fill(WHITE)

        self.image = pygame.image.load("images/main_car.png").convert_alpha()

        self.rect = self.image.get_rect()

    def right(self, move):
        self.rect.x += move

    def left(self, move):
        self.rect.x -= move


all_sprites_list = pygame.sprite.Group()
main_car = Car(100, 200)
main_car.rect.x = 200
main_car.rect.y = 300

all_sprites_list.add(main_car)


hold_right = False
hold_left = False
hold_down = False
hold_up = False
game_over = False
car_x = 300
car_y = 500


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
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

    if hold_left:
        main_car.move(-4)
        if car_x < 5:
            car_x = 5
    if hold_right:
        main_car.move(4)
        if car_x > 520:
            car_x = 520
    if hold_up:
        car_y -= 4
        if car_y < 0:
            car_y = 0
    if hold_down:
        car_y += 4
        if car_y > 510:
            car_y = 510

    all_sprites_list.update()
    screen.fill(WHITE)
    screen.blit(main_car())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()