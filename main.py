import unittest
import requests
import json

data = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()

def min_temp():
    temps = [record['temperature'] for record in data['data']]
    return min(temps)

def max_temp():
    temps = [record['temperature'] for record in data['data']]
    return max(temps)

def avg_temp():
    temps = [record['temperature'] for record in data['data']]
    return sum(temps) / len(temps)

class TestStringMethods(unittest.TestCase):
    def test_min(self):
        temps = [record['temperature'] for record in data['data']]
        self.assertEqual(min_temp(), min(temps))

    def test_avg(self):
        temps = [record['temperature'] for record in data['data']]
        self.assertEqual(avg_temp(), sum(temps) / len(temps))

    def test_max(self):
        temps = [record['temperature'] for record in data['data']]
        self.assertEqual(max_temp(), max(temps))


if __name__ == '__main__':
    print('Min: ', min_temp())
    print('Avg: ', avg_temp())
    print('Max: ', max_temp())
    unittest.main()