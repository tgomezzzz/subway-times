from graphics import *
from selector import *
from train import *

UP = -1
DOWN = 1

def showTimes():
    win = GraphWin('Subway Times', 1200, 700, autoflush=False)
    win.setBackground("black")

    train_selector = Selector(20, 20, 100, 100, [], win)
    center = train_selector.getCenter()
    r = 40

    train_selector.addOption(Tr1(center, r, win))
    train_selector.addOption(Tr2(center, r, win))
    train_selector.addOption(Tr3(center, r, win))
    train_selector.addOption(Tr4(center, r, win))
    train_selector.addOption(Tr5(center, r, win))
    train_selector.addOption(Tr6(center, r, win))
    train_selector.addOption(Tr7(center, r, win))
    train_selector.addOption(TrA(center, r, win))
    train_selector.addOption(TrC(center, r, win))
    train_selector.addOption(TrE(center, r, win))
    train_selector.addOption(TrN(center, r, win))
    train_selector.addOption(TrQ(center, r, win))
    train_selector.addOption(TrR(center, r, win))
    train_selector.addOption(TrW(center, r, win))
    train_selector.addOption(TrB(center, r, win))
    train_selector.addOption(TrD(center, r, win))
    train_selector.addOption(TrF(center, r, win))
    train_selector.addOption(TrM(center, r, win))
    train_selector.addOption(TrL(center, r, win))

    while True:
        key = win.checkKey()
        if key == "Up":
            train_selector.selectNext(UP)
        elif key == "Down":
            train_selector.selectNext(DOWN)
        elif key == "Return":
            break

    win.close()


if __name__ == '__main__':
    showTimes()