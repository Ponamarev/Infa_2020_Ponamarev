import pygame

pygame.init()


  # This color contains an extra integer. It's the alpha value.
PURPLE = (255, 0, 255)
screen = pygame.display.set_mode((200, 325))
 # Make the background white. Remember that the screen is a Surface!
clock = pygame.time.Clock()


def test():
    purple_image = pygame.Surface(size)
    purple_image.set_colorkey(BLACK)
    purple_image.set_alpha(50)

    pygame.draw.rect(purple_image, PURPLE, purple_image.get_rect(), 10)

    pygame.draw.rect(purple_image, PURPLE, purple_image.get_rect(), 10)
    screen.blit(purple_image, (75, 250))


size = (50, 50)
 # Contains a flag telling pygame that the Surface is per-pixel alpha
purple_image = pygame.Surface(size)
purple_image.set_alpha(50)
pygame.draw.rect(purple_image, PURPLE, purple_image.get_rect(), 10)
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:

            screen.blit(purple_image, (75, 250))

    pygame.display.update()
