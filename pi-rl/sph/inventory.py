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
import matplotlib.pyplot as plt
import pandas as pd

from EnvRunner import EnvRunner

timesteps=50
episodes=1000
max_inventory=50
d_lambda=25

env = gym.make('Inventory-v0', n=max_inventory, lam=d_lambda)

runner = EnvRunner(env, terminalReward=100)
history = []

for episode in range(episodes):
    env.reset()

    # timesteps
    reward = 0
    for t in range(timesteps):
        # EnvRunner expects an array of observations
        done, reward = runner.act(obsPreprocess=lambda obs : [obs])

        if done:
            break

    history.append(reward)
    print(f'Episode {episode+1} finished after {t+1} timesteps, reward {reward}')

# plot episodes v rewards
fig, ax = plt.subplots()
ax.plot(history)
ax.set(xlabel='episode', ylabel='reward', title=f'Inventory control problem, timesteps: {timesteps}, episodes: {episodes}')
plt.savefig(f'inventory_M{max_inventory}_Dlambda{d_lambda}_{episodes}ep_{timesteps}steps')
