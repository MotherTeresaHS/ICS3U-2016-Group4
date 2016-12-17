# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game four

from __future__ import division
from scene import *
import ui
from generic_game import *

class GameFour(GenericGame):
    # this class is game four
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        GenericGame.get_game_background(self).fill_color = '#989898'
        
        #create arrow pointing right
        arrow_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y * (5/9))
        arrow_size = Vector2(self.size_of_screen_x * (4/9), self.size_of_screen_y * (1/9))
        self.arrow_right = SpriteNode('./assets/sprites/white_arrow_right.png',
                                      color = '#ffd12b',
                                      parent = input_parent,
                                      position = arrow_position,
                                      z_position = 2,
                                      size = arrow_size,
                                      scale = self.scale_of_sprites)
        #create track for slider
        self.track_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y * (4/9))
        track_size = Vector2(self.size_of_screen_x * (5/18), self.size_of_screen_y * (2/27))
        track_shape = ui.Path.rect(0, 0, track_size.x, track_size.y)
        self.track = ShapeNode(path = track_shape,
                               fill_color = 'clear',
                               stroke_color = 'clear',
                               parent = input_parent,
                               position = self.track_position,
                               z_position = 4,
                               scale = self.scale_of_sprites)
        # create track the the player sees
        seen_track_size = Vector2(self.size_of_screen_x * (6/21), track_size.y)
        seen_track_shape = ui.Path.rect(0, 0, seen_track_size.x, seen_track_size.y)
        self.seen_track = ShapeNode(path = seen_track_shape,
                                    fill_color = '#505050',
                                    stroke_color = '#505050',
                                    parent = input_parent,
                                    position = self.track_position,
                                    z_position = 2,
                                    scale = self.scale_of_sprites)
        # create slider
        slider_position = Vector2(self.size_of_screen_x * (5/6), self.track_position.y)
        slider_size = Vector2(self.size_of_screen_y * (2/27), self.size_of_screen_y * (2/27))
        self.slider = SpriteNode('./assets/sprites/slider.png',
                                 parent = input_parent,
                                 position = slider_position,
                                 z_position = 3,
                                 size = slider_size,
                                 scale = self.scale_of_sprites)
        
    
    #getters and setters
    def get_slider(self):
        #get the slider property
        return self.slider
    
    def get_track(self):
        #get the track property
        return self.track
    
    def get_slider_y(self):
        #get the slider y position
        return self.track_position.y
