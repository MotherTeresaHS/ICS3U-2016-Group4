# Created By: Matthew Lourenco
# Created on: 14 Dec 2016
# This is a class that defines game two

from __future__ import division
from scene import *
import ui
from generic_game import *

class GameTwo(GenericGame):
    # this class is game two
    
    def __init__(self, input_parent, game_position_x = 100, game_position_y = 100):
        # This method is called when a game object is called
        
        GenericGame.__init__(self, input_parent, game_position_x, game_position_y)
