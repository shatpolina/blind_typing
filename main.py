text_us: str = "Hi! Print this message: solution worked!"
text_ru: str = "Привет! Напечатай это сообщение: решение работает!"

import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (500, 250), 75)

    pygame.display.flip()

pygame.quit()
