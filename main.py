import pygame, sys, random
from variable import *
from function import *
from gamefunction import *

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Jerry silver chase")

running = True
obstacle_rects = [obstacle.get_rect(topleft=(random.choice(random_lane), -200)) for obstacle in obstacle_list]
car_choices = random.sample(obstacle_list, len(obstacle_rects))
lanes = [random.choice(random_lane) for _ in range(len(obstacle_rects))]
speeds = [random.choice(speed_list) for _ in range(len(obstacle_rects))]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    draw_road(road_y)
    if road_y >= screen_height:
        road_y = 0
    character_get_rect.topleft = (character_x, character_y)

    character_rect = character.get_rect(topleft=(character_x, character_y))
    screen.blit(character, (character_x, character_y))
    py.draw.rect(screen, "red", character_rect, 2)
    car_choices, lanes, speeds = draw_move_obstacle(screen, obstacle_rects, obstacle_list, car_choices, lanes, speeds, random_lane, speed_list)

    if collide(character_get_rect, obstacle_rects):
        running = False
        print("Game Over!")
    pygame.display.flip()
    Clock.tick(120)
