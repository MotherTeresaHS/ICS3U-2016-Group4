# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game one
# Dec 15 2016: game 1 functional

from __future__ import division
from scene import *
import ui
from numpy import random
from generic_game import *

class GameOne(GenericGame):
    # this class is game one
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
        #create star background
        self.star_background = SpriteNode('./assets/sprites/star_background.jpg',
                                          parent = input_parent,
                                          position = self.game_position,
                                          z_position = 2,
                                          size = self.game_size)
        #create power core
        power_core_position = Vector2(self.game_position.x, self.size_of_screen_y * (2/3) + 20)
        power_core_size = Vector2(self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/18))
        self.power_core = SpriteNode('./assets/sprites/power_core.png',
                                     parent = input_parent,
                                     position = power_core_position,
                                     z_position = 3,
                                     size = power_core_size)
        
        #properties
        self.meteor_size = Vector2(self.size_of_screen_y * (1/6), self.size_of_screen_y * (1/6))
        self.meteor = LabelNode(text = '', color = 'clear', position = (-100, -100), z_position = 0, parent = input_parent)
        self.meteor_move_speed = 20.0
        
    
    #getters and setters
    def get_meteor(self):
        # get meteors property
        return self.meteor
    
    def get_power_core(self):
        # get power core property
        return self.power_core
    
    def get_meteor_move_action(self):
        # get the meteor property
        return self.meteor_move_action
    
    def create_meteor(self, input_meteor_parent):
        # this method creates a meteor
        meteor_start_position = Vector2(random.randint(0, self.size_of_screen_x * (1/3)),
                                        self.size_of_screen_y + 60)
        meteor_end_position = Vector2(self.size_of_screen_x * (1/6), self.size_of_screen_y * (2/3))
        self.meteor_scale = self.scale_of_sprites * 0.5
        temp_texture = './assets/sprites/meteor{0}.png'.format(str(random.randint(1,5)))
        self.meteor = SpriteNode(temp_texture,
                                 parent = input_meteor_parent,
                                 position = meteor_start_position,
                                 z_position = 3,
                                 size = self.meteor_size)
        
        meteor_move_action = Action.move_to(meteor_end_position.x,
                                            meteor_end_position.y,
                                            self.meteor_move_speed)
        
        self.meteor.run_action(meteor_move_action)
    
    def game_over(self):
        # this method calls a game over
        GenericGame.game_over(self)
        self.meteor.remove_all_actions()
