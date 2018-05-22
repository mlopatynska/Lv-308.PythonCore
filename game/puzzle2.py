import pygame
import random
import numpy as np
from PIL import Image
import time

pygame.init()

pygame.mixer.music.load('muz.mp3')
pygame.mixer.music.play(-1)

w_wind = 600
h_wind = 600
w_im = int(w_wind*4/5)
h_im = int(h_wind*3/5)
w_ex = int(w_im/2)
h_ex = int(h_im/2)

w_click = int((w_wind - 60)/3)
h_click = int((h_wind - 60)/5)

prop = 2.0 / 3

done = False
size_check = False
slice_check = False
part_check = False
rez_check = False
pos_check = [-1, -1, -1, -1]  #up1/down0, i, j +/-

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

font_slice = pygame.font.SysFont('Calibri', 30, True, False)
text_tuple = [(3, 4), (4, 5), (4, 6), (6, 8), (8, 10)]
text_slice = []

for num in text_tuple:
    text_slice.append(font_slice.render("{}x{} pieces".format(num[0], num[1]), True, WHITE))

background_image0 = pygame.image.load("fon.jpg")
background_image0 = pygame.transform.scale(background_image0, (2*w_wind, 2*h_wind))

font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("The END",True,BLACK)

background_image = pygame.image.load("fon1.jpg")
background_image = pygame.transform.scale(background_image, (2*w_wind, 2*h_wind))

screen = pygame.display.set_mode((w_wind, h_wind))
pygame.display.set_caption('Puzzle game')
clock = pygame.time.Clock()

def pos_an_cl(x,y):
    m_pos = -1
    n_pos = -1
    for i in range(5):
        for j in range(3):
            if x >= 15+j*(w_click+15) \
                    and x<15+j*(w_click+15)+w_click \
                    and y>=10+i*(h_click+10) \
                    and y<10+i*(h_click+10)+h_click:
                m_pos = j
                n_pos = i
    return (n_pos, m_pos)

def frame_paint_cl(i, j):
    pygame.draw.rect(screen, GREEN, [15 + j * (w_click+15), 10 + i * (h_click+10), w_click, h_click], 4)

screen.blit(background_image0, [0, 0])
for i in range(5):
    pygame.draw.rect(screen, WHITE, [15, 10+i*(h_click+10), w_click, h_click], 4)
    screen.blit(text_slice[i], [40, 45+i*(h_click+10)])
    part = pygame.image.load("C:\Hmarka\Lv-308.PythonCore\Game\mal_"+str(i)+".jpg")
    part1 = pygame.image.load("C:\Hmarka\Lv-308.PythonCore\Game\mal_" + str(i+5) + ".jpg")
    part = pygame.transform.scale(part, (w_click, h_click))
    part1 = pygame.transform.scale(part1, (w_click, h_click))
    screen.blit(part, [30+w_click, 10+i*(h_click+10)])
    screen.blit(part1, [45 + 2*w_click, 10 + i * (h_click + 10)])

def game_end():
    screen.blit(background_image, [0, 0])
    screen.blit(text, [200, 300])
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            game_end()
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]
            if pos_an_cl(x, y)[1] == 0 and not(size_check):
                size_check = not size_check
                m = text_tuple[pos_an_cl(x, y)[0]][1]
                n = text_tuple[pos_an_cl(x, y)[0]][0]
                frame_paint_cl(pos_an_cl(x, y)[0], pos_an_cl(x, y)[1])
            elif pos_an_cl(x, y)[1] > 0 and not(slice_check):
                slice_check = not slice_check
                frame_paint_cl(pos_an_cl(x, y)[0], pos_an_cl(x, y)[1])
                number = pos_an_cl(x, y)[0] + (pos_an_cl(x, y)[1] -1)*5
                img_file = Image.open("C:\\Hmarka\\Lv-308.PythonCore\\Game\\mal_"+str(number)+".jpg")
                img_file = img_file.resize((w_im, h_im), Image.ANTIALIAS)
                img_file.save("mal_tm.jpg")
                ex = pygame.image.load("C:\Hmarka\Lv-308.PythonCore\Game\mal_tm.jpg")
                ex = pygame.transform.scale(ex, (w_ex, h_ex))
    if size_check and slice_check:
        done = not done

    pygame.display.update()
    clock.tick(40)

w_part = w_im/(2*m)-10
h_part = h_im/(2*n)-10

x_im = (w_wind - w_im)/2
y_im = (prop*h_wind  - h_im)/2

x_part = (w_wind/2 - w_part*m-10*(m-1))/2
y_part = prop*h_wind + ((1-prop)*h_wind - h_part*n-10*(n-1))/2

x_ex = (w_wind/2 -w_ex)/2+w_wind/2
y_ex = prop*h_wind + (h_wind*(1-prop)-h_ex)/2

r_list =[]
while len(r_list)< m*n:
    p = random.randint(0, m*n-1)
    if not(p in r_list):
        r_list.append(p)

pos_part = np.reshape(r_list,(n, m))
pos_rez = np.reshape([-1 for i in range(n*m)], (n, m))
pos_end = np.reshape([i for i in range(n*m)], (n, m))
screen = pygame.display.set_mode((w_wind, h_wind))
pygame.display.set_caption('Puzzle game')
clock = pygame.time.Clock()

def pos_an(x,y):
    m_pos = -1
    n_pos = -1
    loc = -1
    elem = 0
    for i in range(n):
        for j in range(m):
            if x >= x_part+j*(w_part+10) \
                    and x<x_part+j*(w_part+10)+w_part \
                    and y>=y_part+i*(h_part+10) \
                    and y<y_part+i*(h_part+10)+h_part:
                m_pos = j
                n_pos = i
                loc = 0
                if pos_part[i][j] >=0:
                    elem = 1
            elif x >= x_im + j*w_im / m \
                    and x < x_im + (j+1)*w_im / m \
                    and y >= y_im+i*h_im / n \
                    and y < y_im+(i+1)*h_im / n:
                m_pos = j
                n_pos = i
                loc = 1
                if pos_rez[i][j] >= 0:
                    elem = 1
                # pygame.draw.rect(screen, GREEN, [x_im + j*w_im / m, y_im+i*h_im / n, w_im / m, h_im / n], 2)
    return (loc, n_pos, m_pos, elem)

def frame_paint(loc, x, y):
    if loc == 1:
        pygame.draw.rect(screen, GREEN, [x_im + y * w_im / m , y_im + x * h_im / n, w_im / m, h_im / n], 4)
    elif loc == 0:
        pygame.draw.rect(screen, GREEN, [x_part + y * (w_part + 10), y_part + x * (h_part + 10), w_part, h_part], 4)



def extr_part(num):
    i = num / m
    j = num % m
    koor_x = j * w_im / m
    koor_y = i * h_im / n
    area = (koor_x, koor_y, koor_x+w_im/m, koor_y+h_im/n)
    img_file_part = img_file.crop(area)
    img_file_part.save("part_tm.jpg")

def part_paint(loc, i, j): #loc =1 if 'up' and 0 if 'down' adn ARRAY[i,j]!=1
    if loc:
        extr_part(pos_rez[i][j])
        mal_part = pygame.image.load("part_tm.jpg")
        screen.blit(mal_part, [x_im  + j * w_im / m, y_im  + i * h_im / n])
    else:
        extr_part(pos_part[i][j])
        mal_part = pygame.image.load("part_tm.jpg")
        mal_part = pygame.transform.scale(mal_part, (w_part, h_part))
        screen.blit(mal_part, [x_part + j * (w_part+10), y_part + i * (h_part+10)])


def screen_paint(): #loc =1 if 'up' and 0 if 'down' adn ARRAY[i,j]!=1
    screen.blit(background_image, [0, 0])
    pygame.draw.line(screen, BLACK, [0, prop * h_wind], [w_wind, prop * h_wind], 1)
    pygame.draw.line(screen, BLACK, [0.5 * w_wind, prop * h_wind], [0.5 * w_wind, h_wind], 1)
    pygame.draw.rect(screen, BLUE, [x_im - 2, y_im - 2, w_im + 4, h_im + 4], 2)
    for i in range(1, m):
        pygame.draw.line(screen, BLUE, [x_im + w_im / m * i, y_im], [x_im + w_im / m * i, y_im + h_im], 1)
    for j in range(1, n):
        pygame.draw.line(screen, BLUE, [x_im, y_im + h_im / n * j], [x_im + w_im, y_im + h_im / n * j], 1)

    for i in range(n):
        for j in range(m):
            if pos_rez[i][j] >=0:
                part_paint(1, i, j)
            if pos_part[i][j] >=0:
                part_paint(0, i, j)

    screen.blit(ex, [x_ex, y_ex])
    pygame.display.update()

screen_paint()

done = False
while not done:
    if np.array_equal(pos_rez, pos_end):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]
            if pos_an(x, y)[0] >=0:
                if pos_an(x, y)[0] == 1 and part_check and not(rez_check) and pos_an(x,y)[3] == 1:
                    screen_paint()
                    frame_paint(1, pos_an(x, y)[1], pos_an(x, y)[2])
                    part_check = False
                    rez_check = True
                    pos_check = [1, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                elif pos_an(x, y)[0] == 1 and part_check and not(rez_check) and pos_an(x,y)[3] == 0:
                    pos_rez[pos_an(x, y)[1]][pos_an(x, y)[2]] = pos_part[pos_check[1]][pos_check[2]]
                    pos_part[pos_check[1]][pos_check[2]] = -1
                    part_check = False
                    rez_check = False
                    pos_check = [-1, -1, -1, -1]
                    screen_paint()
                elif pos_an(x, y)[0] == 1 and not(part_check) and not(rez_check) and pos_an(x, y)[3] == 1:
                    part_check = False
                    rez_check = True
                    pos_check = [1, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                    frame_paint(1, pos_an(x, y)[1], pos_an(x, y)[2])
                elif pos_an(x, y)[0] == 0 and part_check and pos_an(x,y)[3] == 1:
                    screen_paint()
                    frame_paint(0, pos_an(x, y)[1], pos_an(x, y)[2])
                    part_check = True
                    rez_check = False
                    pos_check = [0, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                elif pos_an(x, y)[0] == 0 and part_check and pos_an(x, y)[3] == 0:
                    pos_part[pos_an(x, y)[1]][pos_an(x, y)[2]] = pos_part[pos_check[1]][pos_check[2]]
                    pos_part[pos_check[1]][pos_check[2]] = -1
                    part_check = True
                    rez_check = False
                    pos_check = [0, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                    screen_paint()
                    frame_paint(0, pos_an(x, y)[1], pos_an(x, y)[2])
                elif pos_an(x, y)[0] == 0 and not(part_check) and not(rez_check) and pos_an(x, y)[3] == 1:
                    part_check = True
                    rez_check = False
                    pos_check = [0, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                    frame_paint(0, pos_an(x, y)[1], pos_an(x, y)[2])
                elif pos_an(x, y)[0] == 1 and not(part_check) and rez_check and pos_an(x, y)[3] == 1:
                    screen_paint()
                    part_check = False
                    rez_check = True
                    pos_check = [1, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                    frame_paint(1, pos_an(x, y)[1], pos_an(x, y)[2])
                elif pos_an(x, y)[0] == 1 and not(part_check) and rez_check and pos_an(x, y)[3] == 0:
                    pos_rez[pos_an(x, y)[1]][pos_an(x, y)[2]] = pos_rez[pos_check[1]][pos_check[2]]
                    pos_rez[pos_check[1]][pos_check[2]] = -1
                    rez_check = False
                    part_check = False
                    pos_check = [-1, -1, -1, -1]
                    screen_paint()
                elif pos_an(x, y)[0] == 0 and rez_check and pos_an(x, y)[3] == 1:
                    screen_paint()
                    part_check = True
                    rez_check = False
                    pos_check = [0, pos_an(x, y)[1], pos_an(x, y)[2], 1]
                    frame_paint(0, pos_an(x, y)[1], pos_an(x, y)[2])
                elif pos_an(x, y)[0] == 0 and rez_check and pos_an(x,y)[3] == 0:
                    pos_part[pos_an(x, y)[1]][pos_an(x, y)[2]] = pos_rez[pos_check[1]][pos_check[2]]
                    pos_rez[pos_check[1]][pos_check[2]] = -1
                    part_check = False
                    rez_chech = False
                    pos_check = [-1, -1, -1, -1]
                    screen_paint()
    pygame.display.update()
    clock.tick(40)

game_end()

pygame.quit()
quit()