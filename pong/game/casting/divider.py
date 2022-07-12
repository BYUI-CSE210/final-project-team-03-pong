from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class BoardDivider(Actor):
    """A implement used to hit and bounce the ball in the game."""

    def __init__(self, body, image, debug = False):
        """Constructs a center board divder line.

        Args:Args:
            body: A new instance of Body.
            image: A new instance of image.
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the board divider's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """
        Gets the board dividers's body.

        Returns:
            An instance of Image.
        """
        return self._image

    def draw_line(self):
        """Draws the center line"""
        self._body.set_position(Point(CENTER_X, 0))