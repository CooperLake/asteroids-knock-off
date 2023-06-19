# Example file showing a circle moving on screen
import pygame
import math
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0
pygame.mouse.set_visible(0)
asteroids_array = []
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

screen_width = 1280
screen_height = 720
player_size = 30
font = pygame.font.Font('ARCADE_N.TTF', 46)
win_font = pygame.font.Font('ARCADE_N.TTF', 56)
reset_time = 0

#---------------------------Declarations-----------------------------------#

    #------------------CLASSES------------------------------#

class asteroid:
    def __init__(self, x_coord, y_coord, speed, deviation, size, offset):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed
        self.size = size
        self.deviation = deviation
        self.offset = offset

#---------------------METHODS-------------------------------#

def send_asteroid():
    curr_size = random.randint(100, 140)
    curr_asteroid = asteroid(-curr_size, random.randint(0, screen_height), random.randint(15, 25),random.randint(-3,3), curr_size, random.randint(2000, 25000))
    asteroids_array.append(curr_asteroid)

def maintain_asteroid(asteroid):
    curr_ast = pygame.draw.circle(screen, "grey", (asteroid.x_coord, asteroid.y_coord), asteroid.size)
    asteroid.x_coord += asteroid.speed
    asteroid.y_coord += asteroid.deviation

def set_difficulty(rating):
    for x in range(rating):
        send_asteroid()

def collision(rleft, rtop, width, height,  
            center_x, center_y, radius): 
    

    
    rright, rbottom = rleft + width/2, rtop + height/2

    
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False 

    
    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  

    
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True  

    return False 

    #-------------------execution loop----------------------------#

def main():

    pygame.mouse.set_visible(0)
    alive = True
    dead = False
    winner = False
    x = screen_width // 2
    y = screen_height // 2
    charge = 300
    
    global reset_time

    set_difficulty(100)
    

    while alive:

        if charge < 400:
            charge += 2
            

        curr_time = pygame.time.get_ticks() - reset_time
        if curr_time > 30000:
            pygame.mouse.set_visible(100)
            alive = False
            winner = True
        
        screen.fill("black")
        
        pygame.draw.rect(screen, 'blue', (screen_width - charge - 20, 20, charge, 20))
        pygame.draw.rect(screen, "white", (x, y, player_size, player_size))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w] and y > 0:
                y -= 10
            if keys[pygame.K_s] and y < (screen_height - player_size):
                y += 10
            if keys[pygame.K_a] and x > 0:
                x -= 10
            if keys[pygame.K_d] and x < (screen_width - player_size):
                x += 10 
        else:
            if keys[pygame.K_w] and y > 0:
                y -= 5
            if keys[pygame.K_s] and y < (screen_height - player_size):
                y += 5
            if keys[pygame.K_a] and x > 0:
                x -= 5
            if keys[pygame.K_d] and x < (screen_width - player_size):
                x += 5

        if keys[pygame.K_SPACE] and charge == 400:
            pygame.draw.rect(screen, 'yellow', (0, y+5, x, 20))
            for asteroid in asteroids_array:
                if asteroid.x_coord > 0 and asteroid.x_coord < x and not (asteroid.y_coord - asteroid.size) > y + 25 and not (asteroid.y_coord + asteroid.size) < y + 5:
                    asteroids_array.remove(asteroid)
            charge = 0



        for asteroid in asteroids_array:
            if collision(x, y, player_size, player_size, asteroid.x_coord, asteroid.y_coord, asteroid.size):
                alive = False
                dead = True
                pygame.mouse.set_visible(100)
            if curr_time >= asteroid.offset:
                maintain_asteroid(asteroid)
                
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = False
                alive = False
                pygame.display.quit()
                pygame.quit()
        

    while dead:

        
        button_color = 'black'
        curx, cury = pygame.mouse.get_pos()
        mouse_over_bool = curx > (screen_width / 2 - 250) and curx < (screen_width / 2 + 250) and cury < (screen_height / 2 + 75) and cury > (screen_height / 2 - 75)

        text = font.render('Try Again', False, 'white', None)
        text_rect = text.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)

        if mouse_over_bool:
            button_color = 'grey'
                                                                                                                            

        button = pygame.Rect(screen_width / 2 - 250, screen_height / 2 - 75, 500, 150)
        screen.fill("red")
        pygame.draw.rect(screen, button_color, button)
        

        text = font.render('Try Again', False, 'white', None)
        text_rect = text.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)

        screen.blit(text, text_rect)

        
        keys = pygame.key.get_pressed()
        

        if (pygame.mouse.get_pressed()[0] and mouse_over_bool) or keys[pygame.K_RETURN]:
            reset_time = pygame.time.get_ticks()
            print(reset_time)
            asteroids_array.clear()
            main()

        curr_time = pygame.time.get_ticks()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = False
                alive = False
                pygame.display.quit()
                pygame.quit()
    
    while winner:

        button_color = 'black'
        curx, cury = pygame.mouse.get_pos()
        mouse_over_bool = curx > (screen_width / 2 - 250) and curx < (screen_width / 2 + 250) and cury < (screen_height / 2 + 75) and cury > (screen_height / 2 - 75)

        winner_text = win_font.render('YOU WIN!!!', False, 'black', None)
        winner_text_rect = winner_text.get_rect()
        winner_text_rect.center = (screen_width / 2, screen_height / 4)

        text = font.render('Play Again', False, 'white', None)
        text_rect = text.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)

        if mouse_over_bool:
            button_color = 'grey'

                                                                                                                            

        button = pygame.Rect(screen_width / 2 - 250, screen_height / 2 - 75, 500, 150)
        screen.fill("green")
        pygame.draw.rect(screen, button_color, button)
        


        screen.blit(winner_text, winner_text_rect)
        screen.blit(text, text_rect)


        keys = pygame.key.get_pressed()


        if (pygame.mouse.get_pressed()[0] and mouse_over_bool) or keys[pygame.K_RETURN]:
            reset_time = pygame.time.get_ticks()
            print(reset_time)
            asteroids_array.clear()
            main()

        curr_time = pygame.time.get_ticks()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = False
                alive = False
                pygame.display.quit()
                pygame.quit()
    

main()


