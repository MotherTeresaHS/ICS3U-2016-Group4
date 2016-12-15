# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines a generic game layout
# Dec 14 2016: created a generic game background and cover

from __future__ import division
from scene import *
import ui
import json

class GenericGame():
    # this class is a generic game
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        # read file to determine size of screen
        shared_variables = open('./shared_variables.txt')
        screen_size = json.load(shared_variables)
        self.size_of_screen_x = screen_size[0]
        self.size_of_screen_y = screen_size[1]
        self.center_of_screen_x = screen_size[2]
        self.center_of_screen_y = screen_size[3]
        self.scale_of_sprites = screen_size[4]
        shared_variables.close()
        
        #Properties
        self.__game_position = Vector2(game_position_x, game_position_y)
        self.__game_size = Vector2(self.size_of_screen_x * (1/3), self.size_of_screen_y * (1/3))
        self.__game_shape = ui.Path.rect(0, 0, self.__game_size.x, self.__game_size.y)
        self.__game_shape.line_width = 5
        self.__game_background = ShapeNode(path = self.__game_shape,
                                           fill_color = '#e5e5e5',
                                           stroke_color = 'black',
                                           z_position = 1,
                                           parent = input_parent,
                                           position = self.__game_position)
        # Black cover for game
        self.__cover = ShapeNode(path = self.__game_shape,
                                 fill_color = 'black',
                                 stroke_color = 'black',
                                 z_position = 2,
                                 alpha = 0.5,
                                 parent = input_parent,
                                 position = self.__game_position)
        
    
    #getters and setters
    def get_game_background(self):
        #get the game background property
        return self.__game_background
    
    def get_game_cover(self):
        #get the game cover property
        return self.__cover
    
    def game_over(self):
        # this method calls a gameover and shuts down the game
        pass
