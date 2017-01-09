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
import console
import json
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
        self.game2_timer_time = 0
        self.game2_pause_time = 0
        self.game3_timer_time = 0
        self.game4_slider_touched = False
        self.game4_slider_move_speed = 0.1
        self.game4_score_time = 0
        self.game5_timer_time = 0
        self.game7_player_max_speed = 50
        self.game7_velocity_increase_rate = 6.5
        self.game7_velocity_x = 0
        self.game7_velocity_y = 0
        self.game7_score_time = 0
        
        self.score = 0
        self.score_label_text = 'Score: 000000000'
        
        # create a timer to keep track of how far the player has progressed
        self.start_time = time.time()
        
        # add background color
        background_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        self.background = SpriteNode(position = background_position,
                                     color = '#e5e5e5',
                                     parent = self,
                                     size = self.size)
        # set up scoreboard
        scoreboard_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * (1/100))
        scoreboard_size = Vector2(self.size_of_screen_x * (1/3), self.size_of_screen_y * (1/50))
        scoreboard_shape = ui.Path.rect(0, 0, scoreboard_size.x, scoreboard_size.y)
        self.scoreboard_back = ShapeNode(path = scoreboard_shape,
                                         fill_color = '#4e4e4e',
                                         stroke_color = '#4e4e4e',
                                         parent = self,
                                         position = scoreboard_position,
                                         z_position = 12)
        #add score label
        self.score_label = LabelNode(text = self.score_label_text,
                                     color = 'white',
                                     font = ('futura', 20),
                                     parent = self,
                                     position = scoreboard_position,
                                     z_position = 13)
        # set up 7 games
        self.game1 = GameOne(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (5/6))
        self.game2 = GameTwo(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (5/6))
        self.game3 = GameThree(self, self.size_of_screen_x * (1/6), self.center_of_screen_y)
        self.game4 = GameFour(self, self.size_of_screen_x * (5/6), self.center_of_screen_y)
        self.game5 = GameFive(self, self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/6))
        self.game6 = GameSix(self, self.size_of_screen_x * (5/6), self.size_of_screen_y * (1/6))
        self.game7 = GameSeven(self, self.center_of_screen_x, self.center_of_screen_y)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # keep track of which games are active
        if time.time() - self.start_time > 0 and not self.game1.get_game_active() and not self.game_over:
            self.game1.activate_game()
            #pass
        
        if time.time() - self.start_time > 15 and not self.game2.get_game_active() and not self.game_over:
            self.game2.activate_game()
            self.game2.make_button_green()
            self.game2_timer_time = time.time()
            self.game2.get_timer().text = '5'
            #pass
        
        if time.time() - self.start_time > 30 and not self.game3.get_game_active() and not self.game_over:
            self.game3.activate_game()
            self.game3.create_shape(self)
            self.game3_timer_time = time.time()
            #pass
        
        if time.time() - self.start_time > 45 and not self.game4.get_game_active() and not self.game_over:
            self.game4.activate_game()
            #pass
        
        if time.time() - self.start_time > 70 and not self.game5.get_game_active() and not self.game_over:
            self.game5.activate_game()
            self.game5.create_shape(self)
            self.game5_timer_time = time.time()
            #pass
        
        if time.time() - self.start_time > 100 and not self.game6.get_game_active() and not self.game_over:
            self.game6.activate_game()
            self.game6.create_truck(self)
            #pass
        
        if time.time() - self.start_time > 5 and not self.game7.get_game_active() and not self.game_over:
            self.game7.activate_game()
            self.game7.create_mine(self)
            self.game7.create_mine(self)
            self.game7.create_mine(self)
            self.game7_score_time = time.time()
            #pass
        
        # game 1
        random_game_action_chance = random.randint(0, 500)
        if self.game1.get_game_active() and not self.meteor_on_screen and not self.game_over and random_game_action_chance < 10:
            self.game1.create_meteor(self)
            self.meteor_on_screen = True
        
        if self.game1.get_meteor().frame.intersects(self.game1.get_power_core().frame) and not self.game_over:
            self.end_game()
        
        # game 2
        if self.game2.get_game_active() and self.game2.get_button_is_red() and not self.game2.get_game_paused() and not self.game_over and random_game_action_chance >= 10 and random_game_action_chance < 16:
            self.game2.make_button_green()
            self.game2.get_timer().text = '5'
            self.game2_timer_time = time.time()
        
        if time.time() - self.game2_timer_time > 1 and self.game2.get_timer().text == '5' and not self.game_over:
            self.game2.get_timer().text = '4'
        if time.time() - self.game2_timer_time > 2 and self.game2.get_timer().text == '4' and not self.game_over:
            self.game2.get_timer().text = '3'
        if time.time() - self.game2_timer_time > 3 and self.game2.get_timer().text == '3' and not self.game_over:
            self.game2.get_timer().text = '2'
        if time.time() - self.game2_timer_time > 4 and self.game2.get_timer().text == '2' and not self.game_over:
            self.game2.get_timer().text = '1'
        if time.time() - self.game2_timer_time > 5 and self.game2.get_timer().text == '1' and not self.game_over:
            self.game2.get_timer().text = '0'
            self.end_game()
        
        if self.game2.get_game_paused():
            if time.time() - self.game2_pause_time > 2:
                self.game2.set_game_paused(False)
        
        # game 3
        if time.time() - self.game3_timer_time > 1 and self.game3.get_timer().text == '5' and self.game3.get_game_active() and not self.game_over:
            self.game3.get_timer().text = '4'
        if time.time() - self.game3_timer_time > 2 and self.game3.get_timer().text == '4' and self.game3.get_game_active() and not self.game_over:
            self.game3.get_timer().text = '3'
        if time.time() - self.game3_timer_time > 3 and self.game3.get_timer().text == '3' and self.game3.get_game_active() and not self.game_over:
            self.game3.get_timer().text = '2'
        if time.time() - self.game3_timer_time > 4 and self.game3.get_timer().text == '2' and self.game3.get_game_active() and not self.game_over:
            self.game3.get_timer().text = '1'
        if time.time() - self.game3_timer_time > 5 and self.game3.get_timer().text == '1' and self.game3.get_game_active() and not self.game_over:
            self.game3.get_timer().text = '0'
            self.end_game()
        
        # game 4
        if self.game4.get_game_active() and not self.game_over and not self.game4_slider_touched:
            slider_move_action = Action.move_by(-1, 0, self.game4_slider_move_speed)
            self.game4.get_slider().run_action(slider_move_action)
        
        if not self.game4.get_track().frame.contains_rect(self.game4.get_slider().frame) and self.game4.get_slider().position.x < self.size_of_screen_x * (5/6) and self.game4.get_game_active():
            self.end_game()
        
        if time.time() - self.game4_score_time > 1 and self.game4.get_game_active():
            self.add_to_score(20)
            self.game4_score_time = time.time()
        
        # game 5
        if time.time() - self.game5_timer_time > 1 and self.game5.get_timer().text == '5' and self.game5.get_game_active() and not self.game_over:
            self.game5.get_timer().text = '4'
        if time.time() - self.game5_timer_time > 2 and self.game5.get_timer().text == '4' and self.game5.get_game_active() and not self.game_over:
            self.game5.get_timer().text = '3'
        if time.time() - self.game5_timer_time > 3 and self.game5.get_timer().text == '3' and self.game5.get_game_active() and not self.game_over:
            self.game5.get_timer().text = '2'
        if time.time() - self.game5_timer_time > 4 and self.game5.get_timer().text == '2' and self.game5.get_game_active() and not self.game_over:
            self.game5.get_timer().text = '1'
        if time.time() - self.game5_timer_time > 5 and self.game5.get_timer().text == '1' and self.game5.get_game_active() and not self.game_over:
            self.game5.get_timer().text = '0'
            self.end_game()
        
        # game 6
        if self.game6.get_truck().position.y < -90 and self.game6.get_game_active() and not self.game_over:
            self.game6.get_truck().remove_from_parent()
            self.game6.create_truck(self)
            self.add_to_score(50000)
        
        if self.game6.get_player_car().frame.intersects(self.game6.get_truck().frame) and not self.game_over and self.game6.get_game_active():
            self.end_game()
        
        # game 7
        if gravity().x > 0.05 and self.game7.get_game_active() and not self.game_over:
            self.game7_velocity_y = min(self.game7_velocity_y + self.game7_velocity_increase_rate * gravity().x, self.game7_player_max_speed)
        
        if self.game7.get_player().position.y > self.size_of_screen_y * (23/24) and self.game7_velocity_y > 0:
            self.game7_velocity_y = 0
        
        if gravity().x < -0.05 and self.game7.get_game_active() and not self.game_over:
            self.game7_velocity_y = max(self.game7_velocity_y + self.game7_velocity_increase_rate * gravity().x, -self.game7_player_max_speed)
        
        if self.game7.get_player().position.y < self.size_of_screen_y * (1/24) and self.game7_velocity_y < 0:
            self.game7_velocity_y = 0
        
        if gravity().y > 0.05 and self.game7.get_game_active() and not self.game_over:
            self.game7_velocity_x = max(self.game7_velocity_x - self.game7_velocity_increase_rate * gravity().y, -self.game7_player_max_speed)
        
        if self.game7.get_player().position.x < self.size_of_screen_x * (9/24) and self.game7_velocity_x < 0:
            self.game7_velocity_x = 0
        
        if gravity().y < -0.05 and self.game7.get_game_active() and not self.game_over:
            self.game7_velocity_x = min(self.game7_velocity_x - self.game7_velocity_increase_rate * gravity().y, self.game7_player_max_speed)
        
        if self.game7.get_player().position.x > self.size_of_screen_x * (15/24) and self.game7_velocity_x > 0:
            self.game7_velocity_x = 0
        
        if not self.game_over:
            player_move_action = Action.move_by(self.game7_velocity_x, self.game7_velocity_y)
            self.game7.get_player().run_action(player_move_action)
        
        if len(self.game7.get_mines()) >= 3:
            self.game7.get_mines()[0].alpha = self.game7.get_mines()[0].alpha - 0.1
            if self.game7.get_mines()[0].alpha < 0.1:
                self.game7.get_mines()[0].remove_from_parent()
                self.game7.get_mines().remove(self.game7.get_mines()[0])
        
        if random_game_action_chance > 100 and random_game_action_chance < 111 and self.game7.get_game_active() and len(self.game7.get_mines()) < 3 and not self.game_over:
            self.game7.create_mine(self)
        
        for mine in self.game7.get_mines():
            if mine.frame.intersects(self.game7.get_player().frame) and not self.game_over:
                self.end_game()
        
        if time.time() - self.game7_score_time > 1 and self.game7.get_game_active():
            self.add_to_score(1000)
            self.game7_score_time = time.time()
    
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
        if self.game1.get_meteor().frame.contains_point(touch.location) and not self.game_over:
            self.game1.get_meteor().remove_from_parent()
            self.meteor_on_screen = False
            self.add_to_score(100)
        
        # game 2
        self.game2.get_button().scale = 1
        self.game2.get_button_shadow().scale = 1
        
        if not self.game_over and self.game2.get_game_active() and self.game2.get_button().frame.contains_point(touch.location):
            if self.game2.get_button_is_red():
                self.end_game()
            elif not self.game2.get_button_is_red():
                self.game2.make_button_red()
                self.game2.get_timer().text = ''
                self.game2.set_game_paused(True)
                self.game2_pause_time = time.time()
                self.add_to_score(150)
        
        # game 3
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_one().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 1:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_time = time.time()
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                    self.add_to_score(200)
                else:
                    self.end_game()
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_two().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 2:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_time = time.time()
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                    self.add_to_score(200)
                else:
                    self.end_game()
        if not self.game_over and self.game3.get_game_active() and self.game3.get_button_three().frame.contains_point(touch.location):
            for shape in self.game3.get_incoming_shape():
                if self.game3.get_shape_type() == 3:
                    shape.remove_from_parent()
                    self.game3.get_incoming_shape().remove(shape)
                    self.game3_timer_time = time.time()
                    self.game3.get_timer().text = '5'
                    self.game3.create_shape(self)
                    self.add_to_score(200)
                else:
                    self.end_game()
        
        # game 4
        self.game4_slider_touched = False
        
        # game 5
        if not self.game_over and self.game5.get_game_active() and self.game5.get_diamond_button().frame.contains_point(touch.location):
            if self.game5.get_shape_type() == 1:
                self.game5.get_incoming_shape().remove_from_parent()
                self.game5.get_timer().text = '5'
                self.game5_timer_time = time.time()
                self.game5.create_shape(self)
                self.add_to_score(500)
            else:
                self.end_game()
        if not self.game_over and self.game5.get_game_active() and self.game5.get_square_button().frame.contains_point(touch.location):
            if self.game5.get_shape_type() == 2:
                self.game5.get_incoming_shape().remove_from_parent()
                self.game5.get_timer().text = '5'
                self.game5_timer_time = time.time()
                self.game5.create_shape(self)
                self.add_to_score(500)
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
        # add score text
        score_text_position = Vector2(self.center_of_screen_x, self.size_of_screen_y * (0.3))
        self.score_text = LabelNode(text = self.score_label_text,
                                    font = ('futura', 90),
                                    color = '#ffd12b',
                                    parent = self,
                                    position = score_text_position,
                                    z_position = 14,
                                    scale = self.scale_of_sprites)
        # add console alert to enter a name
        self.player_name = console.input_alert('What is your name?', 'Enter your name', '', 'This is my name', hide_cancel_button = True)
        
        if self.player_name == '':
            self.player_name = 'guest'
        
        self.player_name = str(self.player_name).upper() + ' - '
        
        # write player name to file
        
        score_added = False
        
        high_scores_file = open('./high_scores.txt', 'r+')
        high_scores_table = json.load(high_scores_file)
        for element in range(0, len(high_scores_table)):
            if not score_added and high_scores_table[element][1] < self.score:
                high_scores_table.insert(element, [self.player_name, self.score])
                score_added = True
        if not score_added:
            high_scores_table.append([self.player_name, self.score])
        high_scores_file.seek(0)
        json.dump(high_scores_table, high_scores_file)
        high_scores_file.close()
    
    def add_to_score(self, amount_to_add):
        #adds to the score
        
        self.score = self.score + amount_to_add
        
        self.score_label_text = 'Score: ' + str(self.score).zfill(9)
        self.score_label.text = self.score_label_text
