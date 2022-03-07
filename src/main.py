from guiElements.src.window.window import Window
from guiElements.src.window.windowEvents import WindowEvent
import pygame


SIZE = (800, 600)
FPS = 60
TITLE = "Floppa Editor"

def main():
    
    # window
    root = Window(SIZE, FPS, title=TITLE)

    # events checker
    events = WindowEvent()

    while events.getEvent("windowState"):

        # check for events
        events.eventsCheck()

        # update the window
        root.tick()
        root.fill((255,255,255))
        root.update()


if __name__ == "__main__":
    main()