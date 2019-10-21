import pygame
import random
import time
import os

pygame.mixer.init()
pygame.init()
display_width = 800
display_height = 600
#color
gray = (105,105,105)
white = (255,255,255)
red = (255,0,0)
gold = (255, 255, 0)
#backgrounds
grassimg=pygame.image.load("grass.png")
sideline_rtl=pygame.image.load("side line right.png")
#image car
carimg = pygame.image.load("car.png")
roadimg = pygame.image.load("road.png")
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car race")
clock = pygame.time.Clock()
car_width = 60
car_hight = 120
x = (display_width * 0.38)
y = (display_height * 0.66)

def game_starter():
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mnu_bg=pygame.image.load("background_menu.png")
        gameDisplay.blit(mnu_bg,(0,0))
        pygame.display.update()
        time.sleep(3)
        game_menu()
def game_menu() :

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        menu=pygame.image.load("menu.png")
        gameDisplay.blit(menu,(0,0))
        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        #print(click)
        #print(mouse)
        if 60 + 300 > mouse[0] > 60 and 60 < mouse[1] < 60 + 100:
            pygame.draw.rect(gameDisplay, gray, (60, 60, 300, 100))
            if click[0]==1 :
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, white, (60, 60, 300, 100))
            if click[0]==1:
                quit()
        btntxt=pygame.font.Font('freesansbold.ttf',70)
        TextSurf, TextRect = text_object("START", btntxt)
        TextRect.center = ((60+(300 / 2)), (60 + (100 / 2)))
        gameDisplay.blit(TextSurf, TextRect)

        if 400 + 300 > mouse[0] > 400 and 60 < mouse[1] < 60 + 100:
            pygame.draw.rect(gameDisplay, gray, (400, 60, 300, 100))
        else:
            pygame.draw.rect(gameDisplay, white, (400, 60, 300, 100))
        btntxt2 = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_object("EXIT", btntxt)
        TextRect.center = ((400 + (300 / 2)), (60 + (100 / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        
def background ():
    
    gameDisplay.blit(grassimg,(0,0))
    gameDisplay.blit(grassimg,(0,400))
    gameDisplay.blit(grassimg,(600,0))
    gameDisplay.blit(grassimg,(600,400))
    gameDisplay.blit(sideline_rtl,(580,0))
    gameDisplay.blit(sideline_rtl,(180,0))

def score(i):
    font= pygame.font.Font('freesansbold.ttf',20)
    text =font.render("score :"+ str(i) , True , gold)
    gameDisplay.blit(text,(1,1))

def line(line_x,line_y):
    lineimg=pygame.image.load("line.png")
    gameDisplay.blit(lineimg,(line_x,line_y))

def text_object(text,font):
    textsurface = font.render(text,True,red)
    return textsurface,textsurface.get_rect()

def enemy_cars (enemy_x,enemy_y):
    enemyimg = pygame.image.load("enemy.png")
    gameDisplay.blit(enemyimg,(enemy_x,enemy_y))

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_object(text,large_text)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def crash(x,y):
    pygame.mixer.music.load("game_over.mp3")
    pygame.mixer.music.play(0)
    exp = ['exp1.png','exp2.png','exp3.png','exp4.png','exp5.png','exp6.png','exp7.png','exp8.png']
    #exp = ["exp1.png","exp2.png","exp3.png","exp4.png","exp5.png","exp6.png","exp7.png","exp8.png"]
    while True:
        s=2
        for  s in range(2,8):
            exp_final= pygame.image.load(exp[s])
        #exp_final=pygame.image.load('exp'+str()+'.png')
            gameDisplay.blit(exp_final,(x+68,y+60))
            pygame.display.update()
        else:
            break
    message_display("Game Over ")
def game_loop():
    #music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1,0.0)
    game_score=0

    #enemy
    enemy_x = random.randrange(0,display_width)
    enemy_width = 60
    enemy_height = 120
    enemy_y = -700
    speed_enemy= 6
    #line
    speed_line = 6
    line_width = 80
    line_height = 100
    line_x =(display_width* 0.45)
    line_y = 600
    x = (display_width * 0.38)
    y = (display_height * 0.66)
    x_change = 0
    y_change = 0
    rnd = 0
    game_exit = False
    enemy_cars(enemy_x,enemy_y)
    enemy_y += speed_enemy
    enemy_y = 0 - enemy_height                        
    enemy_x= random.randrange(160,(display_width-350))

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(gray)  # صفحه را سفید میکند طبق رنگ سفیدی که معرفی کردیم
        background()
        score(game_score)
        line(line_x,line_y)
        line_y += speed_line
        if  (line_y + line_height) > display_height  :
            line_y = - 400
        enemy_cars(enemy_x,enemy_y)
        enemy_y += speed_enemy
        if enemy_y > display_height:
            enemy_y = 0 - enemy_height
            enemy_x= random.randrange(140,(display_width-340))
            print(display_width)
            #enemy_x=random.randrange(140,(display_width-140))
            game_score = game_score + 1
            if game_score % 10 ==0 :
                speed_enemy+=1
                speed_line +=1
        car(x,y)
        if  x > (display_width-340) or x< 140:
        #if x > display_width - (car_width+(car_width*2)) or x<140:
            crash(x,y)
        if y >display_height -car_hight or y <-100 :
            y = 430
        print(y,car_hight,enemy_y,enemy_height)
        print(x,car_width,enemy_x,enemy_width)
        if y < enemy_y + enemy_height and y>enemy_y - enemy_height :
            if x >enemy_x and x < enemy_x + enemy_width or x + car_width > enemy_x and x +car_width <enemy_x + enemy_width :
                crash(x,y)
        pygame.display.update()
        clock.tick(60)
game_starter()
game_menu()
game_loop()
pygame.quit()

