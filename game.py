import pygame
from player import Player
from opponent import Opponent
from game import Game
from shot import Shot

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga - Game")

player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))

opponent_image = pygame.Surface((50, 50))
opponent_image.fill((255, 0, 0))

bullet_image = pygame.Surface((5, 10))
bullet_image.fill((255, 255, 0))

opponent_bullet_image = pygame.Surface((5, 10))
opponent_bullet_image.fill((0, 0, 255))

player = Player(x=screen_width // 2, y=screen_height - 60, image=player_image)
opponent1 = Opponent(x=100, y=100, image=opponent_image)
opponent2 = Opponent(x=200, y=100, image=opponent_image)

game = Game()
game.start(player)
game.opponents = [opponent1, opponent2]

bullets = []
enemy_bullets = []
opponent_direction = 1

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_SPACE]:
        bullet = Shot(player.x + player.image.get_width() // 2, player.y, bullet_image, speed=-5)
        bullets.append(bullet)

    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            for opponent in game.opponents[:]:
                if bullet.hit_target(opponent) and not opponent.is_star:
                    opponent.convert_to_star(player)
                    game.opponents.remove(opponent)
                    bullets.remove(bullet)
                    break

    for opponent in game.opponents:
        opponent.move(opponent_direction, 0)
        if opponent.x <= 0 or opponent.x >= screen_width - opponent.image.get_width():
            opponent_direction *= -1

        if pygame.time.get_ticks() % 100 == 0:
            enemy_bullet = opponent.shoot(opponent_bullet_image)
            enemy_bullets.append(enemy_bullet)

    for enemy_bullet in enemy_bullets[:]:
        enemy_bullet.move()
        if enemy_bullet.y > screen_height:
            enemy_bullets.remove(enemy_bullet)
        elif enemy_bullet.hit_target(player):
            player.lives -= 1
            enemy_bullets.remove(enemy_bullet)
            if player.lives <= 0:
                game.end_game()
                running = False

    player.draw(screen)
    for opponent in game.opponents:
        opponent.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy_bullet in enemy_bullets:
        enemy_bullet.draw(screen)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()