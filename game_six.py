# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game six

from __future__ import division
from scene import *
import ui
import math
from numpy import random
from generic_game import *

class GameSix(GenericGame):
    # this class is game six
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        # edit game background
        GenericGame.get_game_background(self).fill_color = '#b9ffaa'
        
        # properties
        self.truck = LabelNode(text = '', color = 'clear', position = (-100, -100), z_position = 0, parent = input_parent)
        self.truck_move_speed = 20.0
        
        # create arrows left and right
        arrow_size = Vector2(self.size_of_screen_x * (1/9), self.size_of_screen_y * (2/9))
        arrow_color = '#ffd12b'
        left_arrow_position = Vector2(self.size_of_screen_x * (13/18), self.size_of_screen_y * (1/6))
        self.left_arrow = SpriteNode('./assets/sprites/white_arrow_left.png',
                                     color = arrow_color,
                                     parent = input_parent,
                                     size = arrow_size,
                                     position = left_arrow_position,
                                     z_position = 2)
        right_arrow_position = Vector2(self.size_of_screen_x * (17/18), self.size_of_screen_y * (1/6))
        self.right_arrow = SpriteNode('./assets/sprites/white_arrow_right.png',
                                      color = arrow_color,
                                      parent = input_parent,
                                      size = arrow_size,
                                      position = right_arrow_position,
                                      z_position = 2)
        # create road
        road_position = self.game_position
        road_size = Vector2(self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/3))
        road_shape = ui.Path.rect(0, 0, road_size.x, road_size.y)
        self.road = ShapeNode(path = road_shape,
                              fill_color = '#a0a0a0',
                              stroke_color = 'clear',
                              parent = input_parent,
                              position = road_position,
                              z_position = 2)
        # create yellow line on road
        yellow_line_position = self.game_position
        yellow_line_size = Vector2(1, road_size.y)
        yellow_line_shape = ui.Path.rect(0, 0, yellow_line_size.x, yellow_line_size.y)
        yellow_line_shape.line_width = 10
        self.yellow_line = ShapeNode(path = yellow_line_shape,
                                     fill_color = '#f9ff80',
                                     stroke_color = '#f9ff80',
                                     parent = input_parent,
                                     position = yellow_line_position,
                                     z_position = 2)
        # create player vehicle
        player_car_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y * (1/18))
        player_car_size = Vector2(self.size_of_screen_x * (1/17), self.size_of_screen_y * (1/7))
        self.player_car = SpriteNode('./assets/sprites/player_car.png',
                                     parent = input_parent,
                                     position = player_car_position,
                                     z_position = 3,
                                     size = player_car_size)
        
        
    
    #getters and setters
    def get_truck(self):
        #gets the truck property
        return self.truck
    
    def get_player_car(self):
        #gets the player car property
        return self.player_car
    
    def get_left_arrow(self):
        #get the left arrow property
        return self.left_arrow
    
    def get_right_arrow(self):
        #get the right arrow property
        return self.right_arrow
    
    def create_truck(self, input_parent):
        # this method creates a truck
        
        self.truck.remove_from_parent()
        
        truck_size = Vector2(self.size_of_screen_x * (1/17), self.size_of_screen_y * (2/15))
        truck_possible_start_positions = [Vector2(self.size_of_screen_x * (19/24), self.size_of_screen_y * (1/3) + (truck_size.y/2) + 10), Vector2(self.size_of_screen_x * (21/24), self.size_of_screen_y * (1/3) + (truck_size.y/2) + 10)]
        truck_possible_end_positions = [Vector2(self.size_of_screen_x * (19/24), - 100), Vector2(self.size_of_screen_x * (21/24), - 100)]
        truck_position = random.randint(0, 2)
        truck_image = './assets/sprites/truck{0}.png'.format(random.randint(1, 5))
        self.truck = SpriteNode(truck_image,
                                parent = input_parent,
                                size = truck_size,
                                position = truck_possible_start_positions[truck_position],
                                z_position = 3)
        self.truck.run_action(Action.rotate_by(math.pi, 0))
        truck_move_action = Action.move_to(truck_possible_end_positions[truck_position].x,
                                           truck_possible_end_positions[truck_position].y,
                                           self.truck_move_speed)
        self.truck.run_action(truck_move_action)
        
    
    def game_over(self):
        # this method calls a game over
        
        GenericGame.game_over(self)
        self.truck.remove_all_actions()
        self.player_car.remove_all_actions()
