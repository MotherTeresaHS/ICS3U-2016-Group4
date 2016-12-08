# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# 8 Dec 2016: created scene, added back button

from scene import *
import ui


class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #These variable are created in order to avoid pointers
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        self.scale_of_sprites = 1
        
        # add background color
        instructions_background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.instructions_background = SpriteNode(position = instructions_background_position, 
                                                  color = '#93acdc', 
                                                  parent = self,
                                                  size = self.size)
        # add back button
        back_button_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.85)
        back_button_shape = ui.Path.oval(0, 0, 120, 120)
        back_button_shape.line_width = 10 * self.scale_of_sprites
        self.back_button_scale = self.scale_of_sprites
        self.back_button = ShapeNode(path = back_button_shape,
                                     fill_color = '#e38926',
                                     stroke_color = '#c97922',
                                     parent = self,
                                     position = back_button_position,
                                     scale = self.back_button_scale)
        # add back symbol
        self.back_symbol_scale = 1.5 * self.scale_of_sprites 
        self.back_symbol = SpriteNode('./assets/sprites/white_arrow_up.png',
                                      parent = self,
                                      position = back_button_position,
                                      scale = self.back_symbol_scale)
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = self.back_button.scale * 0.9
            self.back_symbol.scale = self.back_symbol.scale * 0.9
        
        #dismiss scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #reset scales
        self.back_button.scale = self.back_button_scale
        self.back_symbol.scale = self.back_symbol_scale
    
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
