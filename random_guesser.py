import gym
import numpy as np

env = gym.make('CartPole-v0')
# env.monitor.start('.', force=True)
# random guessing
bestguess = None
bestreward = 0
for i in range(10000):
    observation = env.reset()
    guess = np.random.rand(4) * 2 - 1
    totalreward = 0
    for t in range(200):
        env.render()
        action = 0 if observation.dot(guess) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    if totalreward > bestreward:
        bestguess = guess
        bestreward = totalreward
print(bestreward)
print(bestguess)
# env.monitor.close()