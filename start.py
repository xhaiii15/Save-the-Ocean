import pygame
import sys

# Initialize pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# Play background music
pygame.mixer.music.load("game_music_sounds/bloxfruit_bgmusic.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Save The Ocean")
background_image = pygame.image.load("game_bg/1_game_background (1).png")

start_img = pygame.image.load("play_img/play.png").convert_alpha()
exit_img = pygame.image.load("quit_img/quit.png").convert_alpha()

logo_img = pygame.image.load("logo_img/logo.png").convert_alpha()
logo_width = 400
logo_height = 400
logo_img = pygame.transform.scale(logo_img, (logo_width, logo_height))


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
    import Main  # Import  "Main.py"
    Main.run()  # run function in "Main.py

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))
    screen.blit(logo_img, (50, 10))
    
    if start_button.draw():
        run_game()  # Start the main game "Main.py"

    if exit_button.draw():
        pygame.quit()
        sys.exit()

    pygame.display.update()

pygame.quit()
