import unittest
import collections
import sys
sys.path.append('/home/sribhargava/Desktop/ipl/iplproject2/')
from extra_runs_conceded import find_extra_runs_conceded

class TestExtraRunsConcede(unittest.TestCase):
    def test_file_not_found_exception(self):
        with self.assertRaises(FileNotFoundError):
            find_extra_runs_conceded(2008, 'matches.csv', 'mock_deliveries.csv')
        with self.assertRaises(FileNotFoundError):
            find_extra_runs_conceded(2008, 'mock_matches.csv', 'deliveries.csv')
    def test_find_extra_runs_conceded(self):
        expected_output = "OrderedDict([('Kolkata Knight Riders', 0), ('Kings XI Punjab', 1)])"
        actual_output = str(find_extra_runs_conceded(2008, 'mock_matches.csv', 'mock_deliveries.csv'))
        self.assertEqual(actual_output, expected_output)
    def test_type_error(self):
        with self.assertRaises(TypeError):
            find_extra_runs_conceded('2008', 'mock_matches.csv', 'mock_deliveries.csv')
            find_extra_runs_conceded('2008', 'mock_matches.txt', 'mock_deliveries.csv')
            find_extra_runs_conceded('2008', 'mock_matches.csv', 'mock_deliveries.txt')
    def test_key_error(self):
        with self.assertRaises(KeyError):
            find_extra_runs_conceded('2008', 'mock_deliveries.csv', 'mock_matches.csv')