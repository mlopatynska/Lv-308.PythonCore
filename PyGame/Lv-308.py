import pygame
pygame.init()

background_image = pygame.image.load("saturn_family1.jpg")
player_image = pygame.image.load("playerShip1_orange.png")
click_sound = pygame.mixer.Sound("Ok.wav")



screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game')
clock = pygame.time.Clock()


done = False
stop = False

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("The END",True,BLACK)

i,x,y = 0, 0, 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print "You press Q"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            stop = not stop
            click_sound.play()
        elif event.type == pygame.MOUSEMOTION:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]

        #print(event)

    #screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    screen.blit(player_image, [x-47, y])


    pygame.draw.line(screen, GREEN, [0,0], [800,600], 5)
    pygame.draw.circle(screen, RED, [400,300], 100, 0)

    #for i in range(0,800,200):
    pygame.draw.rect(screen, BLUE, [i, 0, 100, 100], 0)

    if not stop:
        if i > 800:
            i = 0
        else:
            i += 10

    screen.blit(text, [400, 300])
    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()
