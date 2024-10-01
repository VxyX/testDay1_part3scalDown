import pygame
import math

banyakRect = 10 #more than 35 gets too big and make app crash
# 33 repeat = 1615901 radius -> 34 repeat = 2285234 radius

# Initializing Pygame
pygame.init()
# clock = pygame.time.Clock()
 
# Initializing surface
max_width = 600
max_height = 400
screen = pygame.display.set_mode((max_width,max_height))

scroll_x = 4700 # initial view coordinate
scroll_y = 4800

# Initializing Color
color = (0,0,255)

running = True


initX = 5000 # center
initY = 5000
radius = 100 # initial radius
width = 2*radius
height = 2*radius
border = 2

created = 0

rect_surface = pygame.Surface((20000, 20000))
rect_surface.fill((255, 255, 255))
font = pygame.font.SysFont('Arial', 12)

while running:
    # clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Continuous scrolling based on mouse movement
        # if event.type == pygame.MOUSEMOTION:
        #     if event.buttons[0]:  # Left mouse button pressed
        #         scroll_x += event.rel[0]
        #         scroll_y += event.rel[1]
                
    if (created < banyakRect):
            # print(round(radius, 2))
                   
            pygame.draw.circle(rect_surface, color, (initX , initY), radius - border, border)

            x = math.floor(radius * math.sin(math.radians(45)))
            y = math.floor(radius * math.cos(math.radians(45)))

            width = math.sqrt((((2*radius) * (2*radius)) / 2)) #lupa radius itu jari jari... 

            height = width

            pygame.draw.rect(rect_surface, color, (initX-x, initY-y, width, height), border)
            # pygame.draw.rect(rect_surface, color, (x, y, width, height), border)

            
            created += 1

            text_surface = font.render('{}'.format(created), True, color)
            rect_surface.blit(text_surface, (initX + radius + 1, initY))

            # radius = math.sqrt(pow(radius, 2) * 2) + 2*border
            # width = 2*radius
            # height = 2*radius
            radius = x

            print(created)

    screen.blit(rect_surface, (-scroll_x, -scroll_y))
    pygame.display.update()

