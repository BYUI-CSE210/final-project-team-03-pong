from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePaddlesAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        paddles = cast.get_actors(PADDLE_GROUP)
        
        ball_body = ball.get_body()
        paddles_body2 = paddles[1].get_body()
        paddles_body1 = paddles[0].get_body()


        if self._physics_service.is_left_of(ball_body, paddles_body2):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound) 

        if self._physics_service.is_right_of(paddles_body1, ball_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)   