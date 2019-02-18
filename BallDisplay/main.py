import pygame, sys
import threading
from pygame.locals import *

from Ball import ball
from menuClass import menu

pygame.init()

screenW = 1020
screenH = 800
surface = pygame.display.set_mode((screenW, screenH), FULLSCREEN)
BGColor = (25, 25, 25)
surface.fill(BGColor)

clock = pygame.time.Clock()
FPS = 60

moses = pygame.image.load('moses.jpg').convert()
moses = pygame.transform.scale(moses, (screenW + 6, screenH + 6))

bapt = pygame.image.load('baptize.jpg').convert()
bapt = pygame.transform.scale(bapt, (screenW+6, screenH+6))

benj = pygame.image.load('benjamin.jpg').convert()
benj = pygame.transform.scale(benj, (screenW+6, screenH+6))

abin = pygame.image.load('abinadi.jpg').convert()
abin = pygame.transform.scale(abin, (screenW+6, screenH+6))

door = pygame.image.load('door.jpg').convert()
door = pygame.transform.scale(door, (screenW+6, screenH+6))

dream = pygame.image.load('dream.jpg').convert()
dream = pygame.transform.scale(dream, (screenW+6, screenH+6))

fish = pygame.image.load('fish.jpg').convert()
fish = pygame.transform.scale(fish, (screenW+6, screenH+6))

warr = pygame.image.load('warriors.jpg').convert()
warr = pygame.transform.scale(warr, (screenW+6, screenH+6))

water = pygame.image.load('water.jpg').convert()
water = pygame.transform.scale(water, (screenW+6, screenH+6))


def getXY(image):
    colors = []
    for x in range(screenW + 6):
        colors.append([])
        for y in range(screenH + 6):
            colors[x].append(image.get_at((x,y)))
            
    return colors

imgCol = []
imgCol.append(getXY(moses))
imgCol.append(getXY(bapt))
imgCol.append(getXY(benj))
imgCol.append(getXY(abin))
imgCol.append(getXY(door))
imgCol.append(getXY(dream))
imgCol.append(getXY(fish))
imgCol.append(getXY(warr))
imgCol.append(getXY(water))

imgs = []
imgs.append(moses)
imgs.append(bapt)
imgs.append(benj)
imgs.append(abin)
imgs.append(door)
imgs.append(dream)
imgs.append(fish)
imgs.append(warr)
imgs.append(water)


balls = []

totalScore = menu(surface, 'none')
totalScore.makeText((int(screenW * .125),int(screenH * .04166)), 'Total: 0', (int(screenW * .1875), int(screenH * .91666)), (200, 200, 200))



def main():
    canNext = None
    currentImg = 0
    total = 0
    while True:
        clock.tick(FPS)
        surface.fill(BGColor)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i] and keys[pygame.K_n] and keys[pygame.K_d]:
            balls.clear()        
            canNext = True
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
            if event.type == KEYUP:
                if event.key == pygame.K_SPACE and canNext != True:
                    balls.append(ball(surface, imgCol[currentImg]))
                    total += 1
                    totalScore.textList[0].changeText(('Total: ' + str(total)))
                if event.key == pygame.K_BACKSPACE and len(balls) > 0 and canNext != True:
                    balls.pop()                   
                    total -= 1
                    totalScore.textList[0].changeText(('Total: ' + str(total)))
                if event.key == pygame.K_RETURN:
                    canNext = False
                    currentImg += 1
                    if currentImg > len(imgs) - 1:
                        currentImg = 0
                                   
       
            
        for b in balls:
            b.update()
        
        if canNext == True:
            surface.blit(imgs[currentImg], (0,0))
        
        totalScore.displayScreen()
        pygame.display.update()
        

main()