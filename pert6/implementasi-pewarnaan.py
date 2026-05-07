import pygame

# Inisialisasi pygame
pygame.init()

# Ukuran window
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pewarnaan Objek")

# Warna RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

running = True
while running:
    screen.fill(WHITE)

    # Membuat objek berwarna
    pygame.draw.rect(screen, RED, (50, 50, 150, 100))
    pygame.draw.circle(screen, GREEN, (350, 100), 50)
    pygame.draw.polygon(screen, BLUE, [(450, 50), (550, 150), (400, 150)])
    pygame.draw.line(screen, YELLOW, (50, 250), (550, 350), 5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()