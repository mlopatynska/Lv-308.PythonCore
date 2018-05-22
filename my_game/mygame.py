import pygame, random
pygame.init()

background = pygame.image.load("images/road2.png")
car = pygame.image.load("images/main_car.png")
car_yellow = pygame.image.load("images/car_y.png")
car_white = pygame.image.load("images/car_w.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 220)
RED = (250, 0, 0)
GREY = (10, 10, 10)


screen_height = 685
screen_width = 600

car_sound = pygame.mixer.Sound("sounds/car_start.wav")
pygame.mixer.music.load("sounds/car_start.wav")
font = pygame.font.SysFont(None, 50)
text1 = font.render("START", True, WHITE)
text2 = font.render("You broke your car", True, BLACK)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("First game")
font = pygame.font.SysFont('Calibri', 100, True, False)


clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
y = 0
car_x = 300
car_y = 500
car_height = 134
car_width = 70


def start_screen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.fill(GREY)

        button("START!", 210, 200, 160, 70, RED, BLUE, main_loop)
        pygame.display.update()
        clock.tick(10)

def button(message, but_x, but_y, but_w, but_h, b_inactive, b_active, action=None):
    """start game button"""
    mouse_button = pygame.mouse.get_pos()
    button_click = pygame.mouse.get_pressed()
    if but_x + but_w > button_click[0] > but_x and but_y + but_h > mouse_button[1] > but_y:
        pygame.draw.rect(screen, b_inactive, (but_x, but_y, but_w, but_h))
        if action != None and button_click[0] == 1:
            action()
        else:
            pygame.draw.rect(screen, b_active, (but_x, but_y, but_w, but_h))

        #pygame.draw.rect(screen, b_active, (210, 200, 160, 70))
        #pygame.draw.rect(screen, b_inactive, (210, 200, 160, 70))
    screen.blit(text1, (235, 220))

    pygame.display.update()
    clock.tick(100)


def main_car(car_x, car_y):
    screen.blit(car, (car_x, car_y))


def car_2(cars_x, cars_y):
    screen.blit(car_yellow, (cars_x, cars_y))




def main_loop():
    car_sound.play()
    car_x = 300
    car_y = 500
    cars_x = random.randrange(10, 550)
    cars_y = -100
    cars_width = 70
    y = 0
    speed = 3

    hold_right = False
    hold_left = False
    hold_down = False
    hold_up = False
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                if event.key == pygame.K_UP:
                    hold_up = True
                if event.key == pygame.K_DOWN:
                    hold_down = True
                if event.key == pygame.K_RIGHT:
                    hold_right = True
                if event.key == pygame.K_LEFT:
                    hold_left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    hold_up = False
                if event.key == pygame.K_DOWN:
                    hold_down = False
                if event.key == pygame.K_RIGHT:
                    hold_right = False
                if event.key == pygame.K_LEFT:
                    hold_left = False

        if hold_left:
            car_x -= 4
            if car_x < 5:
                car_x = 5
        if hold_right:
            car_x += 4
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

        screen.fill(WHITE)

        # scrolling background

        scroll_y = y % background.get_rect().width
        screen.blit(background, (background.get_rect().height, 0))
        if scroll_y < screen_height:
            screen.blit(background, (0, -scroll_y))
        y -= 6
        car_2(cars_x, cars_y)

        cars_y += speed
        main_car(car_x, car_y)
        if car_x < 6 or car_x > 515:
            screen.blit(text2, [150, 300])

        if cars_y > screen_height:
            cars_y = -70
            cars_x = random.randrange(10, 550)


        if (car_x > cars_x) and (car_x < cars_x + cars_width) or (car_x + car_x > cars_x)\
                and (car_x + car_x < cars_x + cars_width):
            screen.blit(text2, [150, 300])



        pygame.display.flip()
        clock.tick(150)

main_loop()
pygame.quit()
quit()

