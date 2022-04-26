import pygame
import os
import sys

try:
    FPS=60
    C = (255,0,0)

    pygame.init()
    SCREEN = pygame.display.set_mode(size=(570,(500)))#width and height
    pygame.display.set_caption("megaman")
    
    
    X_POSITION = 100
    Y_POSITION = 409
    Y_GRAVITY = 1
    JUMP_HEIGHT = 20
    Y_VELOCITY = JUMP_HEIGHT
    jumping = False

    BACK_IMG = pygame.image.load("Assets\megaman_stage.png")
    MEGAMAN = pygame.image.load("Assets\mega-man.png")
    MEGAMAN_JUMP = pygame.image.load("Assets\megaman_jump.png")

    #scale and resize
    MEGAMAN_SC = pygame.transform.scale(MEGAMAN,(50,50))
    MEGAMAN_JUMP_SC =pygame.transform.scale(MEGAMAN_JUMP,(60,50))
    
    #backround
    #game loop
   
    while True:   
        SCREEN.fill(C)
        CLOCK = pygame.time.Clock()
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN: #ONLY ONE PRESS AT A TIME
                if event.key==pygame.K_ESCAPE:
                        sys.exit()
                        pygame.QUIT

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
             jumping = True

        SCREEN.blit(BACK_IMG,(0,0))
        
        if jumping==True:
                Y_POSITION -=Y_VELOCITY 
                Y_VELOCITY -= Y_GRAVITY 
                if Y_VELOCITY < -JUMP_HEIGHT:
                    jumping = False   
                    Y_VELOCITY  = JUMP_HEIGHT  
                Megaman_jumping_rect = MEGAMAN_JUMP_SC.get_rect(center=(X_POSITION , Y_POSITION)) 
                SCREEN.blit(MEGAMAN_JUMP_SC,Megaman_jumping_rect)
        else:
            Megaman_standing_rect = MEGAMAN_SC.get_rect(center=(X_POSITION , Y_POSITION))
            SCREEN.blit(MEGAMAN_SC,Megaman_standing_rect)
        
 

        pygame.display.update()

except Exception as e:
    print(e)