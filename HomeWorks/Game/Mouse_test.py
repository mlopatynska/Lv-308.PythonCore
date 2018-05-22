import pygame
clock = pygame.time.Clock()
while True:
    pygame.init()
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
       pass

    elif event.type == pygame.MOUSEMOTION:
        print("mouse at (%d, %d)" % event.pos)


    clock.tick(10)
