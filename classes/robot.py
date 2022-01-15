import time
import random
import decimal
from settings import bot_names, params

class Robot:
    def __init__(self,_id):
        self.id = _id
        self.name = bot_names.robot_names[self.id]
        self.foo  = 0
        self.bar  = 0
        self.foobar  = 0
        self.balance  = 0
        self.has_to_be_booted = True
        print(self.name+" has been summoned")

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.name + " has " + str(self.foo)+" foo | "+str(self.bar) + " bar | " + str(self.foobar)+" foobar | "+str(self.balance)+"€"

    # Foo Minting function
    def mint_foo(self):                                                                                                                                                                                                  
        time.sleep(0.5 * params.time_reducer_factor)
        self.foo += 1
        print(self.name + " mints 1 foo in 0.5s")

    # Bar Minting function
    def mint_bar(self):
        waiting_time = float(decimal.Decimal(random.randrange(5, 20)) / 10)
        time.sleep(waiting_time * params.time_reducer_factor)
        self.bar += 1
        print("%s mints 1 bar in %ss" %( self.name, waiting_time))

    # Assembly function
    def assembly(self):
        if self.bar != 0 and self.foo != 0:
            random_ratio = random.random()
            self.foo -= 1
            if random_ratio < 0.6:
                self.bar -= 1
                self.foobar += 1
                print("%s assemblies 1 foobar" %(self.name))
            else:
                print("%s fails in assemblies 1 foobar" %(self.name))
            
    # Sell max foobar function
    def sell_foobar(self):
        qtt_sold = random.randrange(1, self.foobar + 1)
        time.sleep(10 * params.time_reducer_factor)
        self.balance += qtt_sold
        self.foobar -= qtt_sold
        print("%s sold %s foobar in 10s" %( self.name, str(qtt_sold)))

    # Buy bot function  
    def buy_bot(self, counter : int):
        self.balance -= 3
        self.foo -= 6
        return Robot(counter)
        

    def moove(self, _from: str, _to: str):
        print("%s mooves from %s to %s in 5s" %(self.name,_from,_to))
        time.sleep(5 * params.time_reducer_factor)
