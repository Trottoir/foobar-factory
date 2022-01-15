#!/usr/bin/python
from unittest import mock
from classes.factory import Factory
from classes.robot import Robot
import unittest

class TestStringMethods(unittest.TestCase):
    
    # Before each
    def setUp(self):
        all_bots = [Robot(0)]
        self.factory = Factory(all_bots, 3)

    def test_batch_mining_foo(self):
        # compute
        self.factory.batch_mining_foo(self.factory.robots[0])
        # assert
        self.assertEqual(self.factory.robots[0].foo, 18)
        self.factory.batch_mining_foo(self.factory.robots[0])
        self.assertEqual(self.factory.robots[0].foo, 18)

    def test_batch_mining_bar(self):
        # compute
        self.factory.batch_mining_bar(self.factory.robots[0])
        # assert
        self.assertEqual(self.factory.robots[0].bar, 9)
        self.factory.batch_mining_bar(self.factory.robots[0])
        self.assertEqual(self.factory.robots[0].bar, 9)

    def test_batch_assembly_foobar(self):
        self.factory.robots[0].foo = 0
        self.factory.robots[0].bar = 9
        # compute
        self.factory.batch_assembly_foobar(self.factory.robots[0])
        # assert
        self.assertEqual(self.factory.robots[0].foobar, 3)
        self.factory.batch_assembly_foobar(self.factory.robots[0])
        self.assertEqual(self.factory.robots[0].foobar, 3)
        


        self.factory.batch_assembly_foobar(self.factory.robots[0])
        self.assertEqual(self.factory.robots[0].foobar, 3)
    
    def test_batch_sell_foobar(self):
        self.factory.robots[0].foobar = 5
        # compute
        self.factory.batch_sell_foobar(self.factory.robots[0])
        # assert
        self.assertEqual(self.factory.robots[0].foobar, 0)
        self.assertEqual(self.factory.robots[0].balance, 5)
        self.factory.batch_sell_foobar(self.factory.robots[0])
        self.assertEqual(self.factory.robots[0].foobar, 0)
        self.assertEqual(self.factory.robots[0].balance, 5)

    def test_batch_buy_robots(self):
        self.factory.robots[0].balance = 8
        self.factory.robots[0].foo = 14
        new_bots = self.factory.batch_buy_robots(self.factory.robots[0], 0)
        self.assertEqual(self.factory.robots[0].foo, 2)
        self.assertEqual(self.factory.robots[0].balance, 2)
        self.assertEqual(len(new_bots), 2)

    def test_bot_worker(self):
        (new_bots, bot) = self.factory.bot_worker(self.factory.robots[0], 0)
        self.assertEqual(len(new_bots), 1)
        



if __name__ == "__main__":
    unittest.main()
