import pygame, sys
from pygame.locals import *

class menu(object):
    
    def __init__(self, surf, background):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        self.buttonList = []
        self.textList = []
        self.backgroundOn = True
        self.bgImage = ''
        
        if background != 'none':
            self.bgImage = pygame.image.load(background).convert()
            self.bgImage = pygame.transform.scale(self.bgImage, (self.sWidth, self.sHeight))
        else:
            self.backgroundOn = False
    
    def makeButton(self, size, color, textColor, text, pos):
        self.buttonList.append(buttons(self.surf, size, color, textColor, text, pos))
    def makeText(self, size, text, pos, color):
        self.textList.append(texts(self.surf, size, text, pos, color))
    
    def displayScreen(self):
        for x in self.buttonList:
            x.displayButton()
        for x in self.textList:
            x.displayText()
    def displayBackground(self):
        if self.backgroundOn:
            self.surf.blit(self.bgImage, [0,0])        

class buttons(object):
    
    def __init__(self, surf, size, color, textColor, text, pos):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.size = size
        self.xPos = pos[0]
        self.yPos = pos[1]
        self.text = text
        
        self.color = color
        self.textColor = textColor
        
        self.textFont = pygame.font.SysFont("Sylfaen", 50)
        self.textPos = pos
        self.textSurf = self.textFont.render(text, True, self.textColor, None)
        self.textSurf = pygame.transform.scale(self.textSurf, (size[0], size[1]))
        
        self.rect = pygame.Rect(pos, size)
    
    def displayButton(self):
        pygame.draw.rect(self.surf, self.color, [self.xPos, self.yPos, self.size[0], self.size[1]])
        self.surf.blit(self.textSurf, self.textPos)
    
    def clicked(self, mouseXY):
        mouseRect = pygame.Rect(mouseXY[0], mouseXY[1], 5, 5)
        return mouseRect.colliderect(self.rect)
class texts(object):
    
    def __init__(self, surf, size, text, pos, color):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.active = True        
        self.titleFont = pygame.font.SysFont("Sylfaen", 120)
        self.text = text
        self.color = color
        self.size = size
        self.textSurf = self.titleFont.render(self.text, True, self.color, None)
        self.textSurf = pygame.transform.scale(self.textSurf, (self.size[0], self.size[1]))
        self.pos = pos        
    
    def displayText(self):
        if self.active:
            self.surf.blit(self.textSurf, self.pos)
    
    def changeText(self, newText):
        self.text = newText
        self.textSurf = self.titleFont.render(self.text, True, self.color, None)
        self.textSurf = pygame.transform.scale(self.textSurf, (self.size[0], self.size[1]))
        