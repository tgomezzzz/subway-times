from graphics import *
from selector import *
from train import *

UP = -1
DOWN = 1

TRAINS = 0
STATIONS = 1

uptown_times = []
downtown_times = []

def setDisplayTimes(station):
    station.sort()
    for i in range(0, len(uptown_times)):
        up_time = station.uptownTime(i)
        down_time = station.downtownTime(i)
        up_text = str(up_time) + ' min'
        down_text = str(down_time) + ' min'
        if up_time == -1:
            up_text = ''
        elif up_time < 1:
            up_text = 'Arriving'
        if down_time == -1:
            down_text = ''
        elif down_time < 1:
            down_text = 'Arriving'
        uptown_times[i].setText(up_text)
        downtown_times[i].setText(down_text)

def showTimes():
    win = GraphWin('Subway Times', 1200, 700, autoflush=False)
    win.setBackground("black")

    uptown_text = Text(Point(255, 160), "Next uptown trains arriving in:")
    uptown_text.setFill('white')
    uptown_text.setSize(36)
    uptown_text.draw(win)
    downtown_text = Text(Point(280, 400), "Next downtown trains arriving in:")
    downtown_text.setFill('white')
    downtown_text.setSize(36)
    downtown_text.draw(win)

    for i in range(0, 3):
        up_text = Text(Point(200 + (i * 400), 250), '')
        up_text.setFill('white')
        up_text.setSize(36)
        up_text.draw(win)
        uptown_times.append(up_text)

        down_text = Text(Point(200 + (i * 400), 500), '')
        down_text.setFill('white')
        down_text.setSize(36)
        down_text.draw(win)
        downtown_times.append(down_text)  
    
    train_selector = TrainSelector(20, 20, 100, 100, [], win)
    station_selector = StationSelector(140, 20, 1020, 100, [], win)
    selectors = [train_selector, station_selector]
    selected = 0
    train_selector.choose()

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
    train_selector.addOption(TrJ(center, r, win))
    train_selector.addOption(TrZ(center, r, win))
    train_selector.addOption(TrG(center, r, win))

    init = train_selector.selected[1].fetchData()
    names = init[0]
    data = init[1]
    selectors[STATIONS].setOptions(names)
    setDisplayTimes(data['Van Cortlandt Park-242 St'])

    while True:
        key = win.checkKey()
        if key == "Up":
            if selected == TRAINS:
                names, data = selectors[selected].selectNext(UP)
                station = selectors[STATIONS].setOptions(names)
                setDisplayTimes(data[station])
            else:
                station = selectors[selected].selectNext(UP)
                setDisplayTimes(data[station])
        elif key == "Down":
            if selected == TRAINS:
                names, data = selectors[selected].selectNext(DOWN)
                station = selectors[STATIONS].setOptions(names)
                setDisplayTimes(data[station])
            else:
                station = selectors[selected].selectNext(DOWN)
                setDisplayTimes(data[station])
        elif key == "Right" or key == "Left":
            selectors[selected].unchoose()
            selected = 1 - selected
            selectors[selected].choose()
        elif key == "Return":
            break

    win.close()

if __name__ == '__main__':
    showTimes()