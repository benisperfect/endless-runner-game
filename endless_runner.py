import pygame, sys, random

pygame.init()

def character_animation(index, character_list):
    if index < len(character_list):
        index += 1
    if index >= len(character_list):
        index = 0
    return character_list[index]

def random_obstacle(obstacle_list):
    obstacle_index = random.randint(0, len(obstacle_list)-1)
    obstacle = obstacle_list[obstacle_index]
    obstacle_rect = obstacle.get_rect(center=(390, 0))  
    return obstacle, obstacle_rect

def draw_road():
    screen.blit(road, (0, road_y))
    screen.blit(road, (0, road_y-screen_height))

def move_obstacle(obstacle_x, obstacle_y):
    obstacle_y += 1.5
    if obstacle_y >= screen_height:
        obstacle_y = 0
        obstacle_x = 390  
    return obstacle_x, obstacle_y

def draw_obstacle():
    for obstacle_rect in obstacle_place_list:
        screen.blit(obstacle, obstacle_rect)

def change_obstacle(obstacle_list):
    new_obstacle = random_obstacle(obstacle_list)
    

screen_width = 840
screen_height = 650
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Jerry silver chase")
Clock = pygame.time.Clock()

road = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/road.png")
road_y = 0

character1 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character1.png")
character2 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character2.png")
character3 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character3.png")
character4 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character4.png")
character5 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character5.png")
character6 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character6.png")
character7 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character7.png")
character8 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/character8.png")
index = 0
character_list = [character1, character2, character3, character4, character5, character6, character7, character8]
character = character_list[index]
character_get_rect = character.get_rect(center=(screen_width // 2, screen_height // 2))
character_timer = pygame.USEREVENT
pygame.time.set_timer(character_timer, 100)
character_x = screen_width // 2 - character.get_width() // 2 + 66
character_y = screen_height // 2 - character.get_height() // 2 + 120

# obstacle
obstacle1 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/obstacle1.png").convert_alpha()
obstacle2 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/obstacle2.png").convert_alpha()
obstacle3 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/obstacle3.png").convert_alpha()
obstacle4 = pygame.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/obstacle4.png").convert_alpha()
obstacle_list = [obstacle1, obstacle2, obstacle3, obstacle4]
obstacle_place_list = []
obstacle_index = 0
obstacle = obstacle_list[obstacle_index]
obstacle_rect = obstacle.get_rect(center=(screen_width // 2, screen_height // 2))
obstacle_changer = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_changer, 2000)
spawn_obstacle = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_obstacle, 1200)

rect_topleft_y_pos, rect_topright_y_pos = 20, 20
rect_bottomleft_y_pos, rect_bottomright_y_pos = 120, 120
random_coordinate_list = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == character_timer:
            index += 1
            if index >= 8:
                index = 0
            character = character_list[index]
            character = character_animation(index, character_list)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                character_x -= 135
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                character_x += 135
        character_x = min(max(195, character_x), 585)
    
    road_y += 2.5
    draw_road()
    if road_y >= screen_height:
        road_y = 0
    screen.blit(character, (character_x, character_y))
    draw_obstacle()
    pygame.draw.polygon(screen, "cyan", [(200, rect_topleft_y_pos), #topleft
    (250, rect_topright_y_pos), #topright
    (250, rect_bottomright_y_pos), #bottomright
    (200, rect_bottomleft_y_pos)], #bottomleft
    3)

    rect_topleft_y_pos += 1
    rect_topright_y_pos += 1
    rect_bottomright_y_pos += 1
    rect_bottomleft_y_pos += 1
    if rect_topleft_y_pos >= screen_height and rect_topright_y_pos >= screen_height:
        rect_topleft_y_pos, rect_topright_y_pos = 20, 20
        rect_bottomleft_y_pos, rect_bottomright_y_pos = 120, 120

    pygame.display.flip()
    Clock.tick(120)

pygame.quit()
sys.exit()