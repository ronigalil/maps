import pygame
import consts
import sys


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 160, 32)
color_active = pygame.Color(consts.PURPLE)
color_passive = pygame.Color(consts.VIOLET)
color = color_passive
active = False

while True:
    for event in pygame.event.get():

        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:


def initialize_screen():
    size = (consts.WINDOW_HEIGHT, consts.WINDOW_WIDTH)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("ביתילי לחייל")
    finish = False
    # COLOR
    screen.fill(consts.WHITE)
    pygame.display.flip()
    # RUN
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
    pygame.quit()


    # MOUSE
    mouse_point = pygame.mouse.get_pos()
