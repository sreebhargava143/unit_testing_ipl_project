import unittest
import collections
import sys
sys.path.append('/home/sribhargava/Desktop/projects/ipl/iplproject2/')
from matches_played_per_year import find_matches_per_year

class TestMatchesPerYear(unittest.TestCase):
    def test_find_matches_per_year(self):
        expected_output = collections.OrderedDict([('2008', 2), ('2009', 2), ('2010', 2)])
        actual_output = find_matches_per_year('mock_matches.csv')
        self.assertEqual(expected_output, actual_output)
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            find_matches_per_year('matches.csv')
    def test_wrong_file(self):
        with self.assertRaises(TypeError):
            find_matches_per_year('matches.txt')
    def test_key_error(self):
        with self.assertRaises(KeyError):
            find_matches_per_year('mock_deliveries.txt')
if __name__ == "__main__":
    unittest.main()
