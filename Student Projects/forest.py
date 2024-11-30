import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions and the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Adventure Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)  # Forest green color
BROWN = (139, 69, 19)  # Tree trunk color

# Player settings
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Tree settings
tree_width = 40
tree_height = 60
tree_count = 10

# Load background image (ensure you have an image named "forest_background.jpg")
# If you don't have an image, use a solid color background like before
try:
    background = pygame.image.load("forest_background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    background = None  # Use solid color if no image is found

# Generate random tree positions
trees = []
for _ in range(tree_count):
    tree_x = random.randint(0, SCREEN_WIDTH - tree_width)
    tree_y = random.randint(0, SCREEN_HEIGHT - tree_height)
    trees.append((tree_x, tree_y))

# Game loop flag
running = True

# Set up clock for frame rate control
clock = pygame.time.Clock()

# Game loop
while running:
    # Handle events (keyboard, closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of the keyboard (arrow keys)
    keys = pygame.key.get_pressed()

    # Move the player based on arrow keys
    if keys[pygame.K_LEFT]:  # Left arrow key
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:  # Right arrow key
        player_x += player_speed
    if keys[pygame.K_UP]:  # Up arrow key
        player_y -= player_speed
    if keys[pygame.K_DOWN]:  # Down arrow key
        player_y += player_speed

    # Prevent the player from going out of bounds
    player_x = max(0, min(SCREEN_WIDTH - player_size, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_size, player_y))

    # Fill the screen with the background or white if no image
    if background:
        screen.blit(background, (0, 0))  # Draw the background image
    else:
        screen.fill(WHITE)  # Use white background if no image

    # Draw trees (green rectangles)
    for tree in trees:
        pygame.draw.rect(screen, GREEN, (tree[0], tree[1], tree_width, tree_height))  # Tree foliage
        pygame.draw.rect(screen, BROWN, (tree[0] + tree_width // 3, tree[1] + tree_height, tree_width // 3, tree_height // 2))  # Tree trunk

    # Draw the player (red square)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Update the screen
    pygame.display.update()

    # Set the frame rate (60 frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
