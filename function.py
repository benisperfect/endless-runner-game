import pygame as py
from variable import *
from gamefunction import *

py.init()

def character_animation(index, character_list):
    if index < len(character_list):
        index += 1
    if index >= len(character_list):
        index = 0
    return character_list[index]

def draw_road(road_y):
    screen.blit(road, (0, road_y))
    screen.blit(road, (0, road_y - screen_height))

def draw_move_obstacle(screen, obstacle_rects, obstacle_list, car_choices, lanes, speeds, random_lane, speed_list):
    for i in range(len(obstacle_rects)):
        obstacle_rects[i].top += speeds[i]
        if obstacle_rects[i].top >= screen_height:
            obstacle_rects[i].top = -200
            lanes[i] = random.choice(random_lane)
            speeds[i] = random.choice(speed_list)
            car_choices[i] = random.choice(obstacle_list)
            for i in range(len(obstacle_rects)):
                for j in range(i, len(obstacle_rects)):
                    if lanes[i] == lanes[j] and i != j and obstacle_rects[i].colliderect(obstacle_rects[j]):
                        obstacle_rects[j].top -= 120                        
        screen.blit(car_choices[i], (lanes[i], obstacle_rects[i].top))
        py.draw.rect(screen, "red", obstacle_rects[i], 2)
    return car_choices, lanes, speeds

def collide(character_rect, obstacle_rects):
    for obstacle_rect in obstacle_rects:
        if character_rect.colliderect(obstacle_rect):
            return True
    return False