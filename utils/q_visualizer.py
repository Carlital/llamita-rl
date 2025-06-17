import pygame
from config import CELL_SIZE

COLOR_POSITIVE = (0, 200, 0)
COLOR_NEGATIVE = (200, 0, 0)
COLOR_NEUTRAL = (180, 180, 180)

def draw_q_overlay(screen, q_table, cell_size, offset_x=0):
    """Dibuja valores Q encima de cada celda (como color de fondo tenue)"""
    font = pygame.font.SysFont("consolas", 14)

    for state, actions in q_table.items():
        row, col = state
        max_q = max(actions.values()) if actions else 0

        if max_q > 0:
            color = COLOR_POSITIVE
        elif max_q < 0:
            color = COLOR_NEGATIVE
        else:
            color = COLOR_NEUTRAL

        x = offset_x + col * cell_size
        y = row * cell_size
        rect = pygame.Rect(x, y, cell_size, cell_size)
        surface = pygame.Surface((cell_size, cell_size))
        surface.set_alpha(60)
        surface.fill(color)
        screen.blit(surface, rect)

        txt = font.render(f"{max_q:.1f}", True, (0, 0, 0))
        screen.blit(txt, (x + 5, y + 5))
