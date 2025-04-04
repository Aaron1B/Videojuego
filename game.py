import pygame
from player import Player
from opponent import Opponent
from shot import Shot

class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponents = []
        self.is_running = False

    def start(self, player):
        self.player = player
        self.is_running = True

    def update(self):
        """Actualiza la lógica del juego."""
        for opponent in self.opponents:
            if opponent.is_alive and opponent.is_star:
                print(f"¡El jugador ha ganado {self.player.score} puntos!")
                

    def end_game(self):
        self.is_running = False
