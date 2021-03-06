# Pong

Pong is a classic two-player game based on table tennis. Players control the paddles that move vertically on opposite sides of the screen. Players use the paddles to hit the ball back and forth across the screen. The paddles are controlled using the keyboard, 'q'= up for player 1, 'a'= down for player 1, 'p'= up for player 2 and 'l' = down for player 2. The score is kept at the top of the screen. Points are earned when a player fails to hit the ball back to their opponent. The first player to reach a score of 11 wins.

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- pong              (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies

---

- Python 3.8.0 or higher
- Raylib Python CFFI 3.7

## Authors

---

- Olamilekan Ajibola (aji22001@byui.edu)
- Hannah Mosier(hannah89mosier@byui.edu)
- Paul Agyare(agy21003@byui.edu)
