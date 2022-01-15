#!/usr/bin/python
from unittest import mock
from classes.robot import Robot
import unittest
import time

from settings import params


time_reducer_factor = 0.1


class TestStringMethods(unittest.TestCase):

    # Before each
    def setUp(self):
        self.robot = Robot(0)

    def test_mint_foo(self):
        # compute
        self.robot.mint_foo()
        # assert
        self.assertEqual(self.robot.foo, 1)


    def test_mint_bar(self):
        # compute
        self.robot.mint_bar()
        # assert
        self.assertEqual(self.robot.bar, 1)
     

    @mock.patch("random.random")
    def test_assembly(self, random_call):
        # prepare
        self.robot.foo += 1
        self.robot.bar += 1

        robot2 = Robot(1)
        robot2.foo += 1
        robot2.bar += 1

        # compute first
        random_call.return_value = 0.5
        self.robot.assembly()

        # compute second
        random_call.return_value = 0.8
        robot2.assembly()

        # first assert
        self.assertEqual(self.robot.foobar, 1)
        self.assertEqual(self.robot.foo, 0)
        self.assertEqual(self.robot.bar, 0)

        # second assert
        self.assertEqual(robot2.foobar, 0)
        self.assertEqual(robot2.foo, 0)
        self.assertEqual(robot2.bar, 1)

    @mock.patch("random.randrange")
    def test_sell_foobar(self, random_call):
        # prepare
        self.robot.foobar = 3
        random_call.return_value = 2
       
        # compute 
        self.robot.sell_foobar()

        # first assert
        self.assertEqual(self.robot.foobar, 1)
        self.assertEqual(self.robot.balance, 2)

    def test_buy_bots(self):
        # prepare
        self.robot.balance = 6
        self.robot.foo = 12
       
        # compute 
        new_bot = self.robot.buy_bot(1)

        # first assert
        self.assertEqual(new_bot.id, 1)
        self.assertEqual(self.robot.balance, 3)
        self.assertEqual(self.robot.foo, 6)

    def test_moove(self):

        # compute 
        initial_time = time.time()
        self.robot.moove("Place A", "Place B")
        ending_time = time.time()
        total_time = ending_time - initial_time

        # assert
        self.assertTrue(total_time <= 6 * params.time_reducer_factor)
        self.assertTrue(total_time >= 3 * params.time_reducer_factor)



if __name__ == "__main__":
    unittest.main()
