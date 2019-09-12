import unittest
import collections
import sys
sys.path.append('/home/sribhargava/Desktop/ipl/iplproject2/')
from bowlers_economy import calculate_economies
from bowlers_economy import find_top_economical_bowlers
class TestBowlersEconomy(unittest.TestCase):
    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            find_top_economical_bowlers(2008, 'matches.csv', 'deliveries.csv')
            find_top_economical_bowlers(2008, 'mock_matches.csv', 'deliveries.csv')
            find_top_economical_bowlers(2008, 'matches.csv', 'mock_deliveries.csv')
    def test_type_error(self):
        with self.assertRaises(TypeError):
            find_top_economical_bowlers('2008', 'mock_matches.csv', 'mock_deliveries.csv')
            
    def test_calculate_economies(self):
        mock_input = {'S Sreesanth': [8, 6], 'IK Pathan': [5, 2], 'VRV Singh': [3, 2], 'PP Chawla': [2, 4], 'AB Dinda': [10, 7], 'I Sharma': [6, 6], 'AB Agarkar': [4, 2]}
        expected_output = {8.0: 'S Sreesanth', 15.0: 'IK Pathan', 9.0: 'VRV Singh', 3.0: 'PP Chawla', 8.571428571428571: 'AB Dinda', 6.0: 'I Sharma', 12.0: 'AB Agarkar'}
        actual_output = calculate_economies(mock_input)
        self.assertEqual(actual_output, expected_output)
    def test_find_economical_bowlers(self):
        expected_output = "OrderedDict([(15.0, 'IK Pathan'), (12.0, 'AB Agarkar'), (9.0, 'VRV Singh'), (8.571428571428571, 'AB Dinda'), (8.0, 'S Sreesanth'), (6.0, 'I Sharma'), (3.0, 'PP Chawla')])"
        actual_output = str(find_top_economical_bowlers(2008, 'mock_matches.csv', 'mock_deliveries.csv'))
        self.assertEqual(actual_output, expected_output)
    def test_wrong_file(self):
        with self.assertRaises(TypeError):
            find_top_economical_bowlers(2008, 'mock_matches.csv', 'mock_deliveries.txt')
            find_top_economical_bowlers(2008, 'mock_matches.txt', 'mock_deliveries.csv')
    def test_key_error(self):
        with self.assertRaises(KeyError):
            find_top_economical_bowlers(2008, 'mock_deliveries.csv', 'mock_matches.csv')
            