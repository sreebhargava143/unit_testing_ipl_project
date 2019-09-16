import unittest
import collections
import sys
sys.path.append('/home/sribhargava/Desktop/projects/ipl/iplproject2/')
from ipl_helper import *

class TestIplHelper(unittest.TestCase):
    def test_sorted_dict(self):
        mock_input = {
            2 : 2,
            1 : 3,
            3 : 1
        }
        expected_output = {
            1 : 3,
            2 : 2,
            3 : 1
        }
        actual_output = sorted_dict(mock_input)
        self.assertEqual(actual_output, expected_output)
        expected_output = {
            3 : 1,
            2 : 2,
            1 : 3
        }
        actual_output = sorted_dict(mock_input, reverse = True)
        self.assertEqual(actual_output, expected_output)
        expected_output = {
            3 : 1,
            2 : 2,
            1 : 3
        }
        actual_output = sorted_dict(mock_input, by = 'value')
        self.assertEqual(actual_output, expected_output)
        expected_output = {
            1 : 3,
            2 : 2,
            3 : 1
        }
        actual_output = sorted_dict(mock_input, by = 'value', reverse = True)
        self.assertEqual(actual_output, expected_output)
    def test_extract_id_set(self):
        with self.assertRaises(FileNotFoundError):
            extract_id_set(2008, 'matches.csv')
            
        with self.assertRaises(TypeError):
            extract_id_set("2008", 'mock_matches.csv')
            extract_id_set(2008, 'mock_matches.txt')
        expected_output = str(['77', '78'])
        actual_output = str(extract_id_set(2008, 'mock_matches.csv'))
        self.assertEqual(actual_output, expected_output)
    
    def test_extract_deliveries(self):
        with self.assertRaises(FileNotFoundError):
            extract_deliveries('deliveries.csv')
        with self.assertRaises(KeyError):
            extract_deliveries('mock_matches.csv')
        with self.assertRaises(TypeError):
            extract_deliveries('mock_deliveries.txt')