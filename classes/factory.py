from classes.robot import Robot
from typing import List
from settings import params

class Factory:
    def __init__(self, _initial_bots: List[Robot], _foobar_to_build_in_one_cycle: int):
        self.robots = _initial_bots
        self.foobar_to_build_in_one_cycle = _foobar_to_build_in_one_cycle
        self.counter = len(_initial_bots)
        print("A Factory has been created")

    # Foo minting
    def batch_mining_foo(self, bot: Robot):
        while bot.foo < (self.foobar_to_build_in_one_cycle - bot.foobar) * 5: # *5 is a marging error to always have enough foo to assembly + buy a robot
            bot.mint_foo()
        bot.moove( params.Workshops.FOO_MINE.name, params.Workshops.BAR_MINE.name)

    # Bar minting
    def batch_mining_bar(self, bot: Robot):
        while bot.bar < self.foobar_to_build_in_one_cycle - bot.foobar:
            bot.mint_bar()
        bot.moove( params.Workshops.BAR_MINE.name, params.Workshops.ASSEMBLY_LINE.name)

    def batch_assembly_foobar(self, bot: Robot):
        while bot.foobar != self.foobar_to_build_in_one_cycle:
            # Need to reload foo lost during last assembly
            if bot.foo == 0:
                bot.moove( params.Workshops.ASSEMBLY_LINE.name, params.Workshops.FOO_MINE.name)
                while bot.foo < (self.foobar_to_build_in_one_cycle - bot.foobar) * 6:
                    bot.mint_foo()
                bot.moove( params.Workshops.FOO_MINE.name, params.Workshops.ASSEMBLY_LINE.name)

            bot.assembly()
        bot.moove( params.Workshops.ASSEMBLY_LINE.name, params.Workshops.FOOBAR_MARKET_PLACE.name)

    def batch_sell_foobar(self, bot: Robot):
        while bot.foobar != 0:
            bot.sell_foobar()
        bot.moove( params.Workshops.FOOBAR_MARKET_PLACE.name, params.Workshops.ROBOT_MARKET_PLACE.name)

    def batch_buy_robots(self, bot: Robot, counter: int):
        new_bots = []
        while bot.balance >= 3 and bot.foo >= 6:
            counter += 1
            new_bots.append(bot.buy_bot(counter))
        return new_bots

    def bot_worker(self, bot: Robot, counter: int):
        print("**************** Bot "+bot.name+" start its cycle ****************")
        
        self.batch_mining_foo(bot)
        
        self.batch_mining_bar(bot)

        self.batch_assembly_foobar(bot)
                 
                 
        self.batch_sell_foobar(bot)

        new_bots = self.batch_buy_robots(bot, counter)

        print("End of %s cycle, it has %s foobar , %s foo, %s bar, %s € and has generated %s bots"% 
        ( bot.name,str(bot.foobar),str(bot.foo),str(bot.bar),str(bot.balance),str(len(new_bots)),))

        bot.moove( params.Workshops.ROBOT_MARKET_PLACE.name, params.Workshops.FOO_MINE.name)
        return (new_bots, bot)

