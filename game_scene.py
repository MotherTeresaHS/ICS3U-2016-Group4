# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# Dec 14 2016: created game scene. made scene read file to determine scale of sprites
# Dec 15 2016: game 1 functional

from __future__ import division
from scene import *
import ui
import time
from numpy import random
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
        
        # properties
        self.meteor_on_screen = False
        
        # add background color
        background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.background = SpriteNode(position = background_position,
                                     color = '#e5e5e5',
                                     parent = self,
                                     size = self.size)
        # set up 7 games
        self.game1 = GameOne(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (5/6))
        self.game2 = GameTwo(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (5/6))
        self.game3 = GameThree(self, self.size_of_screen_x * (1/6), self.center_of_screen_y)
        self.game4 = GameFour(self, self.size_of_screen_x * (5/6), self.center_of_screen_y)
        self.game5 = GameFive(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/6))
        self.game6 = GameSix(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (1/6))
        self.game7 = GameSeven(self, self.center_of_screen_x, self.center_of_screen_y)
        
        self.game1.activate_game()
        
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        random_game_action_chance = random.randint(0, 100)
        if self.game1.get_game_active and not self.meteor_on_screen and random_game_action_chance < 5:
            self.game1.create_meteor(self)
            self.meteor_on_screen = True
        
        for meteor in self.game1.get_meteors():
            if meteor.frame.intersects(self.game1.get_power_core().frame):
                self.end_game()
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        for meteor in self.game1.get_meteors():
            if meteor.frame.contains_point(touch.location):
                meteor.remove_from_parent()
                self.game1.get_meteors().remove(meteor)
                self.meteor_on_screen = False
    
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
    
    def end_game(self):
        # this method ends the game
        self.game1.game_over()
        self.game2.game_over()
        self.game3.game_over()
        self.game4.game_over()
        self.game5.game_over()
        self.game6.game_over()
        self.game7.game_over()
    
