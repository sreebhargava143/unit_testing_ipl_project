import unittest
import collections
import sys
sys.path.append('/home/sribhargava/Desktop/projects/ipl/iplproject2/')
from total_matches_won import find_matches_won

class TestTotalMatchesWon(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            find_matches_won('matches.csv')
    def test_find_matches_won(self):
        expected_output = "{'Deccan Chargers': OrderedDict([('2008', 0), ('2009', 2), ('2010', 1)]), 'Kings XI Punjab': OrderedDict([('2008', 1), ('2009', 0), ('2010', 0)]), 'Rajasthan Royals': OrderedDict([('2008', 1), ('2009', 0), ('2010', 0)]), 'Kolkata Knight Riders': OrderedDict([('2008', 0), ('2009', 0), ('2010', 0)]), 'Royal Challengers Bangalore': OrderedDict([('2008', 0), ('2009', 0), ('2010', 0)]), 'Chennai Super Kings': OrderedDict([('2008', 0), ('2009', 0), ('2010', 0)]), 'Mumbai Indians': OrderedDict([('2008', 0), ('2009', 0), ('2010', 1)]), 'Delhi Daredevils': OrderedDict([('2008', 0), ('2009', 0), ('2010', 0)])}"
        actual_ouput = str(find_matches_won('mock_matches.csv'))
        self.assertEqual(expected_output, actual_ouput)
    def test_wrong_file(self):
        with self.assertRaises(TypeError):
            find_matches_won('mock_matches.txt')
    def test_key_error(self):
        with self.assertRaises(KeyError):
            find_matches_won('mock_deliveries.csv')