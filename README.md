# connect-four

## Overview

A Connect Four game in Python. It uses [NumPy](https://numpy.org/) to create a 2-dimensional array to act as the game board. It has two versions:

* connect-four-cmd, which runs in the terminal and prints the 2-dimensional array out after each turn.
* connect-four, which uses [PyGame](https://www.pygame.org/wiki/about) to create a GUI.

Both the terminal and GUI versions of the game are able to use custom board sizes, entered by the player at the start of the game. They will verify that there is a minimum required number of rows and columns, and will crash the game if the inputs are not valid.
