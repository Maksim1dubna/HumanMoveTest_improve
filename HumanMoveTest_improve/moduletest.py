import unittest
from main import *

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=5)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        # Сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_usain_and_nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        # Сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_andrey_and_nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        # Сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_usain_andrey_and_nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)