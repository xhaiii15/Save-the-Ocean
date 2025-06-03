import pygame
import sys

# Initialize pygame
pygame.init()

width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Save The Ocean")
background_image = pygame.image.load("1_game_background (1).png")

start_img = pygame.image.load("play.png").convert_alpha()
exit_img = pygame.image.load("quit.png").convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = Button(10, 350, start_img, 0.5)
exit_button = Button(250, 350, exit_img, 0.5)

def run_game():
    import Main  # Import your game logic from "Main.py"

    Main.run()  # Assuming you have a "run" function in "Main.py

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))
    if start_button.draw():
        run_game()  # Start the main game loop in "Main.py"

    if exit_button.draw():
        pygame.quit()
        sys.exit()

    pygame.display.update()

pygame.quit()
