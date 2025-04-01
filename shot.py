from entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def move(self, dy):
        self.y += dy

    def hit_target(self, target):
        if self.rect.colliderect(target.rect):
            return True
        return False
