# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# Dec 7 2016: added menu Items, made info button go to help scene
# Dec 13 2016: made high scores button go to high scores scene

from scene import *
import ui
from instructions_scene import *
from high_scores_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #These variable are created in order to avoid pointers
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        self.scale_of_sprites = 1
        
        # add background color
        background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.background = SpriteNode(position = background_position,
                                     color = '#e5e5e5',
                                     parent = self,
                                     size = self.size)
        # add play button
        play_button_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.4)
        self.play_button_scale = 2 * self.scale_of_sprites
        self.play_button = SpriteNode('./assets/sprites/green_hexagon.png',
                                      position = play_button_position,
                                      parent = self,
                                      scale = self.play_button_scale)
        # add symbol to center of play button
        play_symbol_position = Vector2(self.center_of_screen_x + 10, self.size_of_screen_y * 0.4)
        self.play_symbol_scale = 2 * self.scale_of_sprites
        self.play_symbol = SpriteNode('./assets/sprites/white_play_button.png',
                                      position = play_symbol_position,
                                      parent = self,
                                      scale = self.play_symbol_scale)
        # add game title
        game_title_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.8)
        game_title_scale = self.scale_of_sprites
        self.game_title = LabelNode(text = 'Task Manager',
                                    font = ('Futura', 80),
                                    color = '#3cb346',
                                    parent = self,
                                    position = game_title_position,
                                    scale = game_title_scale)
        # add help button
        help_button_position = Vector2(self.size_of_screen_x * 0.1666, self.size_of_screen_y * 0.4)
        help_button_shape = ui.Path.oval(0, 0, 120, 120)
        help_button_shape.line_width = 10 * self.scale_of_sprites
        self.help_button_scale = self.scale_of_sprites
        self.help_button = ShapeNode(path = help_button_shape,
                                     fill_color = '#4424db',
                                     stroke_color = '#3a1fbb',
                                     position = help_button_position,
                                     parent = self,
                                     scale = self.help_button_scale)
        # add help symbol
        self.help_symbol_scale = 1.3 * self.scale_of_sprites
        self.help_symbol = SpriteNode('./assets/sprites/white_information.png',
                                      position = help_button_position,
                                      parent = self,
                                      scale = self.help_symbol_scale)
        # add high scores button
        high_scores_button_position = Vector2(self.size_of_screen_x * 0.8333, self.size_of_screen_y * 0.4)
        high_scores_button_shape = ui.Path.oval(0, 0, 120, 120)
        high_scores_button_shape.line_width = 10 * self.scale_of_sprites
        self.high_scores_button_scale = self.scale_of_sprites
        self.high_scores_button = ShapeNode(path = high_scores_button_shape,
                                            fill_color = '#ffc800',
                                            stroke_color = '#e4b200',
                                            position = high_scores_button_position,
                                            parent = self,
                                            scale = self.high_scores_button_scale)
        # add high scores symbol
        self.high_scores_symbol_scale = 1.3 * self.scale_of_sprites
        self.high_scores_symbol = SpriteNode('./assets/sprites/white_trophy.png',
                                             position = high_scores_button_position,
                                             parent = self,
                                             scale = self.high_scores_symbol_scale)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = self.help_button.scale * 0.9
            self.help_symbol.scale = self.help_symbol.scale * 0.9
        
        if self.high_scores_button.frame.contains_point(touch.location):
            self.high_scores_button.scale = self.high_scores_button.scale * 0.9
            self.high_scores_symbol.scale = self.high_scores_symbol.scale * 0.9
        
        if self.play_button.frame.contains_point(touch.location):
            self.play_button.scale = self.play_button.scale * 0.9
            self.play_symbol.scale = self.play_symbol.scale * 0.9
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # All buttons return to original size
        self.help_button.scale = self.help_button_scale
        self.help_symbol.scale = self.help_symbol_scale
        self.high_scores_button.scale = self.high_scores_button_scale
        self.high_scores_symbol.scale = self.high_scores_symbol_scale
        self.play_button.scale = self.play_button_scale
        self.play_symbol.scale = self.play_symbol_scale
        
        # switch scenes when buttons pressed
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(InstructionsScene())
        
        if self.high_scores_button.frame.contains_point(touch.location):
            self.present_modal_scene(HighScoresScene())
        
        if self.play_button.frame.contains_point(touch.location):
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
