from graphics import *

class Selector:
    def __init__(self, x, y, w, h, options, win):
        self.rect = Rectangle(Point(x, y), Point(x + w, y + h))
        self.rect.setFill(color_rgb(79, 79, 79))
        self.rect.setOutline("")
        self.rect.draw(win)
        self.win = win

        self.options = options
        self.selected = [-1, None]
        if len(self.options) > 0:
            self.selected = [0, self.options[0]]
        self.is_selected = False

    def addOption(self, option):
        self.options.append(option)
        if len(self.options) == 1:
            self.setSelected(0)

    def setSelected(self, i):
        # Undraw the currently selected object.
        if self.selected[1] != None:
            self.selected[1].undraw()
        
        self.selected[0] = i
        if self.selected[0] < 0:
            self.selected = [len(self.options) - 1, self.options[len(self.options) - 1]]
        elif self.selected[0] >= len(self.options):
            self.selected = [0, self.options[0]]
        else:
            self.selected[1] = self.options[self.selected[0]]
        self.selected[1].draw(self.win)

    def selectNext(self, dir):
        if len(self.options) == 0:
            return
        self.setSelected(self.selected[0] + dir)

    def getCenter(self):
        return self.rect.getCenter()

class TrainSelector(Selector):
    def setSelected(self, i):
        super().setSelected(i)

class StationSelector(Selector):
    def setSelected(self, i):
        super().setSelected(i)