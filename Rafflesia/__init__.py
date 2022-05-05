import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "0"
import pygame
import glfw

pygame.init()
glfw.init()

__version__ = "0.0.9.1"

from Rafflesia.AudioManager import *
from Rafflesia.UtilsManager import *
