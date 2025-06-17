import numpy as np
import random
from config import *
from environment.obstacle_generator import generate_random_obstacles

class GameEnvironment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.reset()

    def reset(self):
        """Inicializa un nuevo episodio con obstáculos y posición inicial/meta"""
        self.agent_pos = [0, 0]
        self.goal_pos = [self.rows - 1, self.cols - 1]
        self.obstacles = generate_random_obstacles(
            self.rows,
            self.cols,
            count=15,
            forbidden_positions=[tuple(self.agent_pos), tuple(self.goal_pos)]
        )
        self.visited = set()
        return self.agent_pos

    def get_state(self):
        """Devuelve la posición actual del agente como tupla"""
        return tuple(self.agent_pos)

    def is_terminal(self):
        """Verifica si la meta ha sido alcanzada"""
        return self.agent_pos == self.goal_pos

    def get_possible_actions(self):
        """Devuelve las acciones posibles (sin salir del grid)"""
        actions = []
        r, c = self.agent_pos
        if r > 0: actions.append("UP")
        if r < self.rows - 1: actions.append("DOWN")
        if c > 0: actions.append("LEFT")
        if c < self.cols - 1: actions.append("RIGHT")
        return actions

    def step(self, action):
        """Mueve al agente en el entorno según la acción, devuelve recompensa"""
        r, c = self.agent_pos

        if action == "UP":
            r -= 1
        elif action == "DOWN":
            r += 1
        elif action == "LEFT":
            c -= 1
        elif action == "RIGHT":
            c += 1

        nueva_pos = (r, c)

        if nueva_pos in self.obstacles:
            reward = REWARD_OBSTACLE
        elif nueva_pos in self.visited:
            reward = REWARD_REPEAT
            self.agent_pos = list(nueva_pos)
        else:
            self.agent_pos = list(nueva_pos)
            self.visited.add(nueva_pos)
            if self.agent_pos == self.goal_pos:
                reward = REWARD_GOAL
            else:
                reward = REWARD_STEP

        return self.get_state(), reward, self.is_terminal()
