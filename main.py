import time
from classes.factory import Factory
from classes.robot import Robot
from counter_multiprocess import get_counter
from settings import params
from multiprocessing import Pool

# Callback of the bot_worker process
def callback(callback_response: tuple[list, Robot]):
    # Replace the Robot object to have the updated object
    all_bots.remove(callback_response[1])
    all_bots.append(callback_response[1])
    #  Bot that run the proccess has to do the process again
    callback_response[1].has_to_be_booted = True
    # We add the process new bots created during the process
    all_bots.extend(callback_response[0])


if __name__ == "__main__":
    # Initialize Factory
    all_bots = [Robot(0), Robot(1)]
    factory = Factory(all_bots, params.foobar_to_build_in_one_cycle)
    pool = Pool(params.max_bot)

    # Continue the process while we don't have the number of bot desired
    while len(factory.robots) <= params.max_bot:
        bot_to_boot = []

        # Determine which robots the Factory has to process
        for bot in factory.robots:
            if bot.has_to_be_booted:
                bot_to_boot.append(bot)
                bot.has_to_be_booted = False

        # Apply the process on Robots to boot
        async_result = [
            pool.apply_async(
                factory.bot_worker,
                args=(
                    robot,
                    get_counter(),
                ),
                callback=callback,
            )
            for robot in bot_to_boot
        ]

        # Check Bot to boot every 3 seconds
        time.sleep(3)
    print("***************** END *****************")
    print(str(params.max_bot) + " bots have been summoned")

    # print bot recap
    for bot in factory.robots:
        print(str(bot))
