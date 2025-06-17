import pygame
import sys
from config import *
from environment.environment import GameEnvironment
from agent.llama_agent import LlamaAgent
from ui.renderer import Renderer
from ui.sidebar import Sidebar

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * GRID_COLS + 300, CELL_SIZE * GRID_ROWS))
pygame.display.set_caption("Llamita RL - Inteligencia de Altura")

clock = pygame.time.Clock()

env = GameEnvironment(GRID_ROWS, GRID_COLS)
agent = LlamaAgent(env)
renderer = Renderer(screen, env, agent)
sidebar = Sidebar(screen, agent)

running = True
while running:
    screen.fill(COLOR_BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent.train_step()

    renderer.draw()
    sidebar.draw()

    pygame.display.flip()
    clock.tick(8)

pygame.quit()
sys.exit()
