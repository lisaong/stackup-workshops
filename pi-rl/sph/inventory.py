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


