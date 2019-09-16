import unittest
import collections
import sys
import json
sys.path.append('/home/sribhargava/Desktop/projects/ipl/iplproject2/')
from performance import *
class TestPerformance(unittest.TestCase):
    def test_get_season_id_dict(self):
        expected_output = {
            '2008': ['77', '78'], 
            '2009': ['124', '131'], 
            '2010': ['183', '186']
            }
        actual_output = get_season_id_dict('mock_matches.csv')
        self.assertEqual(actual_output, expected_output)
        with self.assertRaises(FileNotFoundError):
            get_season_id_dict('matches.csv')
    
        with self.assertRaises(TypeError):
            get_season_id_dict('mock_matches.txt')
    
        with self.assertRaises(KeyError):
            get_season_id_dict('mock_deliveries.csv')

    def test_get_batsmen_strike_rate(self):
        expected_output = str({'AC Gilchrist': {'2008': 0.0, '2009': 66.67, '2010': 250.0}, 'VVS Laxman': {'2008': 171.43, '2009': 50.0, '2010': 150.0}, 'HH Gibbs': {'2008': 83.33, '2009': 150.0, '2010': 66.67}, 'GC Smith': {'2008': 50.0, '2009': None, '2010': None}, 'SA Asnodkar': {'2008': 120.0, '2009': None, '2010': None}, 'M Kaif': {'2008': 200.0, '2009': None, '2010': None}, 'PA Patel': {'2008': None, '2009': 0.0, '2010': None}, 'SK Raina': {'2008': None, '2009': 150.0, '2010': None}, 'ML Hayden': {'2008': None, '2009': 257.14, '2010': None}, 'ST Jayasuriya': {'2008': None, '2009': None, '2010': 0.0}, 'SR Tendulkar': {'2008': None, '2009': None, '2010': 260.0}, 'A Symonds': {'2008': None, '2009': None, '2010': 166.67}})
        
        actual_output = str(get_batsmen_strike_rate([], 'mock_matches.csv', 'mock_deliveries.csv'))
        
        self.assertEqual(actual_output, expected_output)
        
    def test_calculate_strike_rate(self):
        input1 = {
            'AC Gilchrist': {
                '2008': [0, 1],
                '2009': [6, 9],
                '2010': [15, 6]},
            'VVS Laxman': {
                '2008': [12, 7],
                '2009': [1, 2],
                 '2010': [3, 2]},
            'HH Gibbs': {
                '2008': [5, 6],
                '2009': [6, 4],
                '2010': [2, 3]},
            'GC Smith': {
                '2008': [2, 4],
                '2009': [],
                '2010': []}, 
            'SA Asnodkar': {
                '2008': [6, 5],
                '2009': [],
                '2010': []},
            'M Kaif': {
                '2008': [12, 6],
                '2009': [],
                '2010': []},
            'PA Patel': {
                '2008': [],
                '2009': [0, 1],
                '2010': []}, 
            'SK Raina': {
                '2008': [],
                '2009': [9, 6],
                '2010': []}, 
            'ML Hayden': {
                '2008': [],
                '2009': [18, 7],
                '2010': []},
            'ST Jayasuriya': {
                '2008': [],
                '2009': [],
                '2010': [0, 4]}, 
            'SR Tendulkar': {
                '2008': [],
                '2009': [],
                '2010': [26, 10]},
            'A Symonds': {
                '2008': [],
                '2009': [],
                '2010': [5, 3]}
            }
        input2 = ['2008', '2009', '2010']
        expected_output = str({'AC Gilchrist': {'2008': 0.0, '2009': 66.67, '2010': 250.0}, 'VVS Laxman': {'2008': 171.43, '2009': 50.0, '2010': 150.0}, 'HH Gibbs': {'2008': 83.33, '2009': 150.0, '2010': 66.67}, 'GC Smith': {'2008': 50.0, '2009': None, '2010': None}, 'SA Asnodkar': {'2008': 120.0, '2009': None, '2010': None}, 'M Kaif': {'2008': 200.0, '2009': None, '2010': None}, 'PA Patel': {'2008': None, '2009': 0.0, '2010': None}, 'SK Raina': {'2008': None, '2009': 150.0, '2010': None}, 'ML Hayden': {'2008': None, '2009': 257.14, '2010': None}, 'ST Jayasuriya': {'2008': None, '2009': None, '2010': 0.0}, 'SR Tendulkar': {'2008': None, '2009': None, '2010': 260.0}, 'A Symonds': {'2008': None, '2009': None, '2010': 166.67}})
        actual_output = str(calculate_strike_rate(input1, input2))
        self.assertEqual(actual_output, expected_output)