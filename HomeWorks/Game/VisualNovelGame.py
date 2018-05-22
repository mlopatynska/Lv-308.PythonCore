import pygame
import random
from Depends import Background, Sprite, image_shower, DialogueWindow, Button
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
gameDisplay = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
background = None
global_dialog = 0
BG = Background
DG = DialogueWindow
BackGround = None
Dialogue = None
screen_mode = "window"
block_input = False
number = 0
music_button_activator = False
music_idle = True
particles_list = {}
non_touch_zone =(1800,10,1800+80,10+40)
music = {
    "gamer": "Gainer.mp3",
}
score = 0

class ParticleGenerator(object):
    def __init__(self, screen):
        import random
        import time
        self.screen = screen
        self.random_coords = random.randint(10, 1900), random.randint(15, 1070)
        self.rect = self.random_coords[0], self.random_coords[1], self.random_coords[0] + 20, \
                    self.random_coords[1] + 20
        self.create_time = int(time.clock())

    def collide(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if ((self.mouse[0] > self.rect[0]-20 and self.mouse[0] < self.rect[2]) and
                (self.mouse[1] > self.rect[1]-20 and self.mouse[1] < self.rect[3]) and
                (self.click[0] == 1)):
            return True
    def show(self):
        colors = ((255, 255, 255), (119, 232, 38), (38, 109, 232), (232, 145, 38))
        pygame.draw.circle(self.screen, (255, 255, 255), (self.random_coords), 20)
    def need_to_delete(self):
        import time
        self.timenow = int(time.clock())
        if (self.timenow - self.create_time) >= 3:
            return True


def particles_handler(particles_list):
    global score
    for i in particles_list:
        i.show()
        if i.collide():
            particles_list.remove(i)
            score += 1
        if i.need_to_delete():
            try:
                particles_list.remove(i)
            except ValueError:
                pass
        if len(particles_list) <7:
            part_appended = ParticleGenerator(gameDisplay)
            particles_list.append(part_appended)

def music_player():
    global music_idle, block_input, number, non_touch_zone
    if not block_input:
        music_button = Button(gameDisplay, 1800, 10, hight=40, width=80, text="music")
        music_status = music_button.show_button(on=music_idle)
        if music_status is not None:
            music_idle = music_status


def dialog_window(question_answer1=("Do you want to play my game?", "Yes"),
                  question_answer2=("Do you want to play my game?", "No"), shadow=False):
    global Dialogue, DG, block_input, global_dialog, number
    block_input = True
    test1 = DialogueWindow("Button.png", 0, [690, 490])
    var_1 = test1.combine(gameDisplay, question_answer1[0], question_answer1[1], 20, black=shadow)
    test2 = DialogueWindow("Button.png", 0, [690, 590])
    var_2 = test2.combine(gameDisplay, question_answer2[0], question_answer2[1], 20)
    if var_1:
        global_dialog = 1
        number = 0
        block_input = False
        return
    elif var_2:
        global_dialog = 2
        number = 0
        block_input = False
        return



def text_commands_parser(lists, color=(0, 0, 0), size=13):
    global number
    try:
        if "<>" in lists[number]:
            exec(lists[number].replace("<>", ""), globals())
            number += 1
        elif "><" in lists[number]:
            exec(lists[number].replace("><", ""))
        else:
            set_text = image_shower(lists[number],
                                    'freesansbold.ttf',
                                    color=color,
                                    size=size,
                                    coord_x=1350,
                                    coord_y=630)
            gameDisplay.blit(set_text[0], set_text[1])
    except IndexError:
        return "end"


def start():
    global BackGround, BG
    BackGround = BG("cmd.png")
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                elif event.key == pygame.K_RETURN:
                    visual_novel()
        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        press_enter = image_shower("Press Enter to start", "6622.ttf",
                                   color=(255, 255, 255), coord_y=450)
        press_esc = image_shower("Press Esc to quit", "6622.ttf",
                                 color=(255, 255, 255), coord_y=600)
        press_f = image_shower("Press f for full-screen mode", "6622.ttf",
                               color=(255, 255, 255), coord_y=750)
        gameDisplay.blit(press_enter[0], press_enter[1])

        gameDisplay.blit(press_esc[0], press_esc[1])
        gameDisplay.blit(press_f[0], press_f[1])
        pygame.display.update()
        clock.tick(10)


def mini_game():
    global BackGround, BG, screen_mode, number, global_dialog, music_button_activator, \
        block_input, particles_list, score
    number = 0




    tutorial = ['So, game is pretty simple',
                'All, that you must to do is click colored bubbles',
                'Score 60 of them!',
                '><dialog_window(question_answer1=("Start game?", "Yes"),\
question_answer2=("Start game?", "Yes, of course"),shadow=True)']
    global_dialog = None
    score = 0
    BackGround = BG("colours_minigame.jpg")

    start_minigame=False
    parts1 = ParticleGenerator(gameDisplay)
    parts2 = ParticleGenerator(gameDisplay)
    parts3 = ParticleGenerator(gameDisplay)
    parts4 = ParticleGenerator(gameDisplay)
    parts5 = ParticleGenerator(gameDisplay)
    parts6 = ParticleGenerator(gameDisplay)
    parts7 = ParticleGenerator(gameDisplay)
    parts8 = ParticleGenerator(gameDisplay)
    parts9 = ParticleGenerator(gameDisplay)
    particles_list = [parts1, parts2, parts3, parts4, parts5, parts6, parts7, parts8, parts9]
    while True:
        pygame.init()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not block_input and \
                     (pos[0] < non_touch_zone[0] or pos[0] > non_touch_zone[2]) and \
                     (pos[1] < non_touch_zone[1] or pos[0] > non_touch_zone[3]):
                number +=1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_f and screen_mode == "fullscreen":
                    pygame.display.set_mode((1920, 1080))
                    screen_mode = "window"
                elif event.key == pygame.K_f and screen_mode == "window":
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    screen_mode = "fullscreen"
            elif event.type == pygame.MOUSEMOTION:
                pass
        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        if music_button_activator and not block_input:
            music_player()
        if not start_minigame:
            if global_dialog == 1 or global_dialog == 2:
                start_minigame = True
            else:
                text_commands_parser(tutorial, color=(255, 255, 255), size=20)
        else:
            particles_handler(particles_list)
            set_text = image_shower(str(score),
                                    'freesansbold.ttf',
                                    color=(255, 255, 255),
                                    size=50)
            gameDisplay.blit(set_text[0], set_text[1])
        if score == 60:
            return
        pygame.display.update()
        clock.tick(60)


def visual_novel():
    global BackGround, BG, screen_mode, block_input, global_dialog,\
        number, music_button_activator, music_idle, non_touch_zone

    phrase_list = ["Oh, hi!",
                   'This is my first test game on PyGame!',
                   'I still have so much to do, but',
                   'the basis is already there',
                   'Example:',
                   'You can change background here',
                   'Just like that',
                   'Pa-daaaaa',
                   '<>BackGround = BG("roof_night.jpg")',
                   'Working',
                   'But silence is so awful...',
                   'Here, i created my own 8-bit track!',
                   'Check it out!',
                   '<>pygame.mixer.music.load(music.get("gamer"))',
                   '<>pygame.mixer.music.play()',
                   'Yep',
                   '(Music playing)',
                   '<>pygame.mixer.music.set_volume(0)',
                   '<>music_button_activator = True',
                   'If you want to turn it on, then just press a button',
                   'Now, you will saw a little dialogue window',
                   '><dialog_window(shadow=True)',
                   ]

    variant_yes = ['So, yo really want to play?',
                   'Ok!',
                   '><mini_game()'
                   ]

    variant_no = ['So, you choose "no"...',
                  'We\'ll play the game anyway',
                  '><mini_game()'
                  ]
    BackGround = BG("roof_pool.jpg")


    sprite_image = "dog.png"
    sprite_bubble = "Speech-Bubble.png"
    Sprite_of_dog = Sprite(sprite_image, 0, [700, 600])
    Bubble_sprite = Sprite(sprite_bubble, 0, [1180, 500])
    while True:
        pygame.init()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not block_input and \
                    (pos[0]<non_touch_zone[0] or pos[0]>non_touch_zone[2]) and\
                    (pos[1]<non_touch_zone[1] or pos[0]>non_touch_zone[3]):
                if event.button == 1:
                    number += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_f and screen_mode == "fullscreen":
                    pygame.display.set_mode((1920, 1080))
                    screen_mode = "window"
                elif event.key == pygame.K_f and screen_mode == "window":
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    screen_mode = "fullscreen"
            elif event.type == pygame.MOUSEMOTION:
                pass

        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        gameDisplay.blit(Sprite_of_dog.image, Sprite_of_dog.rect)
        gameDisplay.blit(Bubble_sprite.image, Bubble_sprite.rect)
        if global_dialog == 0:
            if text_commands_parser(phrase_list) != "end":
                pass
            else:
                return
        elif global_dialog == 1:
            if text_commands_parser(variant_yes) != "end":
                pass
            else:
                return
        elif global_dialog == 2:
            if text_commands_parser(variant_no) != "end":
                pass
            else:
                return
        if music_button_activator and not block_input:
            music_player()

        pygame.display.update()
        clock.tick(60)



start()