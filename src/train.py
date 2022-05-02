from graphics import *

BASE_URL = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
URL_SUFFIX = {
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    'A': '-ace',
    'C': '-ace',
    'E': '-ace',
    'N': '-nqrw',
    'Q': '-nqrw',
    'R': '-nqrw',
    'W': '-nqrw',
    'B': '-bdfm',
    'D': '-bdfm',
    'F': '-bdfm',
    'M': '-bdfm',
    'L': '-l'
}

class Train:
    def __init__(self, id, center, r, color, win):
        self.id = id

        self.icon = Circle(center, r)
        self.icon.setFill(color)
        self.icon.setOutline("")

        self.text = Text(center, id)
        self.text.setFill("white")
        self.text.setSize(36)

        self.data = []

    def draw(self, win):
        self.icon.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.icon.undraw()
        self.text.undraw()

class Tr1(Train):
    def __init__(self, center, r, win):
        super().__init__("1", center, r, "red", win)

class Tr2(Train):
    def __init__(self, center, r, win):
        super().__init__("2", center, r, "red", win)

class Tr3(Train):
    def __init__(self, center, r, win):
        super().__init__("3", center, r, "red", win)

class Tr4(Train):
    def __init__(self, center, r, win):
        super().__init__("4", center, r, "green", win)

class Tr5(Train):
    def __init__(self, center, r, win):
        super().__init__("5", center, r, "green", win)

class Tr6(Train):
    def __init__(self, center, r, win):
        super().__init__("6", center, r, "green", win)

class Tr7(Train):
    def __init__(self, center, r, win):
        super().__init__("7", center, r, "purple", win)

class TrA(Train):
    def __init__(self, center, r, win):
        super().__init__("A", center, r, "blue", win)

class TrC(Train):
    def __init__(self, center, r, win):
        super().__init__("C", center, r, "blue", win)

class TrE(Train):
    def __init__(self, center, r, win):
        super().__init__("E", center, r, "blue", win)

class TrN(Train):
    def __init__(self, center, r, win):
        super().__init__("N", center, r, "yellow", win)
        self.text.setFill('black')

class TrQ(Train):
    def __init__(self, center, r, win):
        super().__init__("Q", center, r, "yellow", win)
        self.text.setFill('black')

class TrR(Train):
    def __init__(self, center, r, win):
        super().__init__("R", center, r, "yellow", win)
        self.text.setFill('black')

class TrW(Train):
    def __init__(self, center, r, win):
        super().__init__('W', center, r, "yellow", win)
        self.text.setFill('black')

class TrB(Train):
    def __init__(self, center, r, win):
        super().__init__("B", center, r, "orange", win)

class TrD(Train):
    def __init__(self, center, r, win):
        super().__init__("D", center, r, "orange", win)

class TrF(Train):
    def __init__(self, center, r, win):
        super().__init__("F", center, r, "orange", win)

class TrM(Train):
    def __init__(self, center, r, win):
        super().__init__("M", center, r, "orange", win)

class TrL(Train):
    def __init__(self, center, r, win):
        super().__init__("L", center, r, "grey", win)