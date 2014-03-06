import pygame
import sys
import tiledtmxloader
from pygame.locals import *
from Dynamic import *
from Static import *
from Domain import *
from WorldMap import *

try:
    import _path
except:
    print("_path import failed")

import utils

fpsClock = pygame.time.Clock()

ticks_per_second = 25
skip_ticks = 1000/ticks_per_second
max_frameskip = 5

next_game_tick = pygame.time.get_ticks()
loops = 0
interpolation = 0

windowSurfaceObj = pygame.display.set_mode((SCRWIDTH, SCRHEIGHT))
pygame.display.set_caption('Game')

mousex, mousey = 0, 0

domain = Domain(100, (SCRWIDTH/2, SCRHEIGHT/2))
domain.v_scal = 10

for i in range(5):
    dyna = Dynamic(304, 224, homepath + 'bot.png')
    dyna.vx = randint(-1, 1)
    dyna.vy = randint(-1, 1)
    if dyna.vx == 0 and dyna.vy == 0:
        dyna.vx = 1
    dyna.normalize()
    #dyna.point_to_vel_vector()
    dyna.v_scal = randint(10, 15)
    domain.add_fish(dyna)
    
worldMap = WorldMap("map2_tiles_only.tmx")

running = True

clock = pygame.time.Clock()

fps_drawing = True

# set up timer for fps printing
pygame.time.set_timer(pygame.USEREVENT, 1000)

while running:
    clock.tick(30)
              
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                domain.vel[0] = -1
            if event.key == K_RIGHT:
                domain.vel[0] = 1
            if event.key == K_UP:
                domain.vel[1] = -1
            if event.key == K_DOWN:
                domain.vel[1] = 1
            if event.key == K_a:
                domain.if_scale_up = True
            if event.key == K_z:
                domain.if_scale_down = True
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                domain.vel[0] = 0
            if event.key == K_RIGHT:
                domain.vel[0] = 0
            if event.key == K_UP:
                domain.vel[1] = 0
            if event.key == K_DOWN:
                domain.vel[1] = 0
            if event.key == K_a:
                domain.if_scale_up = False
            if event.key == K_z:
                domain.if_scale_down = False
                
    worldMap.cam_world_pos_x += 1

    # adjust camera to position according to the keypresses
    worldMap.set_camera_pos_size()
    windowSurfaceObj.fill((10, 109, 175))
    # render the map
    for sprite_layer in worldMap.sprite_layers:
        if sprite_layer.is_object_group:
            # we dont draw the object group layers
            # you should filter them out if not needed
            continue
        else:
            worldMap.renderer.render_layer(windowSurfaceObj, sprite_layer)
    
    domain.update()
    domain.draw(windowSurfaceObj, interpolation)
    if fps_drawing:
        show_fps(windowSurfaceObj, clock)
    pygame.display.update()