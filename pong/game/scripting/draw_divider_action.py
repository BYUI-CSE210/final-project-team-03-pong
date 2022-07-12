from constants import *
from game.scripting.action import Action


class DrawDividerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        divider = cast.get_first_actor(DIVIDER_GROUP)
        image = divider.get_image()
        position = divider.get_body().get_position()
        self._video_service.draw_image(image, position)