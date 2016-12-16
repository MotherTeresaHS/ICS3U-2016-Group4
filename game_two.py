# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game two

from __future__ import division
from scene import *
import ui
from numpy import random
from generic_game import *

class GameTwo(GenericGame):
    # this class is game two
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        # edit background
        GenericGame.get_game_background(self).fill_color = '#989898'
        
        #properties
        self.button_is_red = True
        self.game_paused = False
        
        # add button to game
        button_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y * (5/6))
        button_size = Vector2(self.size_of_screen_y * (1/4), self.size_of_screen_y * (1/4))
        button_shape = ui.Path.oval(0, 0, button_size.x, button_size.y)
        button_shape.line_width = 10 * self.scale_of_sprites
        self.button = ShapeNode(path = button_shape,
                                fill_color = '#e12525',
                                stroke_color = '#aa1c1c',
                                parent = input_parent,
                                position = button_position,
                                z_position = 2)
        # add button shadow
        button_shadow_position = Vector2(button_position.x, button_position.y - 10)
        self.button_shadow = ShapeNode(path = button_shape,
                                       fill_color = 'black',
                                       stroke_color = 'black',
                                       parent = input_parent,
                                       position = button_shadow_position,
                                       z_position = 1,
                                       alpha = 0.75)
        
    
    #getters and setters
    def get_button_is_red(self):
        #get the button is red property
        return self.button_is_red
    
    def get_button(self):
        #get the button property
        return self.button
    
    def get_button_shadow(self):
        #get the button shadow property
        return self.button_shadow
    
    def get_game_paused(self):
        #get the game paused property
        return self.game_paused
    
    def set_game_paused(self, new_state):
        #set the game paused property
        self.game_paused = new_state
    
    def make_button_green(self):
        # this method activates the button
        
        self.button.fill_color = '#28ed39'
        self.button.stroke_color = '#22cb30'
        self.button_is_red = False
    
    def make_button_red(self):
    	# this method deactivates the button
    	
        self.button.fill_color = '#e12525'
        self.button.stroke_color = '#aa1c1c'
        self.button_is_red = True
    
