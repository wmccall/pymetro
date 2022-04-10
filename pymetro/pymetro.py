from datetime import datetime

from matplotlib import pyplot

from pymetro.consts.metro_consts import (
    DEFAULT_MAP_WIDTH,
    DEFAULT_MAP_HEIGHT,
    DEFAULT_NUM_STATIONS,
    DEFAULT_NUM_LINES,
    DEFAULT_NUM_HUBS,
    DEFAULT_DEBUG_MODE,
)
from pymetro.utils.metro_utils import (
    generate_stations,
    generate_lines,
)

class PyMetro:
    def __init__(self,
                 map_width=DEFAULT_MAP_WIDTH,
                 map_height=DEFAULT_MAP_HEIGHT,
                 num_stations=DEFAULT_NUM_STATIONS,
                 num_lines=DEFAULT_NUM_LINES,
                 num_hubs=DEFAULT_NUM_HUBS,
                 debug=DEFAULT_DEBUG_MODE,
    ):
        self.map_width = map_width
        self.map_height = map_height
        self.num_stations = num_stations
        self.num_lines = num_lines
        self.num_hubs = num_hubs
        self.debug = debug
    
    def details(self):
        print(f"Map Width: {self.map_width}")
        print(f"Map Height: {self.map_height}")
        print(f"Number of Stations: {self.num_stations} (not all will be used)")
        print(f"Number of Train Lines: {self.num_lines}")
        print(f"Number of Hubs: {self.num_hubs}")
        print(f"Debug: {self.debug}")

    def generate(self):
        self.stations = generate_stations(self.map_width, self.map_height, self.num_stations)
        self.tracks_info = generate_lines(self.map_width, self.map_height, self.stations, self.num_lines, self.num_hubs)

    def plot(self):
        pyplot.figure(figsize=(self.map_width*.03, self.map_height*.03))

        stations_x = []
        stations_y = []

        for station in self.stations:
            if station in self.tracks_info['touched_stations'] or self.debug:
                stations_x.append(station['x'])
                stations_y.append(station['y'])

        colors = [[0,0,0]]
        pyplot.scatter(stations_x, stations_y, c=colors, s=30)

        offset = .04
        count = 0

        for line_info in self.tracks_info['lines']:
            line_x = []
            line_y = []

            for station in line_info['line']:
                line_x.append(station['x']+(offset*count))
                line_y.append(station['y']+(offset*count))

            count += 1
            pyplot.plot(line_x, line_y)

        if  self.debug:
            pyplot.show()
        else:
            now = datetime.now()
            pyplot.savefig(f'out/{now.strftime("%m.%d.%Y-%H:%M:%S.jpg")}', dpi=250)