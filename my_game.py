import pygame 
import random #Imports modules

pygame.init() #Initializes pygame


screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))   #Sets the screen size

player = pygame.image.load("image.png")  #Loads images
enemy = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.jpg")

image_height = player.get_height()  #Specifys heights and widths of each image
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


playerXPosition = 100  # Places the image at a specific position
playerYPosition = 20


enemyXPosition =  screen_width   # Places the enemy image at a position
enemyYPosition =  random.randint(0, screen_height - enemy_height)

prizeXPosition =  screen_width  # Places the prize image at a position
prizeYPosition =  random.randint(0, screen_height - prize_height)


keyUp= False
keyDown = False
iCount = 1   # Sets some variables


while 1:  # Starts the loop of the game
    
    screen.fill(0) # Clears the screen
    screen.blit(player, (playerXPosition, playerYPosition))  # Draws the image on the screen at the position
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip() # Updates the images on the screen

    
    for event in pygame.event.get():  # Loops the events 
    
        
        if event.type == pygame.QUIT:  # If the player quits the game it will stop the loop and exit
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:  # Checks if the player clicked a key
        
              
            if event.key == pygame.K_UP: # Did the player click the up key
                keyUp = True

            if event.key == pygame.K_DOWN:  # Did the player click the down key
                keyDown = True
        
        
        if event.type == pygame.KEYUP:  # Checks if the user stopped clicking a key
        
            
            if event.key == pygame.K_UP:  # Did the player stop clicking the up key
                keyUp = False
            if event.key == pygame.K_DOWN:  # Did the player stop clicking the down key
                keyDown = False
             
    
    if keyUp == True:  # is the upkey boolean true
        if playerYPosition > 0 : # moves image up
            playerYPosition -= 2
    if keyDown == True:  # is the downkey boolean true
        if playerYPosition < screen_height - image_height:  # Moves the image down
            playerYPosition += 2  
    
    
    playerBox = pygame.Rect(player.get_rect())  # Specifies the images boundries
    

    
    playerBox.top = playerYPosition  # Updates the players image 
    playerBox.left = playerXPosition
    

    
    enemyBox = pygame.Rect(enemy.get_rect())  # Specifies the enemys boundries
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    prizeBox = pygame.Rect(prize.get_rect())  # Specifies the prize boundries
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    

    
    if playerBox.colliderect(enemyBox):  #Did the player collide with the enemy
     
        print("You lose!")  # Stops the program and tells the user they lost
               
        pygame.quit()
        exit(0)

    
    if enemyXPosition < 0 - enemy_width:  # If the enemy hit the side of the screen it will reset the enemy

        iCount +=1  
        
        enemyXPosition =  screen_width  
        enemyYPosition =  random.randint(0, screen_height - enemy_height)


    if iCount > 10 :  # Starts sending the prize to the user so they can win
       prizeXPosition -= 1



    if prizeXPosition < 0 - prize_width:  # If the prize hits the back then it will reset

        
        prizeXPosition =  screen_width
        prizeYPosition =  random.randint(0, screen_height - prize_height)

   
    if playerBox.colliderect(prizeBox):  #If the player collides with the box then they win
        
        print("You WIN!")      
        
        pygame.quit()
        exit(0)     
  

    if iCount > 4 :  # Makes a max speed for the enemy
        enemyXPosition -= 2

    else : # Makes the enemy speed up
        
        enemyXPosition -= iCount/2
    
  
