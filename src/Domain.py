import utils
import operator

class Domain:
    def __init__(self, radius, pos):
        self.radius = radius
        self.pos = [pos[0], pos[1]]
        #velocity vector, keep normalized
        self.vel = [0.0, 0.0]
        #velocity scalar
        self.v_scal = 10
        #scaling speed
        self.scal_step = 10
        self.fish_list = []
        self.randomness = 160
        self.if_scale_up = False
        self.if_scale_down = False
        self.radius_min = 50
        self.radius_max = 200
        self.rel_offset_x = 0
        self.rel_offset_y = 0

    def draw(self, screen, dt, color=utils.pygame.Color(58, 116, 134)):
        utils.pygame.draw.circle(screen, color, (int(self.pos[0]), int(self.pos[1])), self.radius, 2)
        for f in self.fish_list:
            f.draw(screen, dt)

    def is_in_bounds(self, coords=[], fish=[]):
        if coords:
            k = utils.math.sqrt((coords[0] - self.pos[0]) ** 2 + (coords[1] - self.pos[1]) ** 2)
        elif fish:
            k = utils.math.sqrt((fish.cx - self.pos[0]) ** 2 + (fish.cy - self.pos[1]) ** 2)
        elif fish and coords:
            print("Only one parameter needed")
            return
        if k <= self.radius:
            return True
        else:
            return False

    def add_fish(self, *fishes):
        for f in fishes:
            self.fish_list.append(f)

    def update(self):
        inc_x, inc_y = self.vel[0] * self.v_scal, self.vel[1] * self.v_scal

        if (self.pos[0] + inc_x - self.radius) >= 0 and (self.pos[0] + inc_x + self.radius) <= utils.SCRWIDTH:
            self.pos[0] += inc_x
        if (self.pos[1] + inc_y - self.radius) >= 0 and (self.pos[1] + inc_y + self.radius) <= utils.SCRHEIGHT:
            self.pos[1] += inc_y

        if self.if_scale_down and (self.radius - self.scal_step) >= self.radius_min:
            self.radius -= self.scal_step

        if (self.if_scale_up and (self.radius + self.scal_step) <= self.radius_max and
                    (self.pos[0] - self.radius - self.scal_step) >= 0 and (
                        self.pos[0] + self.radius + self.scal_step) <= utils.SCRWIDTH and
                    (self.pos[1] - self.radius - self.scal_step) >= 0 and (
                        self.pos[1] + self.radius + self.scal_step) <= utils.SCRHEIGHT):
            self.radius += self.scal_step

        for f in self.fish_list:
            f.update()

        for f in self.fish_list:
            if not self.is_in_bounds(fish=f):
                f.new_dir((f.cx, f.cy), self.pos, 40)

    def check_for_collisions(self, coll_layer):
        for fish in self.fish_list:
            tile_x = int(operator.div((fish.cx + self.rel_offset_x), coll_layer.tilewidth))
            tile_y = int(operator.div((fish.cy + self.rel_offset_y), coll_layer.tileheight))
            #print(tile_x, tile_y)
            #print(fish.cx + self.rel_offset_x, fish.cy + self.rel_offset_y)
            if coll_layer.content2D[tile_y][tile_x] is not None:
                print("collision occured")
