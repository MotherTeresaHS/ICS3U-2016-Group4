# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# 8 Dec 2016: created scene, added back button
# 9 Dec 2016: created placeholder image, text area and placeholder text, merged this scene with the help scene and animated the transition
# 13 Dec 2016: Created descriptions for each game, made descriptions and pictures change based on the button pressed
# 14 Dec 2016: made scene read file to determine scale of sprites

from scene import *
import ui
import json

class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #These variables are created in order to avoid pointers
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2
        
        # read file to determine self.scale of sprites
        shared_variables = open('./shared_variables.txt')
        screen_size = json.load(shared_variables)
        self.scale_of_sprites = screen_size[4]
        shared_variables.close()
        
        self.item_move_speed = 2.5
        
        # Game descriptions
        self.game1_description = 'This is game 1:\nIn this game an asteriod\nwill randomly appear and\nmove towards a power\ncore. Tap the asteriod\nto destroy it! If\nthe asteroid touches the\npower core you lose!'
        self.game2_description = "This is game 2:\nThere is a button in\nthe center of this game.\nWhen it turns green you\nmust press it within five\nseconds or you lose. If\nyou press it while it\nis red you will also lose."
        self.game3_description = "This is game 3:\nIn this game, shapes will\nappear on the left and\nyou must sort them by\npressing the matching button on\nthe right. If you press\nthe wrong button or take\nlonger than five seconds to\npress the correct one you lose."
        self.game4_description = "This is game 4:\nIn this game a slider moves\nslowly to the left. Keep it\nas far right as you can!\nIf the slider reaches the\nleft end of the track you lose!"
        self.game5_description = "This is game 5:\nIn the center of this game\na shape will slowly expand.\nSort it by pressing the\nmatching button on the right\nor left. If you press the\nwrong button, or five seconds\npass you lose!"
        self.game6_description = "This is game 6:\nIn this game you are\ndriving down the highway.\nTrucks will drive towards you\nfrom the other direction. avoid\nthem by touching the left or\nright button. If you touch\na truck you lose!"
        self.game7_description = "This is game 7:\nIn this game you are the\ncircle in the middle of\nthe screen. Tilt the screen\nto move the circle. Don't\ntouch the sides of the\nbox or the red triangles\nor you lose!"
        
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
        self.game1_image_scale = 3 * self.scale_of_sprites
        self.game1_image = SpriteNode('assets/sprites/button1.png',
                                      parent = self,
                                      position = game1_image_position,
                                      scale = self.game1_image_scale)
        game2_image_position = Vector2(self.size_of_screen_x * 0.375, self.size_of_screen_y * 0.3)
        self.game2_image_scale = 3 * self.scale_of_sprites
        self.game2_image = SpriteNode('assets/sprites/button2.png',
                                      parent = self,
                                      position = game2_image_position,
                                      scale = self.game2_image_scale)
        game3_image_position = Vector2(self.size_of_screen_x * 0.625, self.size_of_screen_y * 0.3)
        self.game3_image_scale = 3 * self.scale_of_sprites
        self.game3_image = SpriteNode('assets/sprites/button3.png',
                                      parent = self,
                                      position = game3_image_position,
                                      scale = self.game3_image_scale)
        game4_image_position = Vector2(self.size_of_screen_x * 0.875, self.size_of_screen_y * 0.3)
        self.game4_image_scale = 3 * self.scale_of_sprites
        self.game4_image = SpriteNode('assets/sprites/buttonA.png',
                                      parent = self,
                                      position = game4_image_position,
                                      scale = self.game4_image_scale)
        game5_image_position = Vector2(self.size_of_screen_x * 0.25, self.size_of_screen_y * 0.15)
        self.game5_image_scale = 3 * self.scale_of_sprites
        self.game5_image = SpriteNode('assets/sprites/buttonB.png',
                                      parent = self,
                                      position = game5_image_position,
                                      scale = self.game5_image_scale)
        game6_image_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.15)
        self.game6_image_scale = 3 * self.scale_of_sprites
        self.game6_image = SpriteNode('assets/sprites/buttonL.png',
                                      parent = self,
                                      position = game6_image_position,
                                      scale = self.game6_image_scale)
        game7_image_position = Vector2(self.size_of_screen_x * 0.75, self.size_of_screen_y * 0.15)
        self.game7_image_scale = 3 * self.scale_of_sprites
        self.game7_image = SpriteNode('assets/sprites/buttonL1.png',
                                      parent = self,
                                      position = game7_image_position,
                                      scale = self.game7_image_scale)

        # add back button
        back_button_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.9 - self.size_of_screen_y)
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
        # add placeholder Image
        placeholder_image_position = Vector2(self.size_of_screen_x * 0.75, self.size_of_screen_y * 0.425 - self.size_of_screen_y)
        placeholder_image_size = Vector2(self.size_of_screen_x * 0.45, self.size_of_screen_y * 0.7)
        self.placeholder_image = SpriteNode('./assets/sprites/black_massive_multiplayer.png',
                                            parent = self,
                                            position = placeholder_image_position,
                                            size = placeholder_image_size,
                                            scale = self.scale_of_sprites)
        # add text area
        text_area_position = Vector2(self.size_of_screen_x * 0.25, self.size_of_screen_y * 0.425 - self.size_of_screen_y)
        text_area_size = Vector2(placeholder_image_size.x, placeholder_image_size.y)
        text_area_shape = ui.Path.rounded_rect(0, 0, text_area_size.x, text_area_size.y, 30)
        text_area_shape.line_width = 10 * self.scale_of_sprites
        self.text_area = ShapeNode(path = text_area_shape,
                                   fill_color = '#838383',
                                   stroke_color = '#707070',
                                   parent = self,
                                   position = text_area_position,
                                   scale = self.scale_of_sprites)
        # add text
        placeholder_text = 'This is placeholder text\nThis is placeholder text\nThis is placeholder text\nThis is placeholder text\nThis is placeholder text\nThis is placeholder text\nThis is placeholder text\nThis is placeholder text'
        self.placeholder_text_label = LabelNode(text = placeholder_text,
                                               font = ('futura', 30),
                                               color = 'white',
                                               parent = self,
                                               position = text_area_position,
                                               scale = self.scale_of_sprites)
        
        # List of items for animating purposes
        self.scene_items = [self.menu_button, self.menu_symbol, self.credits_box, self.credits_title, self.credits, self.image_explanation, self.game1_image, self.game2_image, self.game3_image, self.game4_image, self.game5_image, self.game6_image, self.game7_image, self.back_button, self.back_symbol, self.placeholder_image, self.text_area, self.placeholder_text_label]
        
    
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
            
        if self.game2_image.frame.contains_point(touch.location):
            self.game2_image.scale = self.game2_image.scale * 0.9
            
        if self.game3_image.frame.contains_point(touch.location):
            self.game3_image.scale = self.game3_image.scale * 0.9
            
        if self.game4_image.frame.contains_point(touch.location):
            self.game4_image.scale = self.game4_image.scale * 0.9
            
        if self.game5_image.frame.contains_point(touch.location):
            self.game5_image.scale = self.game5_image.scale * 0.9
            
        if self.game6_image.frame.contains_point(touch.location):
            self.game6_image.scale = self.game6_image.scale * 0.9
            
        if self.game7_image.frame.contains_point(touch.location):
            self.game7_image.scale = self.game7_image.scale * 0.9
            
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = self.back_button.scale * 0.9
            self.back_symbol.scale = self.back_symbol.scale * 0.9
        
        
    
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
        self.back_button.scale = self.back_button_scale
        self.back_symbol.scale = self.back_symbol_scale
        
        #Move to instructions scene
        if self.game1_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game1_image.texture
            self.placeholder_text_label.text = self.game1_description
        if self.game2_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game2_image.texture
            self.placeholder_text_label.text = self.game2_description
        if self.game3_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game3_image.texture
            self.placeholder_text_label.text = self.game3_description
        if self.game4_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game4_image.texture
            self.placeholder_text_label.text = self.game4_description
        if self.game5_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game5_image.texture
            self.placeholder_text_label.text = self.game5_description
        if self.game6_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game6_image.texture
            self.placeholder_text_label.text = self.game6_description
        if self.game7_image.frame.contains_point(touch.location):
            self.animate_help_to_info()
            self.placeholder_image.texture = self.game7_image.texture
            self.placeholder_text_label.text = self.game7_description
        
        #move back to help scene
        if self.back_button.frame.contains_point(touch.location):
            self.animate_info_to_help()
        
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
    
    def animate_help_to_info(self):
        # move all items up
        for item in self.scene_items:
            item_move_action = Action.move_to(item.position.x,
                                              item.position.y + self.size_of_screen_y,
                                              self.item_move_speed,
                                              TIMING_SINODIAL)
            item.run_action(item_move_action)
    
    def animate_info_to_help(self):
        # move all items up
        for item in self.scene_items:
            item_move_action = Action.move_to(item.position.x,
                                              item.position.y - self.size_of_screen_y,
                                              self.item_move_speed,
                                              TIMING_SINODIAL)
            item.run_action(item_move_action)
