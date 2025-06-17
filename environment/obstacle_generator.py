import random
from collections import deque

def es_camino_valido(inicio, obstacles, rows, cols, pasos_minimos=3):
    visitados = set()
    cola = deque([inicio])
    direcciones = [(0,1),(1,0),(-1,0),(0,-1)]

    while cola and len(visitados) < pasos_minimos:
        r, c = cola.popleft()
        if (r, c) in visitados or (r, c) in obstacles:
            continue
        visitados.add((r, c))

        for dr, dc in direcciones:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cola.append((nr, nc))

    return len(visitados) >= pasos_minimos

def hay_camino(inicio, objetivo, obstacles, rows, cols):
    visitados = set()
    cola = deque([inicio])
    direcciones = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while cola:
        r, c = cola.popleft()
        if (r, c) == objetivo:
            return True
        if (r, c) in visitados or (r, c) in obstacles:
            continue
        visitados.add((r, c))
        for dr, dc in direcciones:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cola.append((nr, nc))
    return False

def generate_random_obstacles(rows, cols, count, forbidden_positions=None):
    obstacles = set()
    forbidden_positions = forbidden_positions or []
    intentos = 0
    inicio = (0, 0)
    meta = (rows - 1, cols - 1)

    while True:
        obstacles.clear()
        while len(obstacles) < count:
            pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))
            if pos not in forbidden_positions and pos != inicio and pos != meta:
                obstacles.add(pos)

        if es_camino_valido(inicio, obstacles, rows, cols) and hay_camino(inicio, meta, obstacles, rows, cols):
            break

        intentos += 1
        if intentos > 1000:
            raise Exception("No se pudo generar un entorno válido con camino a la meta")

    return obstacles

def generate_fixed_obstacles(rows, cols, level=1):
    """
    Genera obstáculos fijos según un nivel prediseñado.
    Esto es útil si quieres tener niveles tipo 'historia'.
    """
    if level == 1:
        return {(2, 2), (3, 3), (4, 2), (1, 5)}
    elif level == 2:
        return {(0, 3), (1, 3), (2, 3), (3, 3), (4, 4)}
    elif level == 3:
        return {(5, 5), (5, 6), (6, 5), (3, 3), (2, 4)}
    else:
        return set()
