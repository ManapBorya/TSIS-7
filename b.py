import pygame
pygame.init()

scrn = pygame.display.set_mode((400,500))
pygame.display.set_caption('Hello World')

iii = pygame.image.load('qwerty.jpeg').convert()
scrn.blit(iii, (0, 0))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()