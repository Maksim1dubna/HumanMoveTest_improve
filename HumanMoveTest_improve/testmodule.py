import unittest
from main import *
from moduletestskips import *
#from test_module import RunnerTest, TournamentTest  # Замените 'test_module' на реальное имя модуля с тестами

# Создание TestSuite
suite = unittest.TestSuite()

# Добавление тестов RunnerTest и TournamentTest в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создание и запуск тестов с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
