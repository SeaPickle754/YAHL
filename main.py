import curses
from datetime import datetime, timezone
from curses.textpad import Textbox, rectangle
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
    mainloop()
    end_curses()


#Not loop but whatever
def mainloop():
    while(1):
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter QSO callsign CTRL+G to end:", curses.A_REVERSE)
        box = get_input(1, 0, 7, 1) 
        box = box.strip().upper()

        stdscr.addstr(3,0, f"callsign is:{box}, y/n?")
        stdscr.refresh()
        if (stdscr.getkey() == "y"):
            break
    

Begin()
