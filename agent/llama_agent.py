import numpy as np
import random
from config import *
from agent.qlearning import QLearning
import csv
import os

class LlamaAgent:
    def __init__(self, env):
        self.env = env
        self.q = QLearning(env.rows, env.cols)
        self.state = self.env.get_state()
        self.episode = 0

        self.last_state = None
        self.last_action = None
        self.last_reward = None
        self.last_next_state = None

        self.total_reward = 0
        self.total_steps = 0
        self.success_count = 0

    def choose_action(self, state):
        """Elige una acción con política epsilon-greedy"""
        if random.uniform(0, 1) < EPSILON:
            return random.choice(self.env.get_possible_actions())
        else:
            return self.q.get_best_action(state, self.env.get_possible_actions())

    def train_step(self):
        """Un paso del ciclo de aprendizaje RL"""
        self.last_state = self.state

        action = self.choose_action(self.state)
        next_state, reward, done = self.env.step(action)

        self.last_action = action
        self.last_reward = reward
        self.last_next_state = next_state

        self.q.update(self.state, action, reward, next_state, self.env.get_possible_actions())
        self.state = next_state

        self.total_reward += reward
        self.total_steps += 1

        if done:
            self.success_count += 1
            self.episode += 1

            if self.episode % 15 == 0:
                self.export_metrics()

            # Reiniciar entorno para el siguiente episodio
            self.env.reset()
            self.state = self.env.get_state()

    def export_metrics(self):
        """Exporta métricas actuales al archivo CSV"""
        file_path = "resultados_entrenamiento.csv"
        escribir_encabezado = not os.path.exists(file_path)

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)

            if escribir_encabezado:
                writer.writerow([
                    "Episodio",
                    "Alpha", "Gamma", "Epsilon",
                    "Recompensa Total",
                    "Pasos Totales",
                    "Pasos Promedio",
                    "Tasa de Éxito (%)"
                ])

            pasos_prom = self.total_steps / self.episode if self.episode > 0 else 0
            tasa_exito = self.success_count / self.episode * 100 if self.episode > 0 else 0

            writer.writerow([
                self.episode,
                ALPHA, GAMMA, EPSILON,
                self.total_reward,
                self.total_steps,
                round(pasos_prom, 2),
                round(tasa_exito, 2)
            ])
