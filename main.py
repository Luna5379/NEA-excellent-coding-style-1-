import sys

import pygame

from classes.running import *

if __name__ == "__main__":
    try:
        project = running()
        project.run()
    except Exception as exception:
        print(f"Error: {exception}")
        pygame.quit()
        sys.exit()