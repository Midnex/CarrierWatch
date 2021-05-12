from dearpygui.core import *
from dearpygui.simple import *
import sys

ver = 0.1
def quit(sender, data):
    sys.exit()

def menuSelection(selection, data):
    if selection == "Settings":
        print("Not available")
    elif selection == "About":
        add_window(
                "About CarrierWatch",
                width=200,
                height=100,
                x_pos=0,
                y_pos=0,
                autosize=False,
                no_resize=True,
                no_move=True,
                no_scrollbar=True,
                no_collapse=True,
                label="About CarrierWatch")


set_main_window_size(400, 200)
set_main_window_resizable(False)
set_main_window_title(f"CarrierWatch v{ver}")
with window("CarrierWatch"):
    with menu_bar("Main Menu Bar"):
        with menu("File"):
            add_menu_item("Exit", callback=quit)
        with menu("Help"):
            add_menu_item("Settings", callback=menuSelection)
            add_menu_item("About", callback=menuSelection)

start_dearpygui(primary_window="CarrierWatch")