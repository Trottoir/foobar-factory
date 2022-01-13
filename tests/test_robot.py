#!/usr/bin/python
from unittest import mock
from classes.robot import Robot
import unittest
import time

from settings import params


time_reducer_factor = 0.1


class TestStringMethods(unittest.TestCase):
    def test_mint_foo(self):
        # prepare
        robot = Robot("TestingRobot")
        # compute
        robot.mint_foo("Thread-1")
        # assert
        self.assertEqual(robot.foo, 1)


    def test_mint_bar(self):
        # prepare
        robot = Robot("TestingRobot")
        # compute
        robot.mint_bar("Thread-1")
        # assert
        self.assertEqual(robot.bar, 1)
     

    @mock.patch("random.random")
    def test_assembly(self, random_call):
        # prepare
        robot1 = Robot("TestingRobot1")
        robot1.foo += 1
        robot1.bar += 1

        robot2 = Robot("TestingRobot2")
        robot2.foo += 1
        robot2.bar += 1

        # compute first
        random_call.return_value = 0.5
        robot1.assembly("Thread-1")

        # compute second
        random_call.return_value = 0.8
        robot2.assembly("Thread-2")

        # first assert
        self.assertEqual(robot1.foobar, 1)
        self.assertEqual(robot1.foo, 0)
        self.assertEqual(robot1.bar, 0)

        # second assert
        self.assertEqual(robot2.foobar, 0)
        self.assertEqual(robot2.foo, 0)
        self.assertEqual(robot2.bar, 1)

    def test_sell_max_foobar(self):
        # prepare
        robot1 = Robot("TestingRobot1")
        robot1.foobar = 3
       
        # compute 
        robot1.sell_max_foobar("Thread-1")

        # first assert
        self.assertEqual(robot1.foobar, 0)
        self.assertEqual(robot1.balance, 3)

    def test_buy_bots(self):
        # prepare
        robot1 = Robot("TestingRobot1")
        robot1.balance = 6
        robot1.foo = 12
       
        # compute 
        new_bots = robot1.buy_bots("Thread-1")

        # first assert
        self.assertEqual(len(new_bots), 2)
        self.assertEqual(robot1.balance, 0)
        self.assertEqual(robot1.foo, 0)

    def test_moove(self):
        # prepare
        robot1 = Robot("TestingRobot1")

        # compute 
        initial_time = time.time()
        robot1.moove("Thread-1", "Place A", "Place B")
        ending_time = time.time()
        total_time = ending_time - initial_time

        # assert
        self.assertTrue(total_time <= 6 * params.time_reducer_factor)
        self.assertTrue(total_time >= 3 * params.time_reducer_factor)



if __name__ == "__main__":
    unittest.main()
