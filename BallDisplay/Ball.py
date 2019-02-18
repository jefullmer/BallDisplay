#Ball.py
import pygame, sys
from pygame.locals import *
from random import randint

class ball(pygame.sprite.Sprite):
    
    def __init__(self, surf, nColors, choice):
        pygame.sprite.Sprite.__init__(self)        
        
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        self.image = pygame.image.load('block.png').convert()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.sWidth - self.rect.width)
        self.rect.y = randint(0, self.sHeight - self.rect.height)
        self.choice = choice
        self.colors = nColors
        if choice == 0:        
            self.speedX = randint(-5, 5)
            self.speedY = randint(-5, 5)
            if self.speedX == 0:
                self.speedX = 1
            if self.speedY == 0:
                self.speedY = 1
        if choice == 1:
            for x in range(125):
                for y in range(125):
                    self.image.set_at((x,y), self.colors[self.rect.x + x][self.rect.y + y])            
        
        
        
        
    def update(self):
        if self.choice == 0:
            for x in range(50):
                for y in range(50):
                    self.image.set_at((x,y), self.colors[self.rect.x + x][self.rect.y + y])
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            if self.rect.x < 0 or self.rect.right > self.sWidth:
                self.speedX = -self.speedX
            if self.rect.y < 0 or self.rect.bottom > self.sHeight:
                self.speedY = -self.speedY
            
        self.surf.blit(self.image, self.rect)