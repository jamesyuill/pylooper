import pygame

class Sample:
    def __init__(self, name):
        self.name = name
        self.button_surface = pygame.Surface((150,50))
        self.button_surface.fill('red')
        self.font = pygame.font.Font(None,24)
        self.text = self.font.render(self.name,True,(0,0,0))
        self.text_rect = self.text.get_rect(center=(self.button_surface.get_width()/2,self.button_surface.get_height()/2))
        self.button_rect = pygame.Rect(125,125,150,50)
        self.sound = pygame.mixer.Sound('basketball.mp3')

    def play_sound(self):
        self.sound.play()


    def display(self, display_surface):
        self.button_surface.blit(self.text, self.text_rect)
        display_surface.blit(self.button_surface,(self.button_rect.x,self.button_rect.y))



    def button_collided(self, eventPos):
        return self.button_rect.collidepoint(eventPos)