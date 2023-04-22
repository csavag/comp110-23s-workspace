import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load(image_path)

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move_left(self):
        self.velocity = (-1, self.velocity[1])
    
    def move_right(self):
        self.velocity = (1, self.velocity[1])



pygame.init()
window_size = (640,480)
window = pygame.display.set_mode(window_size)
player = Player(320,240,0,0, "C:/Users/colin/OneDrive/Pictures/100px-202_WatchittCard.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
    player.update()
    window.fill((255,255,255))
    player.draw(window)
    pygame.display.update()
