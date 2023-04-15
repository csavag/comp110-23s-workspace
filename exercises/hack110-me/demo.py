import pygame
import sys
from random import randint

#starts window
pygame.init()
#constants to define window size and set FPS
HEIGHT = 600
WIDTH = 800
FPS = 30
BACKGROUND_COLOR = (53, 130, 27)
BACKGROUND_COLOR_2 = (27, 10, 53)
APPLE_COLOR = (200, 50, 50)
BASKET_COLOR = (189, 136, 66)
color = False
#apple: pygame.Rect = pygame.Rect(200, 400, 40, 40)
basket: pygame.Rect = pygame.Rect(WIDTH-110, HEIGHT-60, 100, 50)

apples: list[pygame.Rect] = []
current_apple = None

#adds apples randomly
for i in range(1,10):
    random_x: int = randint(0,WIDTH-100)
    random_y: int = randint(0,HEIGHT-100)
    apples.append(pygame.Rect(random_x, random_y, 20, 20))


#creates clock object to limit FPS
FramePerSec = pygame.time.Clock()

#create surface to draw objects on
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

holding_apple = False
while True:
    for event in pygame.event.get():
        #allows you to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for apple in apples:
                if(apple.collidepoint(pos)): #checks if a point is inside the rectangle (apple)
                    holding_apple = not holding_apple

    if holding_apple:
        pos = pygame.mouse.get_pos()
        if(pos[1] <= HEIGHT-50):
            current_apple.center = pos
        if(apple.colliderect(basket)): #checks if two rectangles are overlapping
            holding_apple = False

    #very clever method to switch the color each frame
    #if color:
    #    displaysurface.fill(BACKGROUND_COLOR)
    #    color = False
    #else:
    #    displaysurface.fill(BACKGROUND_COLOR_2)
    #    color = True
    displaysurface.fill(BACKGROUND_COLOR)
    pygame.draw.circle(displaysurface, APPLE_COLOR, apple.center, apple.width/2)
    pygame.draw.rect(displaysurface, BASKET_COLOR, basket)
    pygame.display.update()
    FramePerSec.tick(FPS)