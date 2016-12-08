# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# 7 Dec 2016: created help scene
# 8 Dec 2016: created buttons, shapes, credits and placeholders for game images that take you to the instructions scene

from scene import *
import ui
from instructions_scene import *

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #These variable are created in order to avoid pointers
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        self.scale_of_sprites = 1
        
        # add background color
        help_background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.help_background = SpriteNode(position = help_background_position, 
                                     color = '#93acdc', 
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
        # add box to contain credits
        credits_box_position = Vector2(self.size_of_screen_x * 0.55, self.size_of_screen_y * 0.7)
        credits_box_size = Vector2(self.size_of_screen_x * 0.7, self.size_of_screen_y * 0.4)
        credits_shape = ui.Path.rounded_rect(0, 0, credits_box_size.x, credits_box_size.y, 30)
        credits_shape.line_width = 10 * self.scale_of_sprites
        self.credits_box = ShapeNode(path = credits_shape,
                                     fill_color = '#838383',
                                     stroke_color = '#707070',
                                     parent = self,
                                     position = credits_box_position,
                                     scale = self.scale_of_sprites)
        # Write out "Credits"
        credits_title_position = Vector2(credits_box_position.x, self.size_of_screen_y * 0.8)
        self.credits_title = LabelNode(text = 'Credits',
                                       font = ('Futura', 80),
                                       color = 'white',
                                       parent = self,
                                       position = credits_title_position,
                                       scale = self.scale_of_sprites)
        # Write out the credits
        credits_position = Vector2(credits_box_position.x, self.size_of_screen_y * 0.65)
        self.credits = LabelNode(text = 'Programmer: Matthew Lourenco\nArt by: Kenney Vleugels (www.kenney.nl)\nTemplate: Patrick Coxall\nClass: ICS3U, Mother Teresa High School',
                                 font = ('Futura', 30),
                                 color = 'white',
                                 parent = self,
                                 position = credits_position,
                                 scale = self.scale_of_sprites)
        # Add text that explains what the images are for
        image_explanation_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.45)
        self.image_explanation = LabelNode(text = 'Click on an image below for detailed instructions of each game',
                                           font = ('Futura', 35),
                                           color = self.menu_button.fill_color,
                                           parent = self,
                                           position = image_explanation_position,
                                           scale = self.scale_of_sprites)
        # add 7 game images
        game1_image_position = Vector2(self.size_of_screen_x * 0.125, self.size_of_screen_y * 0.3)
        self.game1_image_scale = self.scale_of_sprites
        self.game1_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game1_image_position,
                                      scale = self.game1_image_scale)
        game2_image_position = Vector2(self.size_of_screen_x * 0.375, self.size_of_screen_y * 0.3)
        self.game2_image_scale = self.scale_of_sprites
        self.game2_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game2_image_position,
                                      scale = self.game2_image_scale)
        game3_image_position = Vector2(self.size_of_screen_x * 0.625, self.size_of_screen_y * 0.3)
        self.game3_image_scale = self.scale_of_sprites
        self.game3_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game3_image_position,
                                      scale = self.game3_image_scale)
        game4_image_position = Vector2(self.size_of_screen_x * 0.875, self.size_of_screen_y * 0.3)
        self.game4_image_scale = self.scale_of_sprites
        self.game4_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game4_image_position,
                                      scale = self.game4_image_scale)
        game5_image_position = Vector2(self.size_of_screen_x * 0.25, self.size_of_screen_y * 0.15)
        self.game5_image_scale = self.scale_of_sprites
        self.game5_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game5_image_position,
                                      scale = self.game5_image_scale)
        game6_image_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.15)
        self.game6_image_scale = self.scale_of_sprites
        self.game6_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game6_image_position,
                                      scale = self.game6_image_scale)
        game7_image_position = Vector2(self.size_of_screen_x * 0.75, self.size_of_screen_y * 0.15)
        self.game7_image_scale = self.scale_of_sprites
        self.game7_image = SpriteNode('assets/sprites/black_question.png',
                                      parent = self,
                                      position = game7_image_position,
                                      scale = self.game7_image_scale)
        
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = self.menu_button.scale * 0.9
            self.menu_symbol.scale = self.menu_symbol.scale * 0.9
        
        if self.game1_image.frame.contains_point(touch.location):
            self.game1_image.scale = self.game1_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game2_image.frame.contains_point(touch.location):
            self.game2_image.scale = self.game2_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game3_image.frame.contains_point(touch.location):
            self.game3_image.scale = self.game3_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game4_image.frame.contains_point(touch.location):
            self.game4_image.scale = self.game4_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game5_image.frame.contains_point(touch.location):
            self.game5_image.scale = self.game5_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game6_image.frame.contains_point(touch.location):
            self.game6_image.scale = self.game6_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        if self.game7_image.frame.contains_point(touch.location):
            self.game7_image.scale = self.game7_image.scale * 0.9
            self.present_modal_scene(InstructionsScene())
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #reset scales
        self.menu_button.scale = self.menu_button_scale
        self.menu_symbol.scale = self.menu_symbol_scale
        self.game1_image.scale = self.game1_image_scale
        self.game2_image.scale = self.game2_image_scale
        self.game3_image.scale = self.game3_image_scale
        self.game4_image.scale = self.game4_image_scale
        self.game5_image.scale = self.game5_image_scale
        self.game6_image.scale = self.game6_image_scale
        self.game7_image.scale = self.game7_image_scale
        
        #dismiss scene
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