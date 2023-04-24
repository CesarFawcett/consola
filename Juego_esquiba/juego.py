import pygame
from Player import Player
from Enemy import Enemy
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla y el ancho de los carriles
size = (650, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mi juego")
carril_width = size[0] // 5

# Crear al jugador en el carril del medio
player = Player(3 * carril_width, size[1] - 100, "play1.png")

# Crear una lista vacía para almacenar a los enemigos
enemies = []
last_enemy_time = pygame.time.get_ticks()


def generar_enemigo():
    global last_enemy_time
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_time > 600:
        carril = random.randint(1, 4)
        enemy = Enemy(carril_width * carril-20, -50, "enem.png")
        enemies.append(enemy)
        last_enemy_time = current_time

paused = False
keys = pygame.key.get_pressed()
while not paused:
    # Procesar eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()

    # Actualizar la posición del jugador y dibujarlo en la pantalla
    screen.fill((0, 0, 0))
    player.draw(screen)

    # Generar enemigos aleatorios
    generar_enemigo()

    # Mover y dibujar los enemigos
    for enemy in enemies:
        enemy.move_down()
        enemy.draw(screen)

    pygame.display.update()
