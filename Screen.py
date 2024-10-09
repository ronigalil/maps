import pygame
import consts
import sys


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
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

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    # it will set background color of screen
    screen.fill((255, 255, 255))

    if active:
        color = color_active
    else:
        color = color_passive

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(150, text_surface.get_width() + 10)


    pygame.display.flip()
    clock.tick(60)

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
