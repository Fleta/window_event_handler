from time import sleep
from keyEventHandler import pressHoldRelease
import window_manager

VIDEO_SHOW_TIME = 180
MEASURING_INSTRUMENT_SHOW_TIME = 60

def loop(video_window, measuring_instrument_window, flag):
    if(flag):
        sleep(VIDEO_SHOW_TIME)
        measuring_instrument_window.show_window()
    else:
        sleep(MEASURING_INSTRUMENT_SHOW_TIME)
        video_window.show_window()
    # pressHoldRelease('alt', 'tab')

def setup():
    flag = True
    video_window = window_manager.WindowMgr().find_window_wildcard('.**')
    measuring_instrument_window = window_manager.WindowMgr().find_window_wildcard('.**')
    while(True):
        loop(video_window, measuring_instrument_window, flag)
        flag = not flag

setup()