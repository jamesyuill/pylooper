import pygame
from sys import exit
from sample import Sample

width = 800
height = 400
fps = 60
beats = 4
bpm = 120
looping = False
frames = 0

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Looper')
clock = pygame.time.Clock()





kick = Sample('kick')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # Call the on_mouse_button_down() function
            if kick.button_collided(event.pos):
                print("Button clicked!")
                looping = True

    
    kick.display(screen)

    if looping and frames % 60 == 0:
        kick.play_sound()

    frames += 1
    pygame.display.update()
    clock.tick(fps)

