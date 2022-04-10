import unittest

from parameterized import parameterized

from pymetro.utils.metro_utils import (
    calculate_y_intercept,
    calculate_dist_from_line,
)

class TestMetroUtils(unittest.TestCase):

    @parameterized.expand([
        [{'x': 1, 'y': 1}, {'x_vec': 1, 'y_vec': 1}, 0],
        [{'x': 3, 'y': 2}, {'x_vec': 1, 'y_vec': -2}, 8],
        [{'x': -8, 'y': 12}, {'x_vec': 4, 'y_vec': -5}, 2],
        [{'x': 8, 'y': 2}, {'x_vec': 8, 'y_vec': 1}, 1],
    ])
    def test_calculate_y_intercept(self, root_station, vector, expected):
        self.assertEqual(expected, calculate_y_intercept(root_station, vector))

    @parameterized.expand([
        [{'x': 1, 'y': 1}, {'x': 0, 'y': 0}, {'x_vec': 1, 'y_vec': 0}, 1],
        [{'x': -1, 'y': -1}, {'x': 0, 'y': 0}, {'x_vec': 1, 'y_vec': 0}, 1],
        [{'x': 4, 'y': 5}, {'x': 8, 'y': 2}, {'x_vec': 8, 'y_vec': 1}, 3.473],
        [{'x': 16, 'y': 4}, {'x': 1, 'y': 12}, {'x_vec': 1, 'y_vec': 3}, 16.760],
    ])
    def test_calculate_dist_from_line(self, station, root_station, vector, expected):
        y_intercept = calculate_y_intercept(root_station, vector)
        self.assertEqual(expected, round(calculate_dist_from_line(station, vector, y_intercept), 3))
