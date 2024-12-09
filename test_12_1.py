import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.runner = runner.Runner("Ivan")
        for i in range (10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    def test_run(self):
        self.runner = runner.Runner("Petya")
        for i in range (10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        self.runner = runner.Runner("Runner1")
        self.runner2 = runner.Runner("Runner2")
        for i in range (10):
            self.runner.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner.distance, self.runner2.distance)