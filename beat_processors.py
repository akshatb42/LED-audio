import time
import numpy as np
from neopixel import Color

def beat_proc_by_name(name, color_func):
    if name == 'sticky_white':
        return StickyWhite(300, 500, 75, color_func)
    elif name == 'dummy':
        return Dummy()

class Dummy:
    def process(self, strip, val, beat_freq):
        pass

class StickyWhite:
    """
    Makes all lights the same color and sleeps for time proportional to beat intensity
    """
    def __init__(self, delay_multiplier, max_delay, delay_thresh, color_func):
        self.delay_multiplier = delay_multiplier
        self.max_delay = max_delay
        self.delay_thresh = delay_thresh
        self.color_func = color_func

    def process(self, strip, val, beat_freq):
        delay = min(val * self.delay_multiplier, self.max_delay)

        if delay > self.delay_thresh:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.color_func.process(i, val, beat_freq))
            strip.show()

            print "BEAT! Sleeping for ", delay
            time.sleep(delay/1000.0)
