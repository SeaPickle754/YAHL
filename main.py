import curses
from datetime import datetime, timezone
from curses.textpad import Textbox, rectangle
from hamutils.adif import ADIWriter


qso_data = {"QSO callsign":None, "time":None, "date":None, "Sent signal":None, "Received signal": None, "Frequency": None, "Mode":None}  

def init_curses():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
def end_curses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    quit()

# thanks for the code 
# tech with tim
def get_input(x, y, width, height):
    win = curses.newwin(x+width, y+width, x, y)
    box = Textbox(win)
    stdscr.refresh()
    box.edit()
    return box.gather()


#------------------------------------------

def  init_program():
    logscr = curses.newwin(curses.LINES // 2, curses.COLS, curses.LINES//2, 0)
    logscr.clear()
    logscr.addch(0,0,"a")
    logscr.refresh()
    logscr.getkey()
def begin():
    init_curses()
    #init_program()
    try:
        show_tutorial()
        query_for_presets()
        mainloop()
    except:
        end_curses()
    end_curses()
    
def show_tutorial():
    stdscr.clear()
    stdscr.addstr(0,0, "TUTORIAL: KK7OYV's YAHL")
    stdscr.addstr(1,0, "CTRL+P when asked for confirmation to adjust presets")
    stdscr.addstr(2,0, "Enter data, CTRL+G to exit prompt")
    stdscr.addstr(3,0, "Press any key to continue!")
    stdscr.refresh()
    stdscr.getkey()

def query_for_presets():
    stdscr.clear()
    stdscr.addstr(0,0, "Querying for presets: Press CTRL+G to skip preset!", curses.A_BLINK)
    stdscr.refresh()
    stdscr.getkey()
    for data in qso_data.keys(): 
            # this loop should continue until the user says the data is correct
            while(1):
                stdscr.clear()
                stdscr.addstr(0, 0, f"Enter {data} CTRL+G to end:", curses.A_STANDOUT)
                box = get_input(1, 0, 7, 1) 
                box = box.strip().upper()
                if len(box) == 0:
                    break
                stdscr.addstr(3,0, f"{data} is: {box} , y/n?", curses.A_BLINK)
                stdscr.refresh()
                if (stdscr.getkey() == "y"):
                   qso_data[data] = box
                   break
    stdscr.clear()
    stdscr.addstr(0,0, "Presets done, press key to start logging!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()
def convert_freq_to_band(freq):
    freq_Mhz = float(freq)
    freq_Mhz = int(freq_Mhz)
    if freq_Mhz == 1:
        return "160m"
    elif freq_Mhz == 3:
        return "80m"
    elif freq_Mhz == 5:
        return "60m"
    elif freq_Mhz == 7:
        return "40m"
    elif freq_Mhz == 10:
        return "30m"
    elif freq_Mhz == 14:
        return "20m"
    elif freq_Mhz == 18:
        return "17m"
    elif freq_Mhz == 21:
        return "15m"
    elif freq_Mhz == 24:
        return "12m"
    elif freq_Mhz == 28 or freq_Mhz == 29:
        return "10m"


def mainloop():
    for data in qso_data.keys(): 
            if qso_data[data] != None:
                continue
            date = datetime.now(timezone.utc)
            if data == "time":
                qso_data[data] = date
                continue
            
            # this loop should continue until the user says the data is correct
            while(1):
                stdscr.clear()

                stdscr.addstr(0, 0, f"Enter {data} CTRL+G to end:", curses.A_STANDOUT)
                box = get_input(1, 0, 7, 1) 
                box = box.strip().upper()
                
                stdscr.addstr(3,0, f"{data} is: {box} , y/n?", curses.A_BLINK)
                stdscr.refresh()
                key = stdscr.getkey()
                if (key == "y"):
                   qso_data[data] = box
                   break
                # ctrl+p == redo presets
                if (ord(key[0]) == 16):
                    query_for_presets()

    adi = ADIWriter(open("test.adif", "wb"))
    adi.add_qso(call = qso_data["QSO callsign"], datetime_on = qso_data["time"], band = convert_freq_to_band(qso_data["Frequency"]), mode = qso_data["Mode"])
    stdscr.addstr((curses.LINES - 1), 0, "Contacts: 1", curses.color_pair(1))
    stdscr.refresh()
    key = stdscr.getkey()
    if key == "q":
        return
    mainloop()
begin()
