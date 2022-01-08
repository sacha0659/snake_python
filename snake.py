
import random
import pygame
ecran = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake")

loop = True
i = 0

snake_position_x = 300
snake_position_y = 300

snake_direction_x = 0
snake_direction_y = 0

pomme_position_x = random.randrange(190,600,10)
pomme_position_y = random.randrange(190,600,10)

snake_position = []

snake_size = 1

score  = 0

Clock = pygame.time.Clock()

chance = random.randint(1,10)

pygame.font.init()
myfont = pygame.font.SysFont('Lato', 40)
mysmallerfont = pygame.font.SysFont('Lato', 30)


# Boucle pour faire tourner le jeu 
while loop:
    ecran.fill((0,0,0))
    
 
    for event in pygame.event.get():
        # Gestion des touches
        if event.type == pygame.KEYDOWN:  
            
            if event.key == pygame.K_RIGHT: 
                snake_direction_x = 10
                snake_direction_y = 0
            if event.key == pygame.K_LEFT:
                snake_direction_x = -10
                snake_direction_y = 0

            if event.key == pygame.K_UP:
                snake_direction_x = 0
                snake_direction_y = -10

            if event.key == pygame.K_DOWN:
                snake_direction_x = 0
                snake_direction_y = 10
            
        if event.type == pygame.QUIT:
            loop = False
    # application de la direction au serpent 
    snake_position_x += snake_direction_x
    snake_position_y += snake_direction_y

    # -------creation du rectangle serpent
    pygame.draw.rect(ecran,(0,255,0),(snake_position_x,snake_position_y,10,10))

    pygame.draw.rect(ecran,(255,255,255),(150,150,500,500),2)

    if snake_position_x <= 150 or snake_position_x >= 650 or snake_position_y <=100 or snake_position_y >=650:
        loop = False


    
    # ------ Pomme 
    
    if chance < 7:
        pygame.draw.rect(ecran,(255,0,0),(pomme_position_x,pomme_position_y,10,10))
    if chance > 7:
        pygame.draw.rect(ecran,(255,255,0),(pomme_position_x,pomme_position_y,10,10))
    if chance == 7:
        pygame.draw.rect(ecran,(0,0,255),(pomme_position_x,pomme_position_y,10,10))

    if pomme_position_x == snake_position_x and pomme_position_y == snake_position_y:
        pomme_position_x = random.randrange(190,600,10)
        pomme_position_y = random.randrange(190,600,10)
        # gestion des differentes pommes 
        if chance > 7:
            snake_size += 20
            score +=2
            print(score)
        if chance < 7:
            snake_size += 1
            score +=1
            print(score)
        if chance == 7:
            if snake_size > 15:
                snake_size -= 15
                i=0
                while i < 15 :
                    snake_position.pop(0)
                    i += 1
                
                
            score +=1
            print(score)
        chance = random.randint(1,10)

    # agrandissement du serpent 
    snake_head_position = []
    snake_head_position.append(snake_position_x)
    snake_head_position.append(snake_position_y)

    snake_position.append(snake_head_position)
    
    if len(snake_position) > snake_size:
        snake_position.pop(0)

    for snake_parts in snake_position:
        pygame.draw.rect(ecran,(0,255,0),(snake_parts[0],snake_parts[1],10,10))
    # si le serpent rentre en collision avec lui meme
    for snake_parts in snake_position[:-1]:
        if snake_head_position == snake_parts:
            loop = False
    
   
    #zone de texte 
    text = myfont.render('score : {}'.format(str(score)), False, (255, 255, 0))
    ecran.blit(text,(40,20))
    pygame.draw.rect(ecran,(255,0,0),(40,670,10,10))
    legend1 = mysmallerfont.render('1pt and 1 snake', False, (255, 255, 0))
    ecran.blit(legend1,(80,670))
    pygame.draw.rect(ecran,(255,255,0),(40,720,10,10))
    legend2 = mysmallerfont.render('2pts and 20 snakes', False, (255, 255, 0))
    ecran.blit(legend2,(80,720))
    pygame.draw.rect(ecran,(0,0,255),(40,770,10,10))
    legend3 = mysmallerfont.render('1pt and -15 snakes', False, (255, 255, 0))
    ecran.blit(legend3,(80,770))
    # gestion des fps
    Clock.tick(13+score)

    
    pygame.display.flip()

pygame.quit()
