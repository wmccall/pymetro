import argparse

from src.pymetro import PyMetro
from src.consts.metro_consts import (
    DEFAULT_MAP_WIDTH,
    DEFAULT_MAP_HEIGHT,
    DEFAULT_NUM_STATIONS,
    DEFAULT_NUM_LINES,
)

parser = argparse.ArgumentParser(description='Randomly generate a metro map')
parser.add_argument("-x", "--width", help="Width of Map", type=int, default=DEFAULT_MAP_WIDTH)
parser.add_argument("-y", "--height", help="Height of Map", type=int, default=DEFAULT_MAP_HEIGHT)
parser.add_argument("-s", "--stations", help="Num Stations", type=int, default=DEFAULT_NUM_STATIONS)
parser.add_argument("-l", "--lines", help="Num Train Lines", type=int, default=DEFAULT_NUM_LINES)
args = parser.parse_args()

if __name__ == "__main__":
    metro = PyMetro(args.width, args.height, args.stations, args.lines)
    metro.details()
    metro.generate()
    metro.ascii_map()
    metro.plot()