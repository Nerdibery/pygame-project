#this is basically a tutorial on how to use pygame library. it has 3 sections 
#constructing a window for display
#game loop code - main body of code
#event handler - lets program shut down

#step one
import pygame #import the module into your code
pygame.init() #initializing the library

#section one: making the window
#making window dimentions and giving them a variable
WINDOW_WIDTH = 800 #measurement is in pixels
WINDOW_HEIGHTS = 600#constants

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHTS))#method for creating screen. pass arguments

player =pygame.Rect((300,250,50,50))# takes four arguments x-coordinate,y-coordinate,width,height

run = True #variable that lets while loop run

while run:
    #game loop

    screen.fill((0,0,0))#prevents the rectangle from leaving a trail, screen is black because rgb values are all zero

    #constructs the game character
    pygame.draw.rect(screen,(255,0,255),player)#variable order - screen name,colour- this follows rgb(select range from o to 255),the rectangle
    
    #game controls
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:#checks if A key is pressed
        player.move_ip(1,0)#movement in x and y direction is passed - this moves to left because x is changing and positive
    elif key[pygame.K_d] == True:
        player.move_ip(-1,0)#moves to the right, y is constant
    elif key[pygame.K_w] == True:
        player.move_ip(0,1)#upward movement
    elif key[pygame.K_s] == True:
        player.move_ip(0,-1)#downward movement
    
    
    
    #event handler
    for event in pygame.event.get():#when an action is detected,
        if event.type ==pygame.QUIT:# in this specific case when the x on the window is clicked, program stops
            run = False# when set to false the loop shuts down
    pygame.display.update()#must be present to refresh screen when changes are made


pygame.quit()#when loop shuts down the program stops