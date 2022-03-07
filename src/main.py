from guiElements.src.inputs.button import Button
from guiElements.src.inputs.textInput import TextInput
from guiElements.src.inputs.fastMenu import FastMenu
from guiElements.src.window.window import Window
from guiElements.src.window.windowEvents import WindowEvent
import pygame

# other elements
from entityBoard import EntityBoard


SIZE = (800, 600)
FPS = 60
TITLE = "Floppa Editor"

def main():
    
    # window
    root = Window(SIZE, FPS, title=TITLE)

    # events checker
    events = WindowEvent()


    # main menu
    mainMenu = FastMenu(
        [
            Button("New Entity", (60,60,60))
    ])
    # initialize deactivated
    mainMenu.deactivate()


    # text input
    textInput = TextInput((0,0), (60,60,60), "Input")
    textInput.deactivate()


    # the created boards
    boards = []

    while events.getEvent("windowState"):

        # tick the window
        root.tick()

        # fill with white
        root.fill((255,255,255))

        # check for events
        events.eventsCheck()


        # open main menu
        if events.getEvent("mouseButtons")[3]:
            mainMenu.activate(events.getEvent("mousePos"))


        # adding a board
        if mainMenu.getClick(0):
            
            # reset the text input
            textInput.setName("Entity")
            textInput.activate(events.getEvent("mousePos"))

            # close the main menu
            mainMenu.deactivate()



        # get the text to add the board
        if events.getEvent("keyRETURN") and textInput.isActive:

            # append a board object to the list
            boards.append(EntityBoard(textInput.pos, textInput.getText()))

            # deactivate the text input
            textInput.deactivate()
            textInput.clearText()


        # adding text to the input
        textInput.addChar(events.getEvent("keyText"), events.getEvent("keyBACKSPACE"))

        # main menu click events
        mainMenu.clickEvent(events.getEvent("mousePos"), events.getEvent("mouseButtons")[1])

        
        #! DRAWING ELEMENTS

        # main menu
        mainMenu.blit(root)


        # boards
        for board in boards:
            board.blit(root)

        # text input
        textInput.blit(root)


        # update the window
        root.update()


if __name__ == "__main__":

    pygame.init()
    main()
    pygame.quit()