from catch_game_rl.game import CatchEnvironment, QLearningAgent

if __name__ == "__main__":
    env = CatchEnvironment(grid_size=5)
    agent = QLearningAgent(env, episodes=500)
    agent.train()
    agent.test(render=True)
