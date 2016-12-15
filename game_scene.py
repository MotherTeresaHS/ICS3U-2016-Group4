# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# Dec 14 2016: created game scene. made scene read file to determine scale of sprites

from __future__ import division
from scene import *
import ui
from game_one import *
from game_two import *
from game_three import *
from game_four import *
from game_five import *
from game_six import *
from game_seven import *

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #These variable are created in order to avoid pointers
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        # read file to determine self.scale of sprites
        shared_variables = open('./shared_variables.txt')
        screen_size = json.load(shared_variables)
        self.scale_of_sprites = screen_size[4]
        shared_variables.close()
        
        # add background color
        background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.background = SpriteNode(position = background_position,
                                     color = '#e5e5e5',
                                     parent = self,
                                     size = self.size)
        # set up 7 games
        game1 = GameOne(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (5/6))
        game2 = GameTwo(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (5/6))
        game3 = GameThree(self, self.size_of_screen_x * (1/6), self.center_of_screen_y)
        game4 = GameFour(self, self.size_of_screen_x * (5/6), self.center_of_screen_y)
        game5 = GameFive(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/6))
        game6 = GameSix(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (1/6))
        #game7 = GameSeven(self, self.center_of_screen_x, self.center_of_screen_y)
        
        
        
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
