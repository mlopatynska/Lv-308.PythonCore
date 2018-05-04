import pygame
pygame.init()
done = False

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('first game')
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (255,0,0)

x = 0
stop = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stop:
                stop = False
            else:
                stop = True
        print(event)

        screen.fill(WHITE)
        pygame.draw.circle(screen, BLACK, [400, 400], 300, 5)
        pygame.draw.rect(screen, RED, [350, 350, 100, 100])
        pygame.draw.line(screen, GREEN, [0, 0], [800, 800], 5)


        pygame.draw.rect(screen, BLACK, [x,  380, 50, 50])
        x += 100
        if x > 800:
            x = 0
        pygame.display.update()

        clock.tick(30)


pygame.quit()
quit()