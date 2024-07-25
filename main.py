import curses
from datetime import datetime, timezone
from curses.textpad import Textbox, rectangle

qso_data = {"QSO callsign":None, "time":None, "date":None, "Sent signal":None, "Received signal": None, "Frequency": None, "Mode":None}  

def init_curses():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
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

def begin():
    init_curses()
    show_tutorial()
    query_for_presets()
    mainloop()
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

#Not loop but whatever
def mainloop():
    for data in qso_data.keys(): 
            if qso_data[data] != None:
                continue
            # this loop should continue until the user says the data is correct
            while(1):
                stdscr.clear()
                date = datetime.now(timezone.utc)
                if data == "time":
                    date = date.time()
                    stdscr.addstr(0, 0, f"Enter {data} CTRL+G to end, currently {date.hour}:{date.minute} UTC", curses.A_STANDOUT)
                if data == "date":
                    date = date.date()
                    stdscr.addstr(0,0, f"Enter {data} CTRL+G to end, currently {date.day}/{date.month} (D/M)", curses.A_STANDOUT)
                else:
                    stdscr.addstr(0, 0, f"Enter {data} CTRL+G to end:", curses.A_STANDOUT)
                box = get_input(1, 0, 7, 1) 
                box = box.strip().upper()
                if len(box) == 0:
                   break
                stdscr.addstr(3,0, f"{data} is: {box} , y/n?", curses.A_BLINK)
                stdscr.refresh()
                key = stdscr.getkey()
                if (key == "y"):
                   qso_data[data] = box
                   break
                # ctrl+p == redo presets
                if (ord(key[0]) == 16):
                    query_for_presets()
begin()
