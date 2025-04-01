from character import Character

class Player(Character):
    def __init__(self, x, y, image, lives=3):
        super().__init__(x, y, image, lives)
        self.score = 0

    def move(self, dx, dy):
        if self.is_alive:
            super().move(dx, dy)

    def shoot(self):
        pass  # Implementar disparo más adelante
