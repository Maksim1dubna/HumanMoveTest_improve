import main
import unittest
class Testing(unittest.TestCase):
    def testwalk(self):
        getwalk = main.Student("WLK")
        a = 50
        for _ in range(0, 10):
            getwalk.walk()
        self.assertEqual(first=getwalk.distance, second=a, msg=str("Дистанции не равны [дистанция человека(объекта)] != {0}".format(a)))
    def testrun(self):
        getrun = main.Student("RN")
        a = 100
        for _ in range(0, 10):
            getrun.run()
        self.assertEqual(first=getrun.distance, second=a, msg=str("Дистанции не равны [дистанция человека(объекта)] != {0}".format(a)))
    def testRunWalk(self):
        getrun = main.Student("WLK")
        getwalk = main.Student("RN")
        for _ in range(0, 1):
            getrun.run()
        for _ in range(0, 10):
            getwalk.run()
        self.assertGreaterEqual(a=getrun.distance, b=getwalk.distance, msg="[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].")


if __name__ == "__main__":
    unittest.main()


tour = Tournament(10, Runner('TOM', speed=10), Runner('Alex'))
print(tour.participants.__getitem__(-1))
elem = tour.start()
print(elem.__getitem__(list(elem)[-1]))
