import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Character Jump Animation")

fps = 60
Run = True
COLOR = (100,160,200) 

Background = pygame.image.load("BG.jpg")
BG =  pygame.transform.scale(Background,(800,400))

Start_Button = pygame.image.load("start_btn.png")
Exit_Button = pygame.image.load("exit_btn.png")

Start_button_img = pygame.transform.scale(Start_Button,(100,70))
Exit_button_img = pygame.transform.scale(Exit_Button,(100,70))

class Button: 
    def __init__(self,X,Y,image):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.topleft = (X,Y)
        self.clicked = False
    
    def draw(self):
          action = False
          pos = pygame.mouse.get_pos()
          if self.rect.collidepoint(pos):  
              if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  
                    self.clicked = True
                    action =True
              if pygame.mouse.get_pressed()[0]==0:
                  self.clicked = False
                  action = False
          screen.blit(self.image,(self.rect.x,self.rect.y,)) 
          return action
          
start = Button(230,150,Start_button_img,) 
exit = Button(480,150,Exit_button_img,)
                                       
while Run:  
    screen.fill((COLOR)) 
    screen.blit(BG,(0,0)) 
    if start.draw() ==True:
        print("START")
        pygame.quit()
        import GAME
        pygame.quit()
        sys.exit()
      
    if exit.draw() ==True:
        print("EXIT")
        Run = False
        pygame.quit() 
        sys.exit()
      
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
    pygame.display.update()
     
