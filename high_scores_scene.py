# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the high scores scene.
# Edited by: Matthew Lourenco
# Dec 13 2016: created high scores scene, made menu button and made it go back to the main menu scene, set up high scores title

from scene import *
import ui

class HighScoresScene(Scene):
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
                                     color = '#b45e00',
                                     parent = self,
                                     size = self.size)
        # add menu button
        menu_button_position = Vector2(self.size_of_screen_x * 0.1, self.size_of_screen_y * 0.85)
        menu_button_shape = ui.Path.oval(0, 0, 120, 120)
        menu_button_shape.line_width = 10 * self.scale_of_sprites
        self.menu_button_scale = self.scale_of_sprites
        self.menu_button = ShapeNode(path = menu_button_shape,
                                     fill_color = '#e38926',
                                     stroke_color = '#c97922',
                                     parent = self,
                                     position = menu_button_position,
                                     scale = self.menu_button_scale)
        # add menu symbol
        self.menu_symbol_scale = 1.5 * self.scale_of_sprites 
        self.menu_symbol = SpriteNode('./assets/sprites/white_arrow_left.png',
                                      parent = self,
                                      position = menu_button_position,
                                      scale = self.menu_symbol_scale)
        # add high scores title
        high_scores_title_position = Vector2(self.center_of_screen_x, self. size_of_screen_y * 0.9)
        self.high_scores_title = LabelNode(text = 'High Scores',
                                           font = ('futura', 80),
                                           color = '#dbdbdb',
                                           parent = self,
                                           position = high_scores_title_position,
                                           scale = self.scale_of_sprites)
        
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = self.menu_button.scale * 0.9
            self.menu_symbol.scale = self.menu_symbol.scale * 0.9
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        # reset scales
        self.menu_button.scale = self.menu_button_scale
        self.menu_symbol.scale = self.menu_symbol_scale
        
        # move to main menu scene
        if self.menu_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
