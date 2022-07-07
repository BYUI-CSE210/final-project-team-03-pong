from constants import *
from game.scripting.action import Action


class ControlPaddlesAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        paddle1 = paddles[0]
        paddle2 = paddles[1]

        # PLAYER 1 CONTROLS
        if self._keyboard_service.is_key_down(PLAYER_1_UP): 
            paddle1.swing_up()
        elif self._keyboard_service.is_key_down(PLAYER_1_DOWN):
            paddle1.swing_down()
        else: 
            paddle1.stop_moving()

        # PLAYER 2 CONTROLS
        if self._keyboard_service.is_key_down(PLAYER_2_UP): 
            paddle2.swing_up()
        elif self._keyboard_service.is_key_down(PLAYER_2_DOWN): 
            paddle2.swing_down()    
        else:
            paddle2.stop_moving()        