# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:09:05 2017

@author: Shihab
"""

import pygame
import time
import random


scoreReadingHandler = open("Highscore",'r')
highscore = int(scoreReadingHandler.read())
print(highscore)
pygame.init()

display_width = 800
display_height = 600

red = (255,0,0)
dark_red = (200,0,0)
green = (0,255,0)
dark_green = (0,200,0)
blue = (0,0,255)
dark_blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Impact')
clock = pygame.time.Clock()

playerSpaceship = pygame.image.load('playerSpaceship.png')
playerSpaceship_width = 76
playerSpaceship_length = 100
playerMissile = pygame.image.load('playerMissile.png')

enemySpaceship = pygame.image.load('enemySpaceship.png')
enemySpaceship_width = 76
enemySpaceship_length = 100
enemyBullet = pygame.image.load('enemyBullet.png')


def player_spaceship (x,y):
    gameDisplay.blit(playerSpaceship,(x,y))

def missile(xm,ym,):
    gameDisplay.blit(playerMissile,(xm,ym))
    
def enemy_spaceship (x,y):
    gameDisplay.blit(enemySpaceship,(x,y))
    
def bullet(xb,yb):
    gameDisplay.blit(enemyBullet,(xb,yb))
    
    
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def message_display(text,fontSize,display_time,display_x,display_y):
    largeText = pygame.font.Font('freesansbold.ttf',fontSize)
    TextSurf, TextRect = text_objects(text,largeText,white)
    TextRect.center = (display_x, display_y)
    gameDisplay.blit(TextSurf,TextRect)
    
    pygame.display.update()
    time.sleep(display_time)
    
def game_over():
    message_display("Over Ran By Enemy!",75,2,display_width/2,display_height/2)
    game_intro()
    
def enemy_escaped(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Enemy Escaped: "+str(count), True, white)
    gameDisplay.blit(text,(display_width-200,0))
    
def game_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, white)
    gameDisplay.blit(text,(display_width-300,0))
    
def crash():
    message_display('You Crashed!',90,2,display_width/2,display_height/2)
    game_intro()

def high_score(score):
    global highscore
    if score>int(highscore):
        open('Highscore', 'w').close()
        highscoreHandler = open("Highscore",'w')
        highscoreHandler.write(str(score))
        highscoreHandler.close()
        highscore=score
    
    
def instruction():
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    textMovement = font.render("Up arrow/Down arrow - Move Up/ Down", True, white)
    textFight = font.render("Shoot - Spacebar",True, white)
    textLinegap = font.render("",True,white)
    textGameplay = font.render("SHOOT DOWN AS MANY ENEMYSPACESHIP AS POSSIBLE",True,white)
    textGameplay2 = font.render("IF YOU MISS MORE THAN 5 ENEMY OR CRASH ",True,white)
    textGameplay3 = font.render("YOUR SPACESHIP WITH THE ENEMY",True,white)
    textGameplay4 = font.render("GAME IS OVER",True,white)
    
    gameDisplay.blit((textMovement),(300,250))
    gameDisplay.blit((textFight),(300,270))
    gameDisplay.blit((textLinegap),(300,290))
    gameDisplay.blit((textGameplay),(300,310))
    gameDisplay.blit((textGameplay2),(300,330))
    gameDisplay.blit((textGameplay3),(300,350))
    gameDisplay.blit((textGameplay4),(300,370))
    
def About():
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text1 = font.render("This game is developed by Nazmul Ahsan Shihab",True,white)
    text2 = font.render("for learning and fun purpose.",True,white)
    text3 = font.render("Images used might be subjected to copyright",True,white)

    gameDisplay.blit((text1),(300,400))
    gameDisplay.blit((text2),(300,420))
    gameDisplay.blit((text3),(300,440))  
    
    

def button(text,text_size, button_x,button_y,w,h,active_color,inactive_color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    if button_x+w>mouse[0]>button_x and button_y+h>mouse[1]>button_y:
        pygame.draw.rect(gameDisplay,active_color,(button_x,button_y,w,h))
        if click[0]==1 and action!=None:
            action()
            
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(button_x,button_y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",text_size)
    textSurf, textRect = text_objects(text,smallText, white)
    textRect.center = ((button_x+w/2),(button_y+h/2))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    global highscore
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(black)
        largeText1 = pygame.font.Font('freesansbold.ttf',50)
        TextSurf1, TextRect1 = text_objects('Space Impact',largeText1, red)
        TextRect1.center = (1.5*display_width/5, 1.4*display_height/5)
        gameDisplay.blit(TextSurf1,TextRect1)
        
        
        largeText2 = pygame.font.Font('freesansbold.ttf',20)
        TextSurf2, TextRect2 = text_objects('I&A Studio',largeText2, white)
        TextRect2.center = (1.1*display_width/5, display_height/5)
        gameDisplay.blit(TextSurf2,TextRect2)
        
        font = pygame.font.SysFont(None, 25)
        highscoreText = font.render("High Score: "+str(highscore), True, white)
        gameDisplay.blit(highscoreText,(display_width-200,10))
        
        
        button('New Game',20, 80,250,200,50,green,dark_green,game_loop)
        button('Instruction',20, 80,325,200,50,green,dark_green,instruction)
        button('About',20, 80,400,200,50,green,dark_green,About)
        button('Exit',20, 80,475,200,50,green,dark_green,pygame.quit)
   
        
        pygame.display.update()
        clock.tick(15)
        
def game_loop(): 
    xp = 0
    yp = display_height/2-playerSpaceship_width/2
    
    xe = display_width+500
    ye = random.randrange(0,(display_height-enemySpaceship_width))
    enemySpeed = 7
    yp_change = 0

    missile_launched = False
    missile_hit = False
    escapeCount=5
    score = 0
    level_up = 100
    global highscore
    
    gameExit = False
    gameDisplay.fill(black)
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    yp_change = 10
                elif event.key == pygame.K_UP:
                    yp_change = -10
                elif event.key == pygame.K_SPACE and missile_launched==False:
                    missile_launched = True
                    ym = yp+playerSpaceship_width/2
                    xm = xp
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yp_change = 0
        
        
        gameDisplay.fill(black)
        enemy_escaped(escapeCount)
        game_score(score)
        
        #enemy escape logic
        if escapeCount==0:
            high_score(score)
            game_over()
            
        #logic ends
        
        #player position logic
        yp+=yp_change
        if yp>display_height-playerSpaceship_width or yp<0:
            yp-=yp_change
        player_spaceship(xp,yp)        
        #logic ends

        #enemy moving logic        
        enemy_spaceship (xe,ye)
        xe-=enemySpeed
        #logic ends
        
        #player missile logic
        if missile_launched == True:          
            xm+=25
            missile(xm,ym)
            if xm+27>xe and ym<ye+enemySpaceship_width and ym+10>ye:
                missile_launched=False
                missile_hit = True
            if xm+27>display_width:
                missile_launched = False      
        
        #enemy position logic
        if xe<-100 or missile_hit == True:
            if xe<-100:
                escapeCount-=1             
            elif missile_hit == True:
                missile_hit = False
                score+=5
            xe = display_width+100
            ye = random.randrange(0,(display_height-enemySpaceship_width))
        #logic ends
            
        # crash logic    
        if xe<(xp+playerSpaceship_length):   
            if (yp < (ye+enemySpaceship_width)) and (yp+playerSpaceship_width)>ye:
                high_score(score)
                crash()               
        #logic ends
        
        # gradual speed increase
        if score >= level_up and enemySpeed <= 20:
            enemySpeed += 2
            level_up += 150
        #logic ends
            
        pygame.display.update()
        clock.tick(60)
    
game_intro()    
game_loop()
scoreReadingHandler.close()   
pygame.quit()
