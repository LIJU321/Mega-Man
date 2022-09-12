import pygame 
import sys
import os

#variables:
fps = 60
Red = (255,0,0)
Run = True
jumping= False
jump = 20
velocity = jump
gravity = 1
x_axis , y_axis = 150, 275



#initializing display
pygame.init()

#setting Display
SCREEN = pygame.display.set_mode((600,460))

#giving color to the screen
SCREEN.fill(Red)

#giving title for window
pygame.display.set_caption("Character_Jump")

#uploading image from directory
backround_img = pygame.image.load("Assets\BG.png")
standing_img = pygame.image.load("Assets\mega-man.png")
jumping_img = pygame.image.load("Assets\megaman_jump.png")

#resize image
backround_img_resized = pygame.transform.scale(backround_img,(100,100))
standing_img_resized = pygame.transform.scale(standing_img,(50,50))
jumping_img_resized = pygame.transform.scale(jumping_img,(60,60))

#creating a rect for character image:

Standing_Rect = standing_img_resized.get_rect(topright=(x_axis,y_axis))

Jumping_Rect = jumping_img_resized.get_rect(topright=(x_axis,y_axis))




#function to draw on display:
def draw_to_screen(y_movement):
    SCREEN.fill(Red)
    SCREEN.blit(backround_img,(0,0))
    if jumping==False:
        SCREEN.blit(standing_img_resized,(x_axis,y_axis))
    else:
     SCREEN.blit(jumping_img_resized,(x_axis,y_axis))

    pygame.display.update()
    



# main function game loop:
while Run:
    Clocks = pygame.time.Clock()
    Clocks.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Run = False
            sys.exit()
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_ESCAPE]:
            Run = False
            sys.exit()
    if keypress[pygame.K_SPACE]:
           jumping = True

    if jumping == True:
        y_axis-=velocity
        velocity-=gravity
    if velocity<-jump:
        jumping=False
        velocity=jump


    draw_to_screen(y_axis)

