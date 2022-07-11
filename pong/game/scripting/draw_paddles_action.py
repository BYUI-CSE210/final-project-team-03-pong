from constants import *
from game.scripting.action import Action


class DrawPaddlesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        body1 = paddles[0].get_body()
        body2 = paddles[1].get_body()
        
        if paddles[0].is_debug():
            rectangle1 = body1.get_rectangle()
            self._video_service.draw_rectangle(rectangle1, PURPLE)

        if paddles[1].is_debug():
            rectangle2 = body2.get_rectangle()
            self._video_service.draw_rectangle(rectangle2, PURPLE)
            
        image1 = paddles[0].get_image()
        position1 = body1.get_position()
        image2 = paddles[1].get_image()
        position2 = body2.get_position()


        self._video_service.draw_image(image1, position1)
        self._video_service.draw_image(image2, position2)