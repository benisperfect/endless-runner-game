import pygame as py

# Initialize Pygame
py.init()

def character_animation(index, character_list):
    if index < len(character_list):
        index += 1
    if index >= len(character_list):
        index = 0
    return character_list[index]

# Screen settings
screen_width, screen_height = 840, 650
screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Show Rect Around Object")

# Load character frames
character1 = py.image.load("assets/character1.png")
character2 = py.image.load("assets/character2.png")
character3 = py.image.load("assets/character3.png")
character4 = py.image.load("assets/character4.png")
character5 = py.transform.scale2x(py.image.load("assets/character5.png"))
character6 = py.image.load("assets/character6.png")
character7 = py.image.load("assets/character7.png")
character8 = py.image.load("assets/character8.png")

# Character animation setup
character_list = [character1, character2, character3, character4, character5, character6, character7, character8]
index = 0
character = character_list[index]
character_rect = character.get_rect(center=(screen_width // 2, screen_height // 2))

character_timer = py.USEREVENT
py.time.set_timer(character_timer, 1000)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == character_timer:
            # Change character frame
            index = (index + 1) % len(character_list)
            character = character_list[index]
            
            # **Update character rect to match the new character size**
            character_rect = character.get_rect(center=(screen_width // 2, screen_height // 2))

    # Draw the character
    screen.blit(character, character_rect.topleft)

    # Draw a red rect around the character
    py.draw.rect(screen, RED, character_rect, 2)  # Thickness = 2

    # Update display
    py.display.flip()

py.quit()
