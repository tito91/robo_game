from Static import *
import math
from random import randint
from utils import *

class Dynamic (Static) :
    def __init__(self, fx=0, fy=0, imagepath=''):
        Static.__init__(self, fx, fy, imagepath)
        #velocity vector, keep normalized
        self.vx, self.vy = 0.0, 0.0
        #velocity scalar
        self.v_scal = 0.0
        #acceleration vector, keep normalized
        self.ax, self.ay = 0.0, 0.0
        #acceleration scalar
        self.a_scal = 0.0
        #angular velocity
        self.w = 0.0
        #angular acceleration
        self.e = 0.0
        #surface for actual transformations
        self.view_surface = self.surfaceObj
        
    def draw(self, surf, dt):
        viewx = self.x + self.v_scal*self.vx
        viewy = self.y + self.v_scal*self.vy
        
        rect = self.view_surface.get_rect()
        rect.topleft = viewx, viewy
        surf.blit(self.view_surface, rect)
        
    def update(self, t=1):
        inc_x, inc_y = self.vx*self.v_scal, self.vy*self.v_scal
    
        self.x += inc_x
        self.y += inc_y
        
        self.cx += inc_x
        self.cy += inc_y
                
    def new_dir(self, A, B, rand=0):
        self.vx = B[0]-A[0]
        self.vy = B[1]-A[1]
        
        if rand:
            self.vx += randint(-rand, rand)
            self.vy += randint(-rand, rand)
            
        #normalize? include scalar for normalized velocity vector?
        self.vx, self.vy = normalize([self.vx, self.vy])
        #self.point_to_vel_vector()
        
    def point_to_vel_vector(self):
        angle = 0
    
        #calculate rotation angle of velocity vector
        if self.vx:
            angle = math.atan(self.vy/self.vx)
            angle = math.degrees(angle)

            #check quadrant and add n*90[deg] 
        #according to display coordinates
        #1st quadrant
        if self.vx > 0 and self.vy <= 0:
            angle = -angle
            pass
        #2nd
        if self.vx <= 0 and self.vy < 0:
            angle = 90+90-angle
        #3rd
        if self.vx < 0 and self.vy >= 0:
            angle = 180 - angle
        #4th
        if self.vx >= 0 and self.vy > 0:
            angle += 270 + 90-angle
                        
        self.view_surface = pygame.transform.rotate(self.surfaceObj, angle)
        
        self.cx = self.x+(self.view_surface.get_width())/2 
        self.cy = self.y+(self.view_surface.get_height())/2
    
    def normalize(self):
        self.vx, self.vy = normalize((self.vx, self.vy))