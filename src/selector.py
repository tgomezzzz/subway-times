from graphics import *

class Selector:
    def __init__(self, x, y, w, h, options, win):
        self.rect = Rectangle(Point(x, y), Point(x + w, y + h))
        self.rect.setFill(color_rgb(79, 79, 79))
        self.rect.setWidth(4)
        self.rect.setOutline("")
        self.rect.draw(win)
        self.win = win

        self.options = options
        self.selected = [-1, None]
        if len(self.options) > 0:
            self.selected = [0, self.options[0]]
        self.in_use = False

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

    def choose(self):
        self.in_use = True
        self.rect.setOutline('white')

    def unchoose(self):
        self.in_use = False
        self.rect.setOutline('')

    def getCenter(self):
        return self.rect.getCenter()

class TrainSelector(Selector):
    def selectNext(self, dir):
        if len(self.options) == 0:
            return
        return self.setSelected(self.selected[0] + dir)

    def setSelected(self, i):
        super().setSelected(i)
        names, data = self.selected[1].fetchData()
        return names, data

class StationSelector(Selector):
    def selectNext(self, dir):
        if len(self.options) == 0:
            return
        return self.setSelected(self.selected[0] + dir)

    def setSelected(self, i):
        super().setSelected(i)
        return self.selected[1].getText()

    def setOptions(self, options):
        self.options = []
        for option in options:
            textBox = Text(self.getCenter(), option)
            textBox.setFill('white')
            textBox.setSize(36)
            self.options.append(textBox)
        if len(self.options) > 0:
            self.setSelected(0)
        return self.selected[1].getText()