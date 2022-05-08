# NYC Subway Arrival Times Display
This repository uses a Python graphics library to display the next three arrival times of trains at any NYC subway station. The selected train line can be switched to any desired train, and from there the station can be set to any station on that line. It uses [MTA's public real-time API](https://api.mta.info/#/landing) to fetch the most recent subway data. To use the display, you'll first need to [get an API key](https://api.mta.info/#/signup) and enter it into a file named `key.txt` in the home directory. The program reads this key and passes it to the API for authentication. Then, just run `python3 subway_times.py` to get real-time subway data!
![CU](https://github.com/tgomezzzz/subway-times/blob/main/cu_stop.png)  
![Bushwick-Aberdeen](https://github.com/tgomezzzz/subway-times/blob/main/alexs_stop.png)  
Eventually, this program will be run on an arduino, and the display will show on an LED matrix rather than on a laptop screen. See the [blog post](https://medium.com/@tjk2132/nyc-subway-times-display-b61a236da606) for more information!
