from classes.factory import Factory
from classes.robot import Robot
from settings import params


initial_bots = [Robot("MaxouBot"), Robot("PoppyBot")]
factory = Factory(initial_bots, params.bot_number_max)
factory.bot_booting()

while len(factory.robots) < params.bot_number_max:
    pass
print("30 bot have been created")