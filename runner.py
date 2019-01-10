from time import sleep
from keyEventHandler import pressHoldRelease

VIDEO_SHOW_TIME = 180
MEASURING_INSTRUEMENT_SHOW_TIME = 60

def loop(flag):
    if(flag):
        sleep(VIDEO_SHOW_TIME)
    else:
        sleep(MEASURING_INSTRUEMENT_SHOW_TIME)
    pressHoldRelease('alt', 'tab')

def setup():
    flag = True
    while(True):
        loop(flag)
        flag = not flag

setup()