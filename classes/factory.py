from classes.robot import Robot
from typing import List
from settings import params
import os


class Factory:
    def __init__(self, _initial_bots: List[Robot], _foobar_to_build_in_one_cycle: int):
        self.robots = _initial_bots
        self.foobar_to_build_in_one_cycle = _foobar_to_build_in_one_cycle
        self.counter = len(_initial_bots)
        print("A Factory has been created")

    # Mint foo while we don't have enough marging for one cycle and moove to the Bar mine
    def batch_mining_foo(self, bot: Robot):
        while (
            bot.foo < (self.foobar_to_build_in_one_cycle - bot.foobar) * 5
        ):  # *5 is a marging error to always have enough foo to assembly + buy a robot
            bot.mint_foo()
        bot.moove(params.Workshops.FOO_MINE.name, params.Workshops.BAR_MINE.name)

    # Mint bar to have enough to build and moove to the Assembly Line
    def batch_mining_bar(self, bot: Robot):
        while bot.bar < self.foobar_to_build_in_one_cycle - bot.foobar:
            bot.mint_bar()
        bot.moove(params.Workshops.BAR_MINE.name, params.Workshops.ASSEMBLY_LINE.name)

    # Assembly foobar while bot have enough foobar and moove to the Foobar Market place
    def batch_assembly_foobar(self, bot: Robot):
        while bot.foobar != self.foobar_to_build_in_one_cycle:
            # Need to reload foo lost during last assembly
            if bot.foo == 0:
                bot.moove(
                    params.Workshops.ASSEMBLY_LINE.name, params.Workshops.FOO_MINE.name
                )
                while bot.foo < (self.foobar_to_build_in_one_cycle - bot.foobar) * 6:
                    bot.mint_foo()
                bot.moove(
                    params.Workshops.FOO_MINE.name, params.Workshops.ASSEMBLY_LINE.name
                )

            bot.assembly()
        bot.moove(
            params.Workshops.ASSEMBLY_LINE.name,
            params.Workshops.FOOBAR_MARKET_PLACE.name,
        )

    # Sell all foobars available and moove to the Robot Market Placce
    def batch_sell_foobar(self, bot: Robot):
        while bot.foobar != 0:
            bot.sell_foobar()
        bot.moove(
            params.Workshops.FOOBAR_MARKET_PLACE.name,
            params.Workshops.ROBOT_MARKET_PLACE.name,
        )

    # Buy all robots possible an return it
    def batch_buy_robots(self, bot: Robot, counter: int):
        new_bots = []
        while bot.balance >= 3 and bot.foo >= 6:
            counter += 1
            new_bots.append(bot.buy_bot(counter))
        return new_bots

    # Laucn
    def bot_worker(self, bot: Robot, counter: int):
        print(
            "**************** PID : "
            + str(os.getpid())
            + " | "
            + bot.name
            + " start its cycle ****************"
        )

        self.batch_mining_foo(bot)

        self.batch_mining_bar(bot)

        self.batch_assembly_foobar(bot)

        self.batch_sell_foobar(bot)

        new_bots = self.batch_buy_robots(bot, counter)

        print(
            "End of %s cycle, it has %s foobar , %s foo, %s bar, %s € and has generated %s bots"
            % (
                bot.name,
                str(bot.foobar),
                str(bot.foo),
                str(bot.bar),
                str(bot.balance),
                str(len(new_bots)),
            )
        )

        bot.moove(
            params.Workshops.ROBOT_MARKET_PLACE.name, params.Workshops.FOO_MINE.name
        )
        return (new_bots, bot)
