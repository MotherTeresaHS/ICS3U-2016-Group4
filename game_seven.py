# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game seven

from __future__ import division
from scene import *
import ui
from generic_game import *

class GameSeven(GenericGame):
    # this class is game seven
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        
        #changed properties
        self.game_size = Vector2(self.size_of_screen_x * (1/3), self.size_of_screen_y)
        self.game_shape = ui.Path.rect(0, 0, self.game_size.x, self.game_size.y)
        self.game_shape.line_width = 5
        GenericGame.get_game_background(self).path = self.game_shape
        GenericGame.get_game_cover(self).path = self.game_shape
        GenericGame.get_game_background(self).z_position = 6
        GenericGame.get_game_cover(self).z_position = 10
        
        #create player
        player_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        player_size = Vector2(self.size_of_screen_y * (1/12), self.size_of_screen_y * (1/12))
        player_shape = ui.Path.oval(0, 0, player_size.x, player_size.y)
        player_shape.line_width = 5
        self.player = ShapeNode(path = player_shape,
                                fill_color = '#66a4cc',
                                stroke_color = '#47728e',
                                parent = input_parent,
                                position = player_position,
                                z_position = 7,
                                size = player_size)
        
        
        
        
    
    #getters and setters
    def get_player(self):
        #get the player property
        return self.player
    
    
    
    
