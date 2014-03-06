import pygame, sys
from pygame.locals import *
from utils import *

class Static:
    def __init__(self, fx=0, fy=0, imagepath=''):
        #position
        self.x, self.y = fx, fy
        #image
        self.surfaceObj = pygame.image.load(imagepath)
        #center point
        self.cx, self.cy = fx+int((self.surfaceObj.get_width())/2), fy+int((self.surfaceObj.get_height())/2)

    def draw(self, surf):
        rect = self.surfaceObj.get_rect()
        rect.topleft = self.x, self.y
        surf.blit(self.surfaceObj, rect)
        