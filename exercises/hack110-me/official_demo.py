import pygame
import sys
from random import randint

# starts window

pygame.init()

# constants to define window size and set FPS

HEIGHT = 450
WIDTH = 800
FPS = 60

# creates clock object to limit FPS

FramePerSec = pygame.time.Clock()

# create surface to draw objects on

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

apples: list[pygame.Rect] = []

# adds apples with randomized locations to list

for i in range(1,10):
    random_x: int = randint(0,WIDTH - 100)
    random_y: int = randint(0,HEIGHT -100)
    apples.append(pygame.Rect(random_x,random_y, 20, 20))

# basket to hold them

basket: pygame.Rect = pygame.Rect(WIDTH-110, HEIGHT-60, 100, 50)

# these track if/which apple we've got in hand

holding_apple: bool = False
current_apple: pygame.Rect

while True:
    for event in pygame.event.get():
        # this allows you to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # when the left mouse is clicked we check whether the mouse is over one of the apples
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for apple in apples:
                if(apple.collidepoint(pos)): # this method checks whether a point is inside the rectangle
                    holding_apple = not holding_apple
                    current_apple = apple
    if holding_apple:
        if(current_apple.colliderect(basket)): # this checks whether two rectangles are overlapping
            holding_apple = False
        current_apple.center = pygame.mouse.get_pos()

    displaysurface.fill((53, 130, 27))
    # these draw our surface on screen
    for apple in apples:
        pygame.draw.circle(displaysurface,(200, 50, 50), (apple.center), apple.width)
    pygame.draw.rect(displaysurface, (189, 136, 66), (basket))

    # update surface and move forward clock
    pygame.display.update()
    FramePerSec.tick(FPS)