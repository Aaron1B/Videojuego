from entity import Entity

class Character(Entity):
    def __init__(self, x, y, image, lives=3):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self, dx, dy):
        if self.is_alive:
            super().move(dx, dy)

    def shoot(self):
        pass  

    def collide(self, other):
        if self.rect.colliderect(other.rect): 
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False
