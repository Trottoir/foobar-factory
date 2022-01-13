from threading import  Thread
from classes.robot import Robot
from typing import List
from settings import params

class Factory:
    def __init__(self, _initial_bots: List[Robot], _bot_number_max: int):
        self.robots = _initial_bots
        self.bot_number_max = _bot_number_max
        print("Une factory vient d'être créée")

    # Init Thread
    def initialize_bot(self, trhead_name: str, bot: Robot):
        self.bot_workflow(trhead_name, bot, 3)

    # Init Thread
    def bot_booting(self):
        for bot in self.robots:
            if not bot.booted:
                bot.booted = True
                thread = Thread(target=self.initialize_bot, args=( "Thread " + str(bot.id),bot,))
                thread.daemon = True
                thread.start()
           

    def bot_workflow(self, trhead_name: str, bot: Robot, number_to_build_in_same_time: int):
        # While we don't have the desired robot number
        while len(self.robots) < self.bot_number_max:
            # Foo minting
            while bot.foo < (number_to_build_in_same_time - bot.foobar) * 6:
                bot.mint_foo(trhead_name)
            bot.moove(trhead_name, params.Workshops.FOO_MINE.name, params.Workshops.BAR_MINE.name)

            # Bar minting
            while bot.bar < (number_to_build_in_same_time - bot.foobar) * 3:
                bot.mint_bar(trhead_name)
            bot.moove(trhead_name, params.Workshops.BAR_MINE.name, params.Workshops.ASSEMBLY_LINE.name)

            # Assembly Line
            while bot.foobar < number_to_build_in_same_time:
                
                # Need to reload foo lost during last assmbly
                if bot.foo == 0:
                    bot.moove(trhead_name, params.Workshops.ASSEMBLY_LINE.name, params.Workshops.FOO_MINE.name)
                    bot.reload_foo(trhead_name)
                    bot.moove(trhead_name, params.Workshops.FOO_MINE.name, params.Workshops.ASSEMBLY_LINE.name)

                bot.assembly(trhead_name)
            bot.moove(trhead_name, params.Workshops.ASSEMBLY_LINE.name, params.Workshops.FOOBAR_MARKET_PLACE.name)

            # FooBar selling office
            bot.sell_max_foobar(trhead_name)
            bot.moove(trhead_name, params.Workshops.FOOBAR_MARKET_PLACE.name, params.Workshops.ROBOT_MARKET_PLACE.name)

            # Robot Shop
            bots = bot.buy_bots(trhead_name)
            self.robots.extend(bots)

            self.bot_booting()
            print("End of %s cycle, it has %s foobar , %s foo, %s bar, %s € and has generated %s bots"% 
            ( bot.name,str(bot.foobar),str(bot.foo),str(bot.bar),str(bot.balance),str(len(bots)),))
            bot.moove(trhead_name, params.Workshops.ROBOT_MARKET_PLACE.name, params.Workshops.FOO_MINE.name)

