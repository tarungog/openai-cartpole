import gym
import numpy as np

env = gym.make('CartPole-v0')
# env.monitor.start('.', force=True)
# random guessing
bestreward = 0
guess = np.random.rand(4) * 2 - 1
for i in range(10000):
    observation = env.reset()
    noise = np.random.rand(4) * 2 - 1
    noise = noise * 0.05
    current_guess = guess + noise
    totalreward = 0
    for t in range(200):
        env.render()
        action = 0 if observation.dot(current_guess) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    if totalreward > bestreward:
        guess = current_guess
        bestreward = totalreward
    if bestreward == 200:
        print("Required {} trials to reach perfect performance".format(i))
        break
print(bestreward)
print(guess)
# env.monitor.close()