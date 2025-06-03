import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
FALL_SPEED = 2  # fall speed 

# Value for desired spawn rate
FISH1_SPAWN_RATE = 500 
FISH2_SPAWN_RATE = 550  
FISH3_SPAWN_RATE = 600
TRASH1_SPAWN_RATE = 500  
TRASH2_SPAWN_RATE = 550  
TRASH3_SPAWN_RATE = 600

# Initialize Music
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Save the Ocean')

# Sound files
good_item_sound = pygame.mixer.Sound('coinpoint.wav')
bad_item_sound = pygame.mixer.Sound('bubblepop.wav')
player_movement_sound = pygame.mixer.Sound('movement.wav')

# Volume levels
good_item_sound.set_volume(0.2)
bad_item_sound.set_volume(0.1)
player_movement_sound.set_volume(0.01)

# Load game assets
background_image = pygame.image.load('1_game_background (1).png')
player_image = pygame.transform.scale(
    pygame.image.load('cactus-mccoy-2-the-ruins-of-calavera-butterfly-net-clip-art-net-thumbnail-removebg-preview.png'),
    (65, 65)
)
fish1 = pygame.transform.scale(
    pygame.image.load('fish1.png'),
    (85, 85)
)
fish2 = pygame.transform.scale(
    pygame.image.load('fish2.png'),
    (85, 85)
)
fish3 = pygame.transform.scale(
    pygame.image.load('fish3.png'),
    (85, 85)
)
trash1 = pygame.transform.scale(
    pygame.image.load('trash1.png'),
    (90, 90)
)
trash2 = pygame.transform.scale(
    pygame.image.load('trash2.png'),
    (70, 70)
)
trash3 = pygame.transform.scale(
    pygame.image.load('trash3.png'),
    (100, 100)
)


class FallingObject:
    def __init__(self, type_index):
        self.image, self.is_good = falling_object_types[type_index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 100)
        self.rect.y = -100  # Start above the screen
        self.speed = FALL_SPEED

    def move(self):
        self.rect.y += self.speed

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - 100)
        self.rect.y = -100  # Reset above the screen

# List of FallingObject instances
falling_object_types = [
    (fish1, False),  # -1 life
    (fish2, False),  # -1 life
    (fish3, False),  # -1 life
    (trash1, True),  # +1 points
    (trash2, True),  # +1 points
    (trash3, True),  # +1 points
                                  
]

# Play background music
pygame.mixer.music.load("bloxfruit_bgmusic.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

# Function to draw the background image
def draw_background():
    screen.blit(pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


# Load button images
try_again_button_image = pygame.image.load('play.png')
quit_button_image = pygame.image.load('quit.png')

def game_over_screen():
    original_game_over_image = pygame.image.load('gameover.png')  
    new_width = 450  # Set the new width you want
    new_height = 250  # Set the new height you want
    game_over_image = pygame.transform.scale(original_game_over_image, (new_width, new_height))

    # Change the location of the image
    game_over_x = 30  # Set the new X coordinate
    game_over_y = 100  # Set the new Y coordinate

    screen.blit(game_over_image, (game_over_x, game_over_y))
    
    try_again_button_image = pygame.transform.scale(pygame.image.load('play.png'), (250, 250))
    quit_button_image = pygame.transform.scale(pygame.image.load('quit.png'), (250, 250))
    
    try_again_button_rect = screen.blit(try_again_button_image, (10, 350))
    quit_button_rect = screen.blit(quit_button_image, (250, 350))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if try_again_button_rect.collidepoint(mouse_x, mouse_y):
                    return True  # Try Again
                elif quit_button_rect.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
# Main game loop
def run():
    pygame.init()
    # Initialize the player position
    player_x = 200
    player_y = 500
    
    running = True
    player_life = 10  # Initial player life
    player_score = 0  # Initial player score
    fish_1 = 0
    fish_2 = 0
    fish_3 = 0
    trash_1 = 0
    trash_2 = 0
    trash_3 = 0
    
    falling_objects = []  # Initialize the falling objects

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
            player_movement_sound.play()
              
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED
            player_movement_sound.play()
            
        # Player screen bounds
        player_x = max(0, min(player_x, SCREEN_WIDTH - 100))

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the background
        draw_background()

        # Spawn random intervals
        if fish_1 % FISH1_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))

        if fish_2 % FISH2_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))
            
        if fish_3 % FISH3_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))
            
        if trash_1 % TRASH1_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))
            
        if trash_2 % TRASH2_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))
            
        if trash_3 % TRASH3_SPAWN_RATE == 0:
            type_index = random.randint(0, len(falling_object_types) - 1)
            falling_objects.append(FallingObject(type_index))

        # Move and draw falling objects
        for obj in falling_objects:
            obj.move()
            screen.blit(obj.image, obj.rect)

            # Collision detection with player
            if obj.rect.colliderect(pygame.Rect(player_x, player_y, 100, 100)):
                if obj.is_good:
                    # Player collected a good item 
                    player_score += 1
                    good_item_sound.play()
                else:
                    # Player collided with a bad item
                    player_life -= 1
                    bad_item_sound.play()

                falling_objects.remove(obj)  # Remove the collected object

            # Remove objects that go out of the screen
            if obj.rect.y > SCREEN_HEIGHT:
                falling_objects.remove(obj)

        # Draw the player
        screen.blit(player_image, (player_x, player_y))

        # Display player life and score
        font = pygame.font.Font(None, 36)
        life_text = font.render(f'Life: {player_life}', True, (0, 0, 0))
        score_text = font.render(f'Score: {player_score}', True, (0, 0, 0))

        # Position the score at the middle top of the screen
        score_x = (SCREEN_WIDTH - score_text.get_width()) // 2
        score_y = 10  

        screen.blit(life_text, (10, 10))  # life text in the top-left corner
        screen.blit(score_text, (score_x, score_y))  # score text position

        # Check for game over (when player life is zero)
        if player_life <= 0:
            if game_over_screen():
                # Reset the game state
                player_life = 10
                player_score = 0
                falling_objects = []
            else:
                running = False
      
        # Update the display
        pygame.display.update()

        # Increase the counters
        fish_1 += 1
        fish_2 += 1
        fish_3 += 1
        trash_1 += 1
        trash_2 += 1
        trash_3 += 1
       
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run()
