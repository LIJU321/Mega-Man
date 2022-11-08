import pygame 
import sys

color = 0,255,0
fps = 60
Red = (255,0,0)
Run = True
jumping= False
jump = 30
velocity = jump
gravity = 1
x_axis , y_axis = 300, 635  
MOVE = 4
Right = False  
Left = False                    
pipex,pipey =400 ,530

pygame.init()
SCREEN = pygame.display.set_mode((800,800))
SCREEN.fill(Red)

pygame.display.set_caption("Character_Jump")

Pipe = pygame.image.load("PIPE.png")
backround_img = pygame.image.load("Background.png")
standing_img = pygame.image.load("mega-man.png")
jumping_img = pygame.image.load("megaman_jump.png")
BGX1 = 0
BG2 = backround_img
BGX2 = backround_img.get_width()

standing_img_resized = pygame.transform.scale(standing_img,(60,60))
jumping_img_resized = pygame.transform.scale(jumping_img,(69,69))
Pipe_resize =pygame.transform.scale(Pipe,(150,200))

Right_MOVE = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png")]
Left_MOVE = [pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png")]
walk_count = 0 

Right_move = pygame.transform.scale(Right_MOVE[0],(60,69))
Right_move1 = pygame.transform.scale(Right_MOVE[1],(60,69))
Right_move2 = pygame.transform.scale(Right_MOVE[2],(60,69))

R_move = [Right_move,Right_move1,Right_move2]

Left_move1 =pygame.transform.scale(Left_MOVE[0],(60,69))
Left_move2 =pygame.transform.scale(Left_MOVE[1],(60,69))
Left_move3 =pygame.transform.scale(Left_MOVE[2],(60,69))

L_move = [Left_move1,Left_move2,Left_move3]

def draw_to_screen(x_axis, y_axis):
    global collide
    collide = True
    global walk_count
    SCREEN.fill(Red)
    SCREEN.blit(backround_img,(BGX1,0))
    SCREEN.blit(BG2,(BGX2,0))
    SCREEN.blit(Pipe_resize,(pipex,pipey))
    if jumping==False:
        if Right == False:
            if Left == False:
                  SCREEN.blit(standing_img_resized,(x_axis,y_axis))
 
    if jumping== True:
     SCREEN.blit(jumping_img_resized,(x_axis,y_axis))

    if Right == True and jumping==False:
        SCREEN.blit(R_move[walk_count//1],(x_axis,y_axis-10))
        walk_count+=1
        if walk_count==len(R_move):
            walk_count=0
      
    if Left == True and jumping ==False:
        SCREEN.blit(L_move[walk_count//1],(x_axis,y_axis-10))
        walk_count+=1
        if walk_count==len(Left_MOVE):
            walk_count = 0
    pygame.display.update()

while Run:
    if Right == True:
        BGX1-=MOVE+4
        BGX2-=MOVE+4
        pipex-=MOVE+4
        if BGX1<-800 and BGX2<1:
            BGX1 = 0
            BGX2 = 800
            if pipex<-10:
                pipex =799  
  
    Clocks = pygame.time.Clock()
    Clocks.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Run = False
            pygame.quit()
            sys.exit()
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_ESCAPE]:
            Run = False
            pygame.quit()
            sys.exit()
    if keypress[pygame.K_SPACE]:
           jumping = True

    if keypress[pygame.K_d]:
        Right = True
        Left = False
        if Right == True:
          if x_axis<350:
           x_axis+= MOVE+4
    if keypress[pygame.K_d]==False:
           Right = False
        
    if keypress[pygame.K_a]:
        Left = True
        Right = False
        if Left == True:
          if x_axis>10:
            x_axis-= MOVE+4
    if keypress[pygame.K_a]==False:
        Left = False
    
    if x_axis+70 and y_axis+79<pipex and pipey+125:
        BGX1-=0
        BGX1-=0
        x_axis-=0

    if jumping == True:
        y_axis-=velocity            
        velocity-=gravity  
    if velocity<-jump:  
        jumping=False
        velocity=jump 
    draw_to_screen(x_axis,y_axis)
     


