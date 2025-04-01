

class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
