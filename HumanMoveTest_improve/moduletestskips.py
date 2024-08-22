import unittest
from main import *
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self.__class__, 'is_frozen', False):
            self.skipTest("Tests are frozen")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для контроля пропуска тестов

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("TestRunner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("TestRunner3")
        runner2 = Runner("TestRunner4")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для контроля пропуска тестов

    @skip_if_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_if_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_if_frozen
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        formatted_result = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")