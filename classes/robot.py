from threading import Thread
import time
import itertools
import random
import decimal
from settings import bot_names, params

class Robot:
    id_iter = itertools.count()
    def __init__(self, _name):
        self.id = next(self.id_iter)
        self.name = _name
        self.foo = 0
        self.bar = 0
        self.foobar = 0
        self.balance = 0
        self.booted = False
        

    # Foo Minting function
    def mint_foo(self, _thread_name: str):                                                                                                                                                                                                  
        time.sleep(0.5 * params.time_reducer_factor)
        self.foo += 1
        print(_thread_name + " : " + self.name + " mints 1 foo in 0.5s")

    # Bar Minting function
    def mint_bar(self, _thread_name: str):
        waiting_time = float(decimal.Decimal(random.randrange(5, 20)) / 10)
        time.sleep(waiting_time * params.time_reducer_factor)
        self.bar += 1
        print("%s : %s mints 1 bar in %ss" %(_thread_name, self.name, waiting_time))

    # Assembly function
    def assembly(self, _thread_name: str):
        if self.bar != 0 and self.foo != 0:
            random_ratio = random.random()
            self.foo -= 1
            if random_ratio < 0.6:
                self.bar -= 1
                self.foobar += 1
                print("%s : %s assemblies 1 foobar" %(_thread_name,self.name))
            else:
                print("%s : %s fails in assemblies 1 foobar" %(_thread_name,self.name))
    
    # Reload foo function
    def reload_foo(self, _trhead_name: str, _from: str):
        
        while self.foo < (3 - self.foobar) * 6:
            self.mint_foo(_trhead_name)
            
    # Sell max foobar function
    def sell_max_foobar(self, _thread_name: str):
        while self.foobar != 0:
            qtt_sold = random.randrange(1, self.foobar + 1)
            time.sleep(10 * params.time_reducer_factor)
            self.balance += qtt_sold
            self.foobar -= qtt_sold
            print("%s : %s sold %s foobar in 10s" %(_thread_name, self.name, str(qtt_sold)))

    # Buy bots function  
    def buy_bots(self, _thread_name: str):
        new_bots = []
        while self.balance >= 3 and self.foo >= 6:
            self.balance -= 3
            self.foo -= 6
            new_bots.append(Robot(bot_names.robot_names[self.id]))
            print("%s : %s bot created " %(_thread_name, bot_names.robot_names[self.id]))
        return new_bots


    def moove(self, _thread_name: str, _from: str, _to: str):
        print("%s : %s mooves from %s to %s" %(_thread_name,self.name,_from,_to))
        time.sleep(5 * params.time_reducer_factor)
