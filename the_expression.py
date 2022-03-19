import pygame
import numpy as np
import argparse

from Game_Data.UI import Bubble_Object

def setup():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    return screen, clock

def draw(screen, clock, FPS, bubble_list):

    clock.tick(FPS)
    screen.blit(background, (0,0))
    
    for bubble_idx in range(len(bubble_list)):
        if bubble_list[bubble_idx].opacity != 0:

            if (pygame.time.get_ticks() %5 == 0):
                bubble_list[bubble_idx].update()
            bubble_list[bubble_idx].draw(screen = screen)
            print(bubble_list[bubble_idx].velocity)
            #print(bubble_list[bubble_idx].x, bubble_list[bubble_idx].y)
    pygame.display.update()
    return 0


if __name__ == "__main__":
    
    exit = False
    FPS = 120

    screen, clock = setup()
    clock.tick(FPS)

    background = pygame.image.load('Game_Data/background/blue.png')
    bubble_list = []
    for i in range(50):
        bubble = Bubble_Object(x = np.random.randint(0,800), y = np.random.randint(0,600), r = np.random.randint(5,20), color=(10,240,240), velocity=np.random.randint(-50,50,(2)))
        bubble_list.append(bubble)

    while (not(exit)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit = True
        draw(screen, clock, FPS, bubble_list)

    pygame.quit()
    quit
