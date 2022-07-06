from game.casting.color import Color
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SIZE = 32

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/start.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
BLUE = Color(0, 93, 243)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
# UP AND DOWN FOR PLAYER 1 AND 2

# SCENES
NEW_GAME = 0
IN_PLAY = 1
GAME_OVER = 2

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS

# HUD
HUD_MARGIN = 15
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
PLAYER_1_SCORE_FORMAT = f"PLAYER 1: {PLAYER_1_SCORE}"
PLAYER_2_SCORE_FORMAT = f"PLAYER 2: {PLAYER_2_SCORE}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "batter/assets/images/ball.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# PADDLE
PADDLE_GROUP = "paddles"
PADDLE_IMAGE = "batter/assets/images/paddle.png"
PADDLE_WIDTH = 106
PADDLE_HEIGHT = 28
PADDLE_RATE = 6
PADDLE_VELOCITY = 7


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"