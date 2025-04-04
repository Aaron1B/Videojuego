from character import Character

class Opponent(Character):
    def __init__(self, x, y, image, is_star=False):
        super().__init__(x, y, image)
        self.is_star = is_star

    def move(self, dx, dy):
        if self.is_alive:
            super().move(dx, dy)

    def shoot(self):
        pass  

    def convert_to_star(self, player):
        if not self.is_star:
            self.is_star = True
            player.score += 10  
