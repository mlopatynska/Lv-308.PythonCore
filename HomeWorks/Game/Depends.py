import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def text_objects(text, font, color=(0, 0, 0)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def image_shower(text, font, color=(0, 0, 0), coord_x=1980/2, coord_y=1080/2, size=100):
    largeText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, largeText, color=color)
    TextRect.center = coord_x, coord_y
    return (TextSurf, TextRect)


class DialogueWindow(Sprite):
    def init__(self, image_file, speed, location):
        super(DialogueWindow, self).__init__(image_file, speed, location)
    def combine(self, surface, title, text, text_size, black=False):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.location_top = self.rect.top
        self.text_size = text_size
        self.title = image_shower(title,
                                  'freesansbold.ttf',
                                  color=(255, 255, 255),
                                  size=self.text_size,
                                  coord_x=1920/2,
                                  coord_y=100)
        self.shadow = black
        self.surface = surface
        self.text = text
        if self.shadow == True:
            self.black_mask = Sprite("black.png", 0, [0, 0])
            self.surface.blit(self.black_mask.image, self.black_mask.rect)
        if ((self.mouse[0]>700 and self.mouse[0] < 1330) and
                (self.mouse[1] > self.rect.top and self.mouse[1] < self.rect.top+100)):
            self.windows = image_shower(self.text,
                                        'freesansbold.ttf',
                                        color=(255, 255, 255),
                                        size=self.text_size,
                                        coord_x=self.rect.left + 300,
                                        coord_y=self.location_top + 50)
            self.surface.blit(self.image, self.rect)
            self.surface.blit(self.title[0], self.title[1])
            self.surface.blit(self.windows[0], self.windows[1])
        else:
            self.windows = image_shower(self.text,
                                        'freesansbold.ttf',
                                        color=(0, 0, 0),
                                        size=self.text_size,
                                        coord_x=self.rect.left + 300,
                                        coord_y=self.location_top + 50)
            self.surface.blit(self.image, self.rect)
            self.surface.blit(self.title[0], self.title[1])
            self.surface.blit(self.windows[0], self.windows[1])

        if ((self.mouse[0]>700 and self.mouse[0] < 1330) and
                (self.mouse[1] > self.rect.top and self.mouse[1] < self.rect.top+100) and (self.click[0] == 1)):
            return True


class Button(object):
    def __init__(self, surface, coordx, coordy, width=25, hight=15, text=""):
        self.surface = surface
        self.coordx = coordx
        self.coordy = coordy
        self.width = width
        self.hight = hight
        self.text = text
    def get_coords(self):
        return (self.coordx, self.coordy, self.width, self.hight)
    def show_button(self, on=True):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.on = on
        if ((self.mouse[0]>self.coordx and self.mouse[0] < self.coordx+self.width) and
                (self.mouse[1] > self.coordy and self.mouse[1] < self.coordy+self.hight)):
            self.windows = image_shower(self.text,
                                        'freesansbold.ttf',
                                        color=(255, 255, 255),
                                        size=20,
                                        coord_x=self.coordx+int(self.width/2),
                                        coord_y=self.coordy+int(self.hight/2))
            pygame.draw.rect(self.surface, (89, 231, 217), (self.coordx, self.coordy,
                                                            self.width, self.hight))
            self.surface.blit(self.windows[0], self.windows[1])
        else:
            self.windows = image_shower(self.text,
                                        'freesansbold.ttf',
                                        color=(0, 0, 0),
                                        size=20,
                                        coord_x=self.coordx + int(self.width / 2),
                                        coord_y=self.coordy + int(self.hight / 2))
            pygame.draw.rect(self.surface, (89, 231, 217), (self.coordx, self.coordy,
                                                            self.width, self.hight))
            self.surface.blit(self.windows[0], self.windows[1])
        if ((self.mouse[0] > self.coordx and self.mouse[0] < self.coordx + self.width) and
                (self.mouse[1] > self.coordy and self.mouse[1] < self.coordy + self.hight) and
                (self.click[0] == 1) and self.on):
            pygame.mixer.music.set_volume(50)
            return False
        elif ((self.mouse[0] > self.coordx and self.mouse[0] < self.coordx + self.width) and
                (self.mouse[1] > self.coordy and self.mouse[1] < self.coordy + self.hight) and
              (self.click[0] == 1) and not self.on):
            pygame.mixer.music.set_volume(0)
            return True




