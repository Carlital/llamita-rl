def pos_to_pixel(col, row, cell_size):
    """Convierte coordenadas del grid a posición en pantalla (px)"""
    return col * cell_size, row * cell_size

def pixel_to_pos(x, y, cell_size):
    """Convierte coordenadas en píxeles a posición de celda"""
    return y // cell_size, x // cell_size

def clamp(value, min_value, max_value):
    """Limita un valor dentro de un rango"""
    return max(min_value, min(value, max_value))

def format_action(action):
    """Convierte acciones a símbolos"""
    return {
        "UP": "⬆",
        "DOWN": "⬇",
        "LEFT": "⬅",
        "RIGHT": "➡"
    }.get(action, str(action))

def traducir_accion(action):
    """Traduce una acción RL al español"""
    return {
        "UP": "arriba",
        "DOWN": "abajo",
        "LEFT": "izquierda",
        "RIGHT": "derecha"
    }.get(action, str(action))

