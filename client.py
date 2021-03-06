from color_funcs import *
from beat_processors import *
from val_processors import *
from controller import *
import argparse

HOST = ''
PORT = 6000

def run(color_func, val_proc, beat_proc, beat_colors):
    color_func = color_func_by_name(color_func)
    val_proc = val_proc_by_name(val_proc, color_func)

    beat_colors =  color_func_by_name(beat_colors)
    beat_proc = beat_proc_by_name(beat_proc, beat_colors)

    controller = StripController(HOST, PORT, beat_proc, val_proc)
    controller.run()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run LED strip.')

    parser.add_argument('--beats', dest='beat_proc', default='sticky_white',
            help='beat processor to use (default: sticky_white)')
    parser.add_argument('--vals', dest='val_proc', default='histogram',
            help='val processor to use (default: histogram)')
    parser.add_argument('--colors', dest='color_func', default='color_wheel',
            help='color function to use (default: color_wheel)')
    parser.add_argument('--beat_colors', dest='beat_color', default='white',
            help='color function to use for beats (default: white)')

    args = parser.parse_args()

    run(args.color_func, args.val_proc, args.beat_proc, args.beat_color)
