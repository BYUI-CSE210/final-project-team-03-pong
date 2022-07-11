from constants import *
from game.scripting.action import Action


class DrawScoresAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(SCORE_STATS_GROUP)
        self._draw_label(cast, SCORE_1_GROUP, PLAYER_1_SCORE_FORMAT, stats.get_score(1))
        self._draw_label(cast, SCORE_2_GROUP, PLAYER_2_SCORE_FORMAT, stats.get_score(2))

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)