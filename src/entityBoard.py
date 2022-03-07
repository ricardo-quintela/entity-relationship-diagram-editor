from pygame import Surface, draw
from guiElements.src.inputs.label import Label
from guiElements.src.inputs.fastMenu import FastMenu
from guiElements.src.inputs.button import Button
from guiElements.src.inputs.textInput import TextInput

class EntityBoard:
    def __init__(self, pos:tuple, title:str) -> None:
        """Constructor of the class EntityBoard

        Parameters
        ----------
        pos : tuple
            the position of the board
        title : str
            the title of the board
        """

        self._pos = pos
        self._title = title

        # the board surface
        self._surface = self.draw()

        # the attributes
        self._attributes = []

        # the attribute's keys
        self.keys = []

    
    def draw(self) -> Surface:
        """Draws a rectangular board with the title, attributes and keys

        Returns
        -------
        Surface
            the drawn surface
        """

        title = Label(self._title, (0,0,0), 20, True)

        surface = Surface((title.size[0] + 10, title.size[1] + 10))

        surface.fill((255,255,255))

        draw.rect(surface, (0,0,0), (0,0,surface.get_width() - 1, surface.get_height() - 1), 2)

        title.blit(surface, (5, 5))

        return surface

    
    def blit(self, canvas: Surface):
        """Draws the board on the given surface

        Parameters
        ----------
        canvas : Surface
            the surface where to draw the board
        """

        canvas.blit(self._surface, self._pos)
