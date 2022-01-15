import time
from typing import Iterable
from classes.factory import Factory
from classes.robot import Robot
from counter_multiprocess import get_counter
from settings import params
from multiprocessing import Pool

# Callback of the bot_worker process
def callback(bots : tuple[list, Robot]):
    #  Bot that run the proccess has to do the process again

    all_bots.remove(bots[1])
    bots[1].has_to_be_booted = True
    # We add the process new bots created during the process
    all_bots.extend(bots[0])
    all_bots.append(bots[1])

if __name__ == "__main__":
    all_bots = [Robot(0), Robot(1)]
    factory = Factory(all_bots, params.foobar_to_build_in_one_cycle)
    pool = Pool(params.max_bot)
    
    while len(factory.robots) <= params.max_bot :
        bot_to_boot = []

        # Determine which robots we have to Boot 
        for bot in factory.robots:
            if bot.has_to_be_booted:
                print(str(bot))
                bot_to_boot.append(bot)
                bot.has_to_be_booted = False

        # Apply the process 
        async_result = [pool.apply_async(factory.bot_worker, args=(robot, get_counter(), ), callback=callback) for robot in bot_to_boot]

        if len(bot_to_boot) == 0:
            print("Main Thread : No process to launch")
        else:
            print("Main Thread : "+ str(len(bot_to_boot))+ " process launched") 

        time.sleep(2)
        print("Main Thread : Check Bot to boot every 2 seconds")

    print(str(params.max_bot) + " bots have been built")
    for bot in factory.robots:
        print(str(bot))
    