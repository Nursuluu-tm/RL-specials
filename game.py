"""
Q-Learning Catch Game
---------------------

This script implements a simple reinforcement learning agent using the Q-learning algorithm
to solve a 1D grid-based "Catch the Falling Object" game.

The environment is a vertical grid where a single object falls from the top to the bottom
over a series of time steps. At the bottom row, a basket can move left, right, or stay in
place to catch the falling object. The agent is trained to learn optimal movements of the 
basket to maximize successful catches.

Key Features:
-------------
- Q-learning algorithm with temporal state representation.
- Epsilon-greedy exploration strategy with decay.
- Modular design with CatchEnvironment and QLearningAgent classes.
- Console-based animation for testing the learned policy.
- Performance tracking and visualization using matplotlib.

Dependencies:
-------------
- numpy
- matplotlib
- Python 3.x standard libraries (random, time, os, collections)

Usage:
------
Simply run the script to train the agent, view animated test episodes,
and plot the learning progress.

Author: <Your Name>
Date: <Date>
"""




import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Environment settings
WIDTH = 7
HEIGHT = 6
ACTIONS = [-1, 0, 1]  # Left, Stay, Right

# Q-learning parameters
EPISODES = 2000
ALPHA = 0.1
GAMMA = 0.95
EPSILON = 1.0
MIN_EPSILON = 0.01
DECAY_RATE = 0.995


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_environment(object_x, basket_x, height, current_step):
    clear_console()
    for row in range(height):
        line = [" "] * WIDTH
        if row == current_step:
            line[object_x] = "*"
        elif row == height - 1 and current_step == height - 1:
            line[basket_x] = "^"
        print("".join(line))


class CatchEnvironment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.object_x = random.randint(0, self.width - 1)
        self.basket_x = self.width // 2
        self.step_count = 0
        return self._get_state()

    def step(self, action_idx):
        move = ACTIONS[action_idx]
        self.basket_x = max(0, min(self.width - 1, self.basket_x + move))
        self.step_count += 1

        reward = 0
        done = False
        if self.step_count == self.height:
            done = True
            reward = 1 if self.basket_x == self.object_x else -1

        return self._get_state(), reward, done

    def _get_state(self):
        return (self.object_x, self.basket_x, self.step_count)


class QLearningAgent:
    def __init__(self, actions, alpha, gamma, epsilon):
        self.q_table = defaultdict(lambda: [0.0 for _ in actions])
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, len(self.actions) - 1)
        return int(np.argmax(self.q_table[state]))

    def update(self, state, action, reward, next_state):
        max_next_q = max(self.q_table[next_state])
        self.q_table[state][action] += self.alpha * (reward + self.gamma * max_next_q - self.q_table[state][action])


# Training the agent
env = CatchEnvironment(WIDTH, HEIGHT)
agent = QLearningAgent(ACTIONS, ALPHA, GAMMA, EPSILON)
results = []
success_counter = 0

for episode in range(1, EPISODES + 1):
    state = env.reset()
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state

    if reward == 1:
        success_counter += 1

    if episode % 100 == 0:
        results.append(success_counter)
        success_counter = 0

    agent.epsilon = max(MIN_EPSILON, agent.epsilon * DECAY_RATE)

# Visual test after training
def test_agent(agent, env, delay=0.4, games=3):
    for _ in range(games):
        state = env.reset()
        done = False

        while not done:
            object_x, basket_x, current_step = state
            render_environment(object_x, basket_x, env.height, current_step)

            action = int(np.argmax(agent.q_table[state]))
            state, _, done = env.step(action)
            time.sleep(delay)

        object_x, basket_x, current_step = state
        render_environment(object_x, basket_x, env.height, current_step)
        if basket_x == object_x:
            print("\n🎯 Caught the object!")
        else:
            print("\n❌ Missed the object.")
        time.sleep(1.5)

# Run test
test_agent(agent, env)

# Plotting results
plt.figure(figsize=(10, 5))
plt.plot([i * 100 for i in range(1, len(results) + 1)], results, marker='o')
plt.title("Learning Progress of Q-Learning Agent")
plt.xlabel("Episodes")
plt.ylabel("Successful Catches (per 100 episodes)")
plt.grid(True)
plt.tight_layout()
plt.show()
