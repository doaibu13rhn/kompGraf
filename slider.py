import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

r, g, b = 100, 100, 100

running = True
while running:
    screen.fill((r, g, b))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]: r = min(255, r+1)
    if keys[pygame.K_a]: r = max(0, r-1)
    if keys[pygame.K_w]: g = min(255, g+1)
    if keys[pygame.K_s]: g = max(0, g-1)
    if keys[pygame.K_e]: b = min(255, b+1)
    if keys[pygame.K_d]: b = max(0, b-1)

    pygame.display.flip()

pygame.quit()