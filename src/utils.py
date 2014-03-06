import pygame, os
import math

pygame.init()

SCRWIDTH, SCRHEIGHT = 800, 600

homepath = "C:\\Users\\Krzysztof\\Dropbox\\fishy\\data\\"

freesansbold_font = pygame.font.Font('freesansbold.ttf', 32)

redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
    
def normalize(vect):
        mag = math.sqrt(sum(vect[i]*vect[i] for i in range(len(vect))))
        return [vect[i]/mag  for i in range(len(vect))]
        
def show_fps(screen, clock):
    fps = str(clock.get_fps())[:-8]
    fpsSurfaceObj = freesansbold_font.render(fps, False, whiteColor)
    fpsRectobj = fpsSurfaceObj.get_rect()
    fpsRectobj.topleft = (0, 0)
    screen.blit(fpsSurfaceObj, fpsRectobj)
    
