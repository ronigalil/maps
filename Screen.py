import pygame
import consts



pygame.init()
size = (consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ביתילי לחייל")
finish = False
# COLOR
WHITE = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()
# RUN
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()
# MOUSE
mouse_point = pygame.mouse.get_pos()
