import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

# RGB colors
red = (225, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, red, (50, 50, 100, 100))
    pygame.draw.circle(screen, green, (250, 100), 50)
    pygame.draw.line(screen, blue, (50, 300), (300, 300), 5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()