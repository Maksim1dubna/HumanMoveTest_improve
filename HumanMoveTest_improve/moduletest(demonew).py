import main
import unittest
class TournamentTest(unittest.TestCase):
    def setUpClass(self, *all_results):
        self.all_result = {}
        self.all_result.update(all_results)
    def setUp(self, *participants):
        self.participants = list(participants)
    def tearDownClass(self):
        for key, value in self.all_results.items():
            print("{0}: {1}".format(key, value))

    def teststartYN(self):
        tour = main.Tournament(90,
                               main.Runner('Усэйн', 10),
                               main.Runner('Ник', 3))
        results = tour.start()
        self.assertTrue(results.__getitem__(list(results)[-1])=='Ник', 'Неверно')
    def teststartAN(self):
        tour = main.Tournament(90,
                               main.Runner('Андрей', 9),
                               main.Runner('Ник', 3))
        results = tour.start()
        self.assertTrue(results.__getitem__(list(results)[-1])=='Ник', 'Неверно')

    def teststartYAN(self):
        tour = main.Tournament(90, main.Runner('Усэйн', 10),
                               main.Runner('Андрей', 9),
                               main.Runner('Ник', 3))
        results = tour.start()
        self.assertTrue(results.__getitem__(list(results)[-1])=='Ник', 'Неверно')

if __name__ == "__main__":
    tournament_test_object = TournamentTest()
    tournament_test_object.setUpClass()
    unittest.main()