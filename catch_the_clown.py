import pygame, random

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Catch The Clown')

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Set Game Values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5


score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([1, -1])
clown_dy = random.choice([1, -1])

#Set Colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

#Set Fonts
font = pygame.font.Font('Franxurter.ttf', 32)

#Set Text
score_text = font.render('Score: ' + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH-50, 10)

title_text = font.render('Catch The Clown', True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

lives_text = font.render('Lives: ' + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render('GAMEOVER', True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Click anywhere to play again', True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)



#Set Sounds and Music
click_sound = pygame.mixer.Sound('click_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')


#Set Images
clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

#The main game loop
pygame.mixer.music.play(-1, 0.0)


running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        #a click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #the clown was clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION

                #move the clown in a new direction
                
                previous_dx = clown_dx
                previous_dy = clown_dy

                while(previous_dx == clown_dx and previous_dy == clown_dy):        
                    clown_dx = random.choice([1, -1])
                    clown_dy = random.choice([1, -1])
            #We missed the clown
            else:
                miss_sound.play()
                player_lives -= 1

    
    #move the clown
    clown_rect.x += clown_dx*clown_velocity
    clown_rect.y += clown_dy*clown_velocity

    #bounce the clown off the edges of this display
    if clown_rect.left <= 0:
        clown_dx = -1*clown_dx
        clown_rect.left = 0
    if clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1*clown_dx
        clown_rect.right = WINDOW_WIDTH
    if clown_rect.top <= 0:
        clown_dy = -1*clown_dy
        clown_rect.top = 0
    if clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1*clown_dy
        clown_rect.bottom = WINDOW_HEIGHT


    #print(clown_rect.left, clown_rect.right, clown_rect.top, clown_rect.bottom)
    
    #Get a list of all keys currently being pressed down
    #keys = pygame.key.get_pressed()   
    

    #Move the dragon continously
    #if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
    #    dragon_rect.x -= PLAYER_VELOCITY
    #if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
    #    dragon_rect.x += PLAYER_VELOCITY
    #if keys[pygame.K_UP] and player_rect.top > 64:
    #    player_rect.y -= PLAYER_VELOCITY
    #if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
    #    player_rect.y += PLAYER_VELOCITY

    #Move the coin
    #if coin_rect.x < 0:
        #player missed coin
    #    player_lives -= 1
    #    miss_sound.play()
        #place coin off the end of the screen again
    #    coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
    #    coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    #else:
    #    coin_rect.x -= coin_velocity
        #move hte coint
    #Check for collison between player and coin
    #if player_rect.colliderect(coin_rect):
    #    score += 1
    #    coin_sound.play()
    #    coin_velocity += COIN_ACCELERATION
    #    coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
    #    coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    #update HUD
    #score_text = font.render('Score: ' + str(score), True, GREEN, DARKGREEN)
    #lives_text = font.render('Lives: ' + str(player_lives), True, GREEN, DARKGREEN)


    #if player_lives == 0:
    #    display_surface.blit(game_over_text, game_over_rect)
    #    display_surface.blit(continue_text, continue_rect)
    #    pygame.display.update()

        #Pause game until player presses a key, then reset
    #    pygame.mixer.music.stop()
    #    is_paused = True
    #    while is_paused:
    #        for event in pygame.event.get():
                #player wants to play again
    #            if event.type == pygame.KEYDOWN:
    #                score = 0
    #                player_lives = PLAYER_STARTING_LIVES
    #                player_rect.y = WINDOW_HEIGHT // 2
    #                coin_velocity = COIN_STARTING_VELOCITY
    #                pygame.mixer.music.play(-1, 0.0)
    #                is_paused = False
                #player wants to quit
    #            if event.type == pygame.QUIT:
    #                is_paused = False
    #                running = False


    #Fill the display surface to cover old images
    #display_surface.fill((0,0,0))

    #Draw rectangles to represent rectangles
    #pygame.draw.rect(display_surface, (0,255,0), dragon_rect, 1)
    #pygame.draw.rect(display_surface, (255,0,0), coin_rect, 1)
    

    #Blit background
    display_surface.blit(background_image, background_rect)

    #Blit the HUD to the screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

    #blit assets
    display_surface.blit(clown_image, clown_rect)
    
    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()