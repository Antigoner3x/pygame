#new graphics window

#from livewires import games,color
import pygame
from pygame.locals import *
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0,0,0

screen = pygame.display.set_mode(size)
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
#games.init(screen_width = 640, screen_height =480, fps = 50)

#background image
#wall_image = games.load_image("hud.jpg", transparent = False)
#Set background
#games.screen.background = wall_image

#Set radar

#games.screen.mainloop()
