import os
import datetime
from enum import Enum

class track:
    '''Store data read from DHT sensor.'''
    class _dlmtrs_(Enum):
        '''private enum for file delimiters'''
        TABS="\t"
        COMM=","
    def __init__(self, delim=None, filenom="room.t"):
        if os.path.isfile(filenom) or delim not in [e.value for e in _dlmtrs_.values]:
            delim = None
        if delim is None:
            
        file = open(filenom, "w+")
        line = ""
        
    def print(self, temp=None, humidity=None, time=None):
        if time is None:
            line+=_delim_(datetime.datetime.now())
        else:
            line+=_delim_(time)
    def _delim_(self, strg):
        return strg+"\n"
            

track()
