import pygame
from player import Player
from opponent import Opponent
from game import Game
from shot import Shot

# Inicializar Pygame
pygame.init()

# Definir algunas configuraciones del juego
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga - Game")

# Cargar imágenes
player_image = pygame.Surface((50, 50))  # Reemplaza con la imagen de tu jugador
player_image.fill((0, 255, 0))  # Color verde para el jugador

opponent_image = pygame.Surface((50, 50))  # Reemplaza con la imagen del oponente
opponent_image.fill((255, 0, 0))  # Color rojo para los enemigos

bullet_image = pygame.Surface((5, 10))  # Reemplaza con la imagen de tu bala
bullet_image.fill((255, 255, 0))  # Color amarillo para las balas

# Crear el jugador y los oponentes
player = Player(x=screen_width // 2, y=screen_height - 60, image=player_image)
opponent1 = Opponent(x=100, y=100, image=opponent_image)
opponent2 = Opponent(x=200, y=100, image=opponent_image)

# Crear el juego
game = Game()

# Iniciar el juego
game.start(player)

# Lista de oponentes
game.opponents = [opponent1, opponent2]

# Lista de disparos
bullets = []

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Limpiar la pantalla con color negro

    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica de movimiento y disparo del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_SPACE]:
        # Disparar una bala
        bullet = Shot(player.x + player.image.get_width() // 2, player.y, bullet_image)
        bullets.append(bullet)

    # Actualizar las balas
    for bullet in bullets[:]:
        bullet.move(-5)
        if bullet.y < 0:
            bullets.remove(bullet)  # Eliminar las balas que salen de la pantalla

    # Comprobar colisiones entre el jugador y los oponentes
    for opponent in game.opponents[:]:
        if player.rect.colliderect(opponent.rect):  # Si el jugador colisiona con un oponente
            opponent.convert_to_star(player)  # Convertir al oponente en estrella y sumar puntos

    # Dibuja el jugador, oponentes y balas
    player.draw(screen)
    for opponent in game.opponents:
        opponent.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    # Mostrar la puntuación
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el framerate
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
