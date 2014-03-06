import pygame, sys, tiledtmxloader
from utils import *
import math


class WorldMap:
    def __init__(self, filename):
        args = sys.argv[1:]
        if len(args) < 1:
            path_to_map = os.path.join(homepath, filename)
        else:
            path_to_map = args[0]
            
        self.world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode(path_to_map)

        # load the images using pygame
        self.resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
        self.resources.load(self.world_map)

        # prepare map rendering
        assert self.world_map.orientation == "orthogonal"

        # renderer
        self.renderer = tiledtmxloader.helperspygame.RendererPygame()

        # cam_offset is for scrolling
        self.cam_world_pos_x = 0
        self.cam_world_pos_y = abs(self.world_map.pixel_height - SCRHEIGHT)

        # set initial cam position and size
        self.renderer.set_camera_position_and_size(self.cam_world_pos_x, self.cam_world_pos_y, SCRWIDTH, SCRHEIGHT, "topleft")

        # retrieve the layers
        self.sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(self.resources)
        
    def print_map_info(self):      
        print("loaded map:", self.world_map.map_file_name)

        x_pixels = self.world_map.pixel_width
        y_pixels = self.world_map.pixel_height
        print("map size in pixels:", x_pixels, y_pixels)

        print("tile size used:",  self.world_map.tilewidth, self.world_map.tileheight)

        print("tiles used:", self.world_map.width, self.world_map.height)

        print("found '", len(self.world_map.layers), "' layers on this map")
        
    def set_camera_pos_size(self):
        self.renderer.set_camera_position(self.cam_world_pos_x, self.cam_world_pos_y, "topleft")