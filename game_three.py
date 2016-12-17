# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game three

from __future__ import division
from scene import *
import ui
import math
from numpy import random
from generic_game import *

class GameThree(GenericGame):
    # this class is game three
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        # edit game background
        GenericGame.get_game_background(self).fill_color = '#b9ffaa'
        
        #properties
        self.incoming_shape = []
        self.shape_move_speed = 5.0
        self.shape_type = 0
        
        # add timer circle
        timer_circle_position = Vector2(self.size_of_screen_x * (1/6), self.center_of_screen_y)
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
                                    z_position = 3,
                                    scale = self.scale_of_sprites)
        #add 3 buttons on right of game
        button1_position = Vector2(self.size_of_screen_x * (5/18), self.size_of_screen_y * (11/18))
        button2_position = Vector2(self.size_of_screen_x * (5/18), self.size_of_screen_y * (1/2))
        button3_position = Vector2(self.size_of_screen_x * (5/18), self.size_of_screen_y * (7/18))
        button_size = Vector2(self.size_of_screen_x * (1/9), self.size_of_screen_y * (1/9))
        button_shape = ui.Path.rect(0, 0, button_size.x, button_size.y)
        button_shape.line_width = 5
        self.button1 = ShapeNode(path = button_shape,
                                 fill_color = 'clear',
                                 stroke_color = 'black',
                                 parent = input_parent,
                                 position = button1_position,
                                 z_position = 2)
        self.button2 = ShapeNode(path = button_shape,
                                 fill_color = 'clear',
                                 stroke_color = 'black',
                                 parent = input_parent,
                                 position = button2_position,
                                 z_position = 2)
        self.button3 = ShapeNode(path = button_shape,
                                 fill_color = 'clear',
                                 stroke_color = 'black',
                                 parent = input_parent,
                                 position = button3_position,
                                 z_position = 2)
        button1_symbol_size = Vector2(self.size_of_screen_y * (7/72), self.size_of_screen_y * (7/72))
        self.button1_symbol_shape = ui.Path.oval(0, 0, button1_symbol_size.x, button1_symbol_size.y)
        self.button1_symbol = ShapeNode(path = self.button1_symbol_shape,
                                        fill_color = 'green',
                                        stroke_color = 'clear',
                                        parent = input_parent,
                                        position = button1_position,
                                        z_position = 3)
        button2_symbol_size = button1_symbol_size
        self.button2_symbol_shape = ui.Path.rect(0, 0, button2_symbol_size.x, button2_symbol_size.y)
        self.button2_symbol = ShapeNode(path = self.button2_symbol_shape,
                                        fill_color = 'green',
                                        stroke_color = 'clear',
                                        parent = input_parent,
                                        position = button2_position,
                                        z_position = 3)
        self.button3_symbol_size = button1_symbol_size
        self.button3_symbol = SpriteNode('./assets/sprites/green_hexagon.png',
                                         color = 'green',
                                         parent = input_parent,
                                         size = self.button3_symbol_size,
                                         position = button3_position,
                                         z_position = 3)
        self.button3_symbol.run_action(Action.rotate_by(math.pi / 2, 0))
        
    
    #getters and setters
    def get_timer(self):
        #gets the timer text property
        return self.timer_text
    
    def get_shape_type(self):
        #get the shape type property
        return self.shape_type
    
    def get_incoming_shape(self):
        #get the incoming shape property
        return self.incoming_shape
    
    def get_button_one(self):
        #get the button one property
        return self.button1
    
    def get_button_two(self):
        #get the button two property
        return self.button2
    
    def get_button_three(self):
        #get the button three property
        return self.button3
    
    def create_shape(self, input_parent):
        # this method creates a shape
        
        self.shape_type = random.randint(1, 4)
        shape_start_position = Vector2(-100, self.center_of_screen_y)
        shape_end_position = Vector2(self.size_of_screen_x * (1/18), self.center_of_screen_y)
        
        if self.shape_type == 1:
            self.incoming_shape.append(ShapeNode(path = self.button1_symbol_shape,
                                                 fill_color = 'green',
                                                 stroke_color = 'clear',
                                                 parent = input_parent,
                                                 position = shape_start_position,
                                                 z_position = 3))
        elif self.shape_type == 2:
            self.incoming_shape.append(ShapeNode(path = self.button2_symbol_shape,
                                                 fill_color = 'green',
                                                 stroke_color = 'clear',
                                                 parent = input_parent,
                                                 position = shape_start_position,
                                                 z_position = 3))
        elif self.shape_type == 3:
            self.incoming_shape.append(SpriteNode('./assets/sprites/green_hexagon.png',
                                                  color = 'green',
                                                  parent = input_parent,
                                                  size = self.button3_symbol_size,
                                                  position = shape_start_position,
                                                  z_position = 3))
            self.incoming_shape[0].run_action(Action.rotate_by(math.pi / 2, 0))
        shape_move_action = Action.move_to(shape_end_position.x,
                                           shape_end_position.y,
                                           self.shape_move_speed)
        self.incoming_shape[0].run_action(shape_move_action)
        
        
        
    
    def game_over(self):
        # this method calls a game over
        
        GenericGame.game_over(self)
        for shape in self.incoming_shape:
            shape.remove_all_actions()
