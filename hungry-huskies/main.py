import pygame
import sys
from dog import Dog
from food import Food
import random
from filesave import *
import json

pygame.init()
clock = pygame.time.Clock()

size = width, height = 600, 800
foodspeed = 6
dogspeed = 5
foodx = [25, 125, 225, 325, 425, 525]

BLUE = (135, 200, 255)
BLUE1 = (117, 191, 255)
GREY = (212, 212, 212)
UCONNBLUE = (0, 14, 47)
UCONNGREY = (124, 135, 142)
UCONNRED = (228, 0, 43)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hungry Huskies')
background = pygame.image.load('./photos/background.png')
screen.fill(UCONNBLUE)
# screen.blit(background, (0,0))


bone = Food('./resized_photos/food/bone.png', foodx[0], 0, foodspeed)
cheese = Food('./resized_photos/food/cheese.png', foodx[1], 0, foodspeed)
peanutbutter = Food('./resized_photos/food/peanutbutter.png', foodx[2], 0, foodspeed)
salmon = Food('./resized_photos/food/salmon.png', foodx[3], 0, foodspeed)
strawberry = Food('./resized_photos/food/strawberry.png', foodx[4], 0, foodspeed)
watermelon = Food('./resized_photos/food/watermelon.png', foodx[5], 0, foodspeed)

carson = Dog('./resized_photos/dogs/carson.png', 'Carson', 'Strawberry', 250, 650)
celeste = Dog('./resized_photos/dogs/celeste.png', 'Celeste', 'Bone', 250, 650)
jonathan = Dog('./resized_photos/dogs/jonathan.png', 'Jonathan', 'Watermelon', 250, 650)
marlin = Dog('./resized_photos/dogs/marlin.png', 'Marlin', 'Cheese', 250, 650)
tildy = Dog('./resized_photos/dogs/tildy.png', 'Tildy', 'Salmon', 250, 650)
wonton = Dog('./resized_photos/dogs/wonton.png', 'Wonton', 'Peanut Butter', 250, 650)

foods = [bone, cheese, peanutbutter, salmon, strawberry, watermelon]
dogs = [carson, celeste, jonathan, marlin, tildy, wonton]

favfoods = {
    'Carson': strawberry,
    'Celeste': bone,
    'Jonathan': watermelon,
    'Marlin': cheese,
    'Tildy': salmon,
    'Wonton': peanutbutter
}

try:
    with open('data.json', 'r') as f:
        highscores = json.load(f)
except:
    highscores = {
        'Carson': 0,
        'Celeste': 0,
        'Jonathan': 0,
        'Marlin': 0,
        'Tildy': 0,
        'Wonton': 0
    }
    write_tofile(highscores)
else:
    write_tofile(highscores)





while True:
    gameon = False
    score = 0

    screen.fill(UCONNBLUE)
    i = 1
    x, y = 20, 5
    xt, yt = x + 200, y + 5
    xf = xt - 75
    for dog in dogs:
        screen.blit(dog.img, (x, y))

        font = pygame.font.Font('./fonts/GOODDP__.TTF', 40)
        screen.blit(font.render(f'{i}: {dog.name}', True, WHITE), (xt, yt))
        yt += 40
        font = pygame.font.Font('./fonts/GOODDP__.TTF', 25)
        screen.blit(font.render(f'Favorite Treat: {dog.favfood}', True, WHITE), (xt, yt))
        screen.blit(favfoods[dog.name].img, (xf, yt))
        yt += 25
        hs = highscores[dog.name]
        screen.blit(font.render(f'High Score: {hs}', True, WHITE), (xt, yt))

        yt += 65
        i += 1
        y += 130


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                currentdog = dogs[0]
                favfood = favfoods[currentdog.name]
                gameon = True
            elif event.key == pygame.K_2:
                currentdog = dogs[1]
                favfood = favfoods[currentdog.name]
                gameon = True
            elif event.key == pygame.K_3:
                currentdog = dogs[2]
                favfood = favfoods[currentdog.name]
                gameon = True
            elif event.key == pygame.K_4:
                currentdog = dogs[3]
                favfood = favfoods[currentdog.name]
                gameon = True
            elif event.key == pygame.K_5:
                currentdog = dogs[4]
                favfood = favfoods[currentdog.name]
                gameon = True
            elif event.key == pygame.K_6:
                currentdog = dogs[5]
                favfood = favfoods[currentdog.name]
                gameon = True

    while gameon:
        screen.blit(background, (0, 0))
        if foods[0].pos[1] >= 700:
            xdif = abs((currentdog.pos[0] + 50) - (favfood.pos[0] + 25))
            if xdif < 50:
                score += 1
            else:
                gameon = False
                if score > highscores[currentdog.name]:
                    highscores[currentdog.name] = score
                    write_tofile(highscores)
            random.shuffle(foodx)
            i = 0
            for food in foods:
                food.pos[0] = foodx[i]
                food.totop()
                i += 1 
        if gameon:
            for food in foods:
                food.move()
                screen.blit(food.img, food.pos)

        sbcor = [250, 10]
        font = pygame.font.Font('./fonts/GOODDP__.TTF', 40)
        highscore = highscores[currentdog.name]
        screen.blit(font.render(f'Score: {score}', True, WHITE), sbcor)
        sbcor[0] -= 25
        sbcor[1] += 40
        font = pygame.font.Font('./fonts/GOODDP__.TTF', 35)
        screen.blit(font.render(f'High Score: {highscore}', True, WHITE), sbcor)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and currentdog.pos[0]>0:
            currentdog.pos[0] -= dogspeed
        if keys[pygame.K_RIGHT] and currentdog.pos[0]<500:
            currentdog.pos[0] += dogspeed
        pygame.event.pump()
        pygame.draw.rect(screen, UCONNRED, (0, 700, 600, 100))
        screen.blit(currentdog.img, currentdog.pos)

        pygame.display.update()
        clock.tick(60)
    pygame.display.update()
    clock.tick(60)