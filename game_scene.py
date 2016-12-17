# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
# Edited by: Matthew Lourenco
# Dec 14 2016: created game scene. made scene read file to determine scale of sprites
# Dec 15 2016: game 1, 2, and 3 functional
# Dec 16 2016: game 4, 5, and 6 functional
# Dec 17 2016: removed scaling of sprites

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
        
        #temp properties to fix errors
        self.menu_button = LabelNode(text = '', color = 'clear', position = (-100, -100), z_position = 0, parent = self)
        self.menu_button_scale = 0
        self.menu_text = LabelNode(text = '', color = 'clear', position = (-100, -100), z_position = 0, parent = self)
        self.menu_text_scale = 0
        
        # properties
        self.game_over = False
        self.meteor_on_screen = False
        self.game2_count_to_five = False
        self.game2_count = 0
        self.game2_pause_counter = False
        self.game2_pause_count = 0
        self.game3_timer_count = 0
        self.game4_slider_touched = False
        self.game4_slider_move_speed = 0.1
        self.game5_timer_count = 0
        
        # create a timer to keep track of how far the player has progressed
        self.start_time = time.time()
        
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
        
        # keep track of which games are active
        if time.time() - self.start_time > 15 and not self.game2.get_game_active() and not self.game_over:
            self.game2.activate_game()
            #pass
        
        if time.time() - self.start_time > 30 and not self.game3.get_game_active() and not self.game_over:
            self.game3.activate_game()
            self.game3.create_shape(self)
            #pass
        
        if time.time() - self.start_time > 45 and not self.game4.get_game_active() and not self.game_over:
            self.game4.activate_game()
            #pass
        
        if time.time() - self.start_time > 60 and not self.game5.get_game_active() and not self.game_over:
            self.game5.activate_game()
            self.game5.create_shape(self)
            #pass
        
        if time.time() - self.start_time > 75 and not self.game6.get_game_active() and not self.game_over:
            self.game6.activate_game()
            self.game6.create_truck(self)
            #pass
        
        # game 1
        random_game_action_chance = random.randint(0, 500)
        if self.game1.get_game_active() and not self.meteor_on_screen and not self.game_over and random_game_action_chance < 10:
            self.game1.create_meteor(self)
            self.meteor_on_screen = True
        
        for meteor in self.game1.get_meteors():
            if meteor.frame.intersects(self.game1.get_power_core().frame) and not self.game_over:
                self.end_game()
        
        # game 2
        if self.game2.get_game_active() and self.game2.get_button_is_red() and not self.game2.get_game_paused() and not self.game_over and random_game_action_chance >= 10 and random_game_action_chance < 16:
            self.game2.make_button_green()
            self.game2_count_to_five = True
            self.game2.get_timer().text = '5'
        
        if self.game2_count_to_five and not self.game_over:
            self.game2_count = self.game2_count + 1
        
        if self.game2_count == 30 and not self.game_over:
            self.game2.get_timer().text = '4'
        if self.game2_count == 60 and not self.game_over:
            self.game2.get_timer().text = '3'
        if self.game2_count == 90 and not self.game_over:
            self.game2.get_timer().text = '2'
        if self.game2_count == 120 and not self.game_over:
            self.game2.get_timer().text = '1'
        if self.game2_count == 150 and not self.game_over:
            self.game2_count_to_five = False
            self.game2.get_timer().text = '0'
            self.end_game()
        
        if self.game2_pause_counter:
            self.game2_pause_count = self.game2_pause_count + 1
            if self.game2_pause_count == 60:
                self.game2_pause_counter = False
                self.game2.set_game_paused(False)
        
        # game 3
        if self.game3.get_game_active() and not self.game_over:
            self.game3_timer_count = self.game3_timer_count + 1
        
        if not self.game_over and self.game3_timer_count == 30:
            self.game3.get_timer().text = '4'
        if not self.game_over and self.game3_timer_count == 60:
            self.game3.get_timer().text = '3'
        if not self.game_over and self.game3_timer_count == 90:
            self.game3.get_timer().text = '2'
        if not self.game_over and self.game3_timer_count == 120:
            self.game3.get_timer().text = '1'
        if not self.game_over and self.game3_timer_count == 150:
            self.game3.get_timer().text = '0'
            self.end_game()
        
        # game 4
        if self.game4.get_game_active() and not self.game_over and not self.game4_slider_touched:
            slider_move_action = Action.move_by(-1, 0, self.game4_slider_move_speed)
            self.game4.get_slider().run_action(slider_move_action)
        
        if not self.game4.get_track().frame.contains_rect(self.game4.get_slider().frame) and self.game4.get_slider().position.x < self.size_of_screen_x * (5/6) and self.game4.get_game_active():
            self.end_game()
        
        # game 5
        if self.game5.get_game_active() and not self.game_over:
            self.game5_timer_count = self.game5_timer_count + 1
        
        if not self.game_over and self.game5_timer_count == 30:
            self.game5.get_timer().text = '4'
        if not self.game_over and self.game5_timer_count == 60:
            self.game5.get_timer().text = '3'
        if not self.game_over and self.game5_timer_count == 90:
            self.game5.get_timer().text = '2'
        if not self.game_over and self.game5_timer_count == 120:
            self.game5.get_timer().text = '1'
        if not self.game_over and self.game5_timer_count == 150:
            self.game5.get_timer().text = '0'
            self.end_game()
        
        # game 6
        if self.game6.get_truck().position.y < -90 and self.game6.get_game_active() and not self.game_over:
            self.game6.create_truck(self)
        
        if self.game6.get_player_car().frame.intersects(self.game6.get_truck().frame) and not self.game_over and self.game6.get_game_active():
            self.end_game()
        
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.game_over:
            if self.menu_button.frame.contains_point(touch.location):
                self.menu_button.scale = self.menu_button.scale * 0.9
                self.menu_text.scale = self.menu_text.scale * 0.9
        
        # game 2
        if self.game2.get_game_active() and not self.game_over and self.game2.get_button().frame.contains_point(touch.location):
            self.game2.get_button().scale = self.game2.get_button().scale * 0.9
            self.game2.get_button_shadow().scale = self.game2.get_button_shadow().scale * 0.9
        
        # game 4
        if self.game4.get_slider().frame.contains_point(touch.location) and not self.game_over:
            self.game4_slider_touched = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # game 4
        if self.game4.get_track().frame.contains_point(touch.location) and self.game4_slider_touched:
            self.game4.get_slider().position = Vector2(touch.location.x, self.game4.get_slider_y())
        
        
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # reset scale of buttons
        if self.game_over:
            self.menu_button.scale = self.menu_button_scale
            self.menu_text.scale = self.menu_text_scale
            # dismiss scene when menu button pressed
            if self.menu_button.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
        
        # game 1
        for meteor in self.game1.get_meteors():
            if meteor.frame.contains_point(touch.location) and not self.game_over:
                meteor.remove_from_parent()
                self.game1.get_meteors().remove(meteor)
                self.meteor_on_screen = False
        
        # game 2
        self.game2.get_button().scale = 1
        self.game2.get_button_shadow().scale = 1
        
        if not self.game_over and self.game2.get_game_active() and self.game2.get_button().frame.contains_point(touch.location):
            if self.game2.get_button_is_red():
                self.end_game()
            elif not self.game2.get_button_is_red():
                self.game2.make_button_red()
                self.game2_count_to_five = False
                self.game2_count = 0
                self.game2.get_timer().text = ''
                self.game2.set_game_paused(True)
                self.game2_pause_counter = True
                self.game2_pause_count = 0
        
        # game 3
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_one().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 1:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_count = 0
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                else:
                    self.end_game()
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_two().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 2:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_count = 0
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                else:
                    self.end_game()
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_three().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 3:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_count = 0
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                else:
                    self.end_game()
        
        # game 4
        self.game4_slider_touched = False
        
        # game 5
        if not self.game_over and self.game5.get_game_active() and self.game5.get_diamond_button().frame.contains_point(touch.location):
            if self.game5.get_shape_type() == 1:
                self.game5.get_incoming_shape().remove_from_parent()
                self.game5.get_timer().text = '5'
                self.game5_timer_count = 0
                self.game5.create_shape(self)
            else:
                self.end_game()
        if not self.game_over and self.game5.get_game_active() and self.game5.get_square_button().frame.contains_point(touch.location):
            if self.game5.get_shape_type() == 2:
                self.game5.get_incoming_shape().remove_from_parent()
                self.game5.get_timer().text = '5'
                self.game5_timer_count = 0
                self.game5.create_shape(self)
            else:
                self.end_game()
        
        # game 6
        if not self.game_over and self.game6.get_game_active() and self.game6.get_left_arrow().frame.contains_point(touch.location):
            player_car_move_action = Action.move_to(self.size_of_screen_x * (19/24), self.game6.get_player_car().position.y, 1.0, TIMING_SINODIAL)
            self.game6.get_player_car().run_action(player_car_move_action)
        
        if not self.game_over and self.game6.get_game_active() and self.game6.get_right_arrow().frame.contains_point(touch.location):
            player_car_move_action = Action.move_to(self.size_of_screen_x * (21/24), self.game6.get_player_car().position.y, 1.0, TIMING_SINODIAL)
            self.game6.get_player_car().run_action(player_car_move_action)
        
        
        
    
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
        self.game_over = True
        self.game1.game_over()
        self.game2.game_over()
        self.game3.game_over()
        self.game4.game_over()
        self.game5.game_over()
        self.game6.game_over()
        self.game7.game_over()
        
        # remove temp variables
        self.menu_button.remove_from_parent()
        self.menu_text.remove_from_parent()
        
        # add 'game over' text
        game_over_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * 0.7)
        self.game_over_text = LabelNode(text = 'Game Over',
                                        font = ('futura', 120),
                                        color = '#49db56',
                                        parent = self,
                                        position = game_over_position,
                                        z_position = 15,
                                        scale = self.scale_of_sprites)
        # add menu button
        menu_button_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        menu_button_size = Vector2(self.size_of_screen_x * 0.4, self.size_of_screen_y * 0.15)
        menu_button_shape = ui.Path.rounded_rect(0, 0, menu_button_size.x, menu_button_size.y, 60)
        menu_button_shape.line_width = 10 * self.scale_of_sprites
        self.menu_button_scale = self.scale_of_sprites
        self.menu_button = ShapeNode(path = menu_button_shape,
                                     fill_color = '#5564ff',
                                     stroke_color = '#4652d1',
                                     parent = self,
                                     position = menu_button_position,
                                     z_position = 14,
                                     scale = self.menu_button_scale)
        # add menu text
        self.menu_text_scale = self.scale_of_sprites
        self.menu_text = LabelNode(text = 'MENU',
                                   color = '#e2e2e2',
                                   font = ('futura', 60),
                                   parent = self,
                                   position = menu_button_position,
                                   z_position = 15,
                                   scale = self.menu_text_scale)
        
    
