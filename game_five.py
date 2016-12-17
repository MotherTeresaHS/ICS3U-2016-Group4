# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game five

from __future__ import division
from scene import *
import ui
import math
from numpy import random
from generic_game import *

class GameFive(GenericGame):
    # this class is game five
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        # edit background
        GenericGame.get_game_background(self).fill_color = '#77a0ee'
        
        # properties
        self.shape_type = 0
        self.incoming_shape_position = Vector2(self.size_of_screen_x*(1/6), self.size_of_screen_y*(1/6))
        self.incoming_shape = 0
        
        # create buttons on left and right
        diamond_button_position = Vector2(self.size_of_screen_x * (1/18), self.size_of_screen_y * (1/6))
        diamond_button_size = Vector2(self.size_of_screen_x * (1/9), self.size_of_screen_y * (1/3))
        diamond_button_shape = ui.Path.rect(0, 0, diamond_button_size.x, diamond_button_size.y)
        diamond_button_shape.line_width = 5
        self.diamond_button = ShapeNode(path = diamond_button_shape,
                                        fill_color = 'clear',
                                        stroke_color = 'black',
                                        parent = input_parent,
                                        position = diamond_button_position,
                                        z_position = 2)
        square_button_position = Vector2(self.size_of_screen_x * (5/18), self.size_of_screen_y * (1/6))
        self.square_button = ShapeNode(path = diamond_button_shape,
                                       fill_color = 'clear',
                                       stroke_color = 'black',
                                       parent = input_parent,
                                       position = square_button_position,
                                       z_position = 2)
        # add square symbol
        square_symbol_size = Vector2(self.size_of_screen_x * (1/15), self.size_of_screen_x * (1/15))
        self.square_symbol_shape = ui.Path.rect(0, 0, square_symbol_size.x, square_symbol_size.y)
        self.square_symbol_shape.line_width = 5
        self.square_symbol = ShapeNode(path = self.square_symbol_shape,
                                       fill_color = '#2200c4',
                                       stroke_color = '#190091',
                                       parent = input_parent,
                                       position = square_button_position,
                                       z_position = 3)
        # add diamond symbol
        self.diamond_symbol = ShapeNode(path = self.square_symbol_shape,
                                        fill_color = '#2200c4',
                                        stroke_color = '#190091',
                                        parent = input_parent,
                                        position = diamond_button_position,
                                        z_position = 3)
        self.diamond_symbol.run_action(Action.rotate_by(math.pi / 4, 0))
        
        # add timer circle
        timer_circle_position = Vector2(self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/18) + 10)
        timer_circle_size = Vector2(self.size_of_screen_y * (1/9), self.size_of_screen_y * (1/9))
        timer_circle_shape = ui.Path.oval(0, 0, timer_circle_size.x, timer_circle_size.y)
        timer_circle_shape.line_width = 8 * self.scale_of_sprites
        self.timer_circle = ShapeNode(path = timer_circle_shape,
                                      fill_color = '#e38926',
                                      stroke_color = '#c97922',
                                      parent = input_parent,
                                      position = timer_circle_position,
                                      z_position = 2)
        # add timer text
        self.timer_text = LabelNode(text = '5',
                                    font = ('futura', 60),
                                    color = 'white',
                                    parent = input_parent,
                                    position = timer_circle_position,
                                    z_position = 3)
        
    
    #getters and setters
    def get_incoming_shape(self):
        # get the incoming shape property
        return self.incoming_shape
    
    def get_shape_type(self):
        # get the shape type property
        return self.shape_type
    
    def get_timer(self):
        # get the timer property
        return self.timer_text
    
    def get_diamond_button(self):
        # get the diamond button property
        return self.diamond_button
    
    def get_square_button(self):
        # get the square button property
        return self.square_button
    
    def create_shape(self, input_parent):
        # this method creates a random shape in the center of the game
        
        self.shape_type = random.randint(1, 3)
        
        initial_shape_scale = 0.01
        final_shape_scale = self.scale_of_sprites
        
        if self.shape_type == 1:
            self.incoming_shape = ShapeNode(path = self.square_symbol_shape,
                                            fill_color = '#2200c4',
                                            stroke_color = '#190091',
                                            parent = input_parent,
                                            position = self.incoming_shape_position,
                                            z_position = 4,
                                            scale = initial_shape_scale)
            self.incoming_shape.run_action(Action.rotate_by(math.pi / 4, 0))
        if self.shape_type == 2:
            self.incoming_shape = ShapeNode(path = self.square_symbol_shape,
                                            fill_color = '#2200c4',
                                            stroke_color = '#190091',
                                            parent = input_parent,
                                            position = self.incoming_shape_position,
                                            z_position = 4,
                                            scale = initial_shape_scale)
        
        shape_expand_action = Action.scale_to(final_shape_scale, 12)
        self.incoming_shape.run_action(shape_expand_action)
