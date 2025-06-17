import pygame
from config import CELL_SIZE, GRID_COLS
from utils.helpers import format_action
from utils.helpers import traducir_accion

class Sidebar:
    def __init__(self, screen, agent):
        self.screen = screen
        self.agent = agent
        self.font = pygame.font.SysFont("consolas", 20)
        self.x_offset = CELL_SIZE * GRID_COLS + 20
        self.q_cargada = len(agent.q.q_table) > 0


    def draw_text(self, text, y):
        """Dibuja texto alineado a la derecha del grid"""
        label = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(label, (self.x_offset, y))

    def draw(self):
        """Renderiza el panel de información RL"""
        state = self.agent.state
        episode = self.agent.episode
        q = self.agent.q.q_table.get(state, {})
        best_action = self.agent.q.get_best_action(state, self.agent.env.get_possible_actions()) if q else "N/A"
        q_value = q.get(best_action, 0) if q else 0

        last_s = self.agent.last_state
        last_a = self.agent.last_action
        last_r = self.agent.last_reward
        last_s_ = self.agent.last_next_state

        y = 20
        self.draw_text(f"[Llamita RL]", y); y += 30
        self.draw_text(f"Episodio: {episode}", y); y += 40

        self.draw_text("Ciclo de Aprendizaje RL", y); y += 30
        self.draw_text(f"1. Estado S: {last_s if last_s else '...'}", y); y += 25
        accion_texto = traducir_accion(last_a) if last_a else "..."
        self.draw_text(f"2. Acción A: {accion_texto}", y); y += 25
        self.draw_text(f"3. Recompensa R: {last_r if last_r is not None else '...'}", y); y += 25
        self.draw_text(f"4. Siguiente S': {last_s_ if last_s_ else '...'}", y); y += 25
        self.draw_text(f"5. Q(S,A): {round(q_value, 2)}", y); y += 40
        estado = "Cargada" if self.q_cargada else "Nueva"
        self.draw_text(f"Q-table: {estado}", y + 30)
