# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game seven

from __future__ import division
from scene import *
import ui
import math
from numpy import random
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
        
        #properties
        self.mines = []
        self.mine_minimum_distance = self.size_of_screen_y * (1/6)
        self.mine_move_speed = 20
        
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
    
    def get_mines(self):
        #get the mines property
        return self.mines
    
    def create_mine(self, input_parent):
        #this method creates a seeking mine that heads towards the player
        
        mine_position = Vector2(random.randint(round(self.size_of_screen_x * (9/24), 3), round(self.size_of_screen_x * (15/24), 3) + 1), random.randint(round(self.size_of_screen_y * (1/24), 3), round(self.size_of_screen_y * (23/24), 3) + 1))
        mine_size = Vector2(self.size_of_screen_y * (1/18), self.size_of_screen_y * (1/18))
        mine_shape = ui.Path.rounded_rect(0, 0, mine_size.x, mine_size.y, 8)
        mine_shape.line_width = 5 * self.scale_of_sprites
        
        if mine_position.x - self.player.position.x > self.mine_minimum_distance or mine_position.x - self.player.position.x < -self.mine_minimum_distance or mine_position.y - self.player.position.y > self.mine_minimum_distance or mine_position.y - self.player.position.y < -self.mine_minimum_distance:
            self.mines.append(ShapeNode(path = mine_shape,
                                        fill_color = '#ff5555',
                                        stroke_color = '#d74848',
                                        parent = input_parent,
                                        position = mine_position,
                                        z_position = 7))
            self.mine_move_action = Action.move_to(self.player.position.x, self.player.position.y, self.mine_move_speed)
            self.mines[len(self.mines) - 1].run_action(self.mine_move_action)
        
    
    def game_over(self):
        #this calls and changes the game_over method
        
        GenericGame.game_over(self)
        
        for mine in self.mines:
            mine.remove_all_actions()
