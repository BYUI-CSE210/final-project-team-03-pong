# IMPORT STUFF HERE
from constants import *

from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.point import Point
from game.casting.text import Text
from game.casting.image import Image
from game.casting.label import Label
from game.casting.paddle import Paddle 
from game.casting.scores import Scores
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.collide_walls_action import CollideWallsAction
from game.scripting.control_paddles_action import ControlPaddlesAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_paddles_action import MovePaddlesAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    CONTROL_PADDLES_ACTION = ControlPaddlesAction(KEYBOARD_SERVICE)
    COLLIDE_WALLS_ACTION = CollideWallsAction
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_PADDLES_ACTION = MovePaddlesAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)    
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    

    

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_scores(cast)
        self._add_ball(cast)
        self._add_paddle(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PADDLES_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x = SCREEN_WIDTH + PADDLE_WIDTH + BALL_WIDTH
        y = CENTER_Y
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)


    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SIZE, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)


    def _add_scores(self, cast):
        # Player 1 Score
        cast.clear_actors(SCORES_GROUP)
        text1 = Text(PLAYER_1_SCORE_FORMAT, FONT_FILE, FONT_SIZE, ALIGN_CENTER)
        position1 = Point(CENTER_X - 50, HUD_MARGIN)
        label1 = Label(text1, position1)

        # Player 2 score
        text2 = Text(PLAYER_2_SCORE_FORMAT, FONT_FILE, FONT_SIZE, ALIGN_CENTER)
        position2 = Point(CENTER_X + 50, HUD_MARGIN)
        label2 = Label(text2, position2)

        cast.add_actor(SCORES_GROUP, label1)
        cast.add_actor(SCORES_GROUP, label2) 

    def _add_score_stats(self, cast):
        cast.clear_actors(SCORE_STATS_GROUP)
        score_stats = Scores()
        cast.add_actor(SCORE_STATS_GROUP, score_stats)

    def _add_paddles(self, cast):
        cast.clear_actors(PADDLE_GROUP)
        
        # COMMON ATTRIBUTES
        image = Image(PADDLE_IMAGE, 1, 90)
        size = Point(PADDLE_WIDTH, PADDLE_HEIGHT)
        velocity = Point(0, 0)
        y = CENTER_Y

        # PLAYER 1
        x1 = SCREEN_WIDTH - (PADDLE_WIDTH * 2)
        position1 = Point(x1, y)
        body1 = Body(position1, size, velocity)       
        paddle1 = Paddle(body1, image, True)

        # PLAYER 2
        x2 = SCREEN_WIDTH + (PADDLE_WIDTH * 2)
        position2 = Point(x2, y)
        body2 = Body(position2, size, velocity)       
        paddle2 = Paddle(body2, image, True)


        cast.add_actor(PADDLE_GROUP, paddle1)
        cast.add_actor(PADDLE_GROUP, paddle2)


    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_PADDLES_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_PADDLES_ACTION)
        script.add_action(UPDATE, self.COLLIDE_WALLS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PADDLES_ACTION)
        script.add_action(UPDATE, self.MOVE_PADDLES_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)