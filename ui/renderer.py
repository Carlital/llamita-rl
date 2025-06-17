import pygame
from config import CELL_SIZE, GRID_ROWS, GRID_COLS, COLOR_GRID
import os

class Renderer:
    def __init__(self, screen, env, agent):
        self.screen = screen
        self.env = env
        self.agent = agent
        self.load_assets()

    def load_assets(self):
        """Carga las imágenes necesarias"""
        base_path = os.path.join("ui", "sprites")
        self.llama_img = pygame.image.load(os.path.join(base_path, "llama_idle.png"))
        self.llama_img = pygame.transform.scale(self.llama_img, (CELL_SIZE, CELL_SIZE))

        self.goal_img = pygame.image.load(os.path.join(base_path, "goal.png"))
        self.goal_img = pygame.transform.scale(self.goal_img, (CELL_SIZE, CELL_SIZE))

        self.obstacle_img = pygame.image.load(os.path.join(base_path, "obstacle.png"))
        self.obstacle_img = pygame.transform.scale(self.obstacle_img, (CELL_SIZE, CELL_SIZE))

    def draw_grid(self):
        """Dibuja el grid de fondo"""
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, COLOR_GRID, rect, 1)

    def draw_entities(self):
        """Dibuja los elementos del juego"""
        for (row, col) in self.env.obstacles:
            self.screen.blit(self.obstacle_img, (col * CELL_SIZE, row * CELL_SIZE))

        goal_r, goal_c = self.env.goal_pos
        self.screen.blit(self.goal_img, (goal_c * CELL_SIZE, goal_r * CELL_SIZE))

        agent_r, agent_c = self.env.agent_pos
        self.screen.blit(self.llama_img, (agent_c * CELL_SIZE, agent_r * CELL_SIZE))

    def draw(self):
        """Dibuja todo"""
        self.draw_grid()
        self.draw_entities()
