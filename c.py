import pygame
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((1200,800))
width, height = 1200 // 2, 800 // 2
done = False
image = pygame.image.load('micky.jpg')
sec = pygame.image.load('hand2.png')
mik_sec = sec.get_rect('hand2.png')
minute = pygame.image.load('hand1.png')
mik_min = minute.get_rect(center=(width,height))
mic_rect = image.get.rect(center = (width, height))
font = pygame.font.SysFont('Micky', 100)
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        screen.fill((255,255,255))
        time = datetime.datetime.now()
        time.render = font.render(time.strftime("%H:%M:%S"), True, 
        pygame.Color('black'), pygame.Color('white'))