import numpy as np
from config import *

class QLearning:
    def __init__(self, rows, cols):
        self.q_table = {}
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]

    def get_q(self, state, action):
        """Obtiene el valor Q de un estado-acción"""
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.actions}
        return self.q_table[state][action]

    def get_best_action(self, state, available_actions):
        """Devuelve la mejor acción para un estado dado"""
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.actions}
        q_vals = self.q_table[state]
        filtered = {a: q_vals[a] for a in available_actions}
        return max(filtered, key=filtered.get)

    def update(self, state, action, reward, next_state, next_actions):
        """Actualiza la tabla Q con la fórmula de Bellman"""
        current_q = self.get_q(state, action)
        max_q_next = max([self.get_q(next_state, a) for a in next_actions]) if next_actions else 0
        new_q = current_q + ALPHA * (reward + GAMMA * max_q_next - current_q)
        self.q_table[state][action] = new_q
