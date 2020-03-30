#
# Example of solving the inventory control with lost sales problem
#
# Env: https://github.com/paulhendricks/gym-inventory/blob/master/gym_inventory/envs/inventory_env.py
#
# Author: Lisa Ong, NUS/ISS
#

import gym
import pyogmaneo
import gym_inventory # workaround for registration issue

from EnvRunner import EnvRunner

env = gym.make('Inventory-v0')

runner = EnvRunner(env)

for episode in range(1000):
    env.reset()

    # timesteps
    for t in range(50):
        done, _ = runner.act()

        if done:
            print(f'Episode {episode+1} finished after {t+1} timesteps')
            break