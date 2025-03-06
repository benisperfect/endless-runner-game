import pygame as py
import random 

py.init()

# screen const
screen_width = 840
screen_height = 650
screen = py.display.set_mode([screen_width, screen_height], py.RESIZABLE)
Clock = py.time.Clock()
game_font = py.font.Font("assets/04B_19.ttf", 40)
score = 0
high_score = 0
white = (255, 255, 255)

running = True
road_y = 0
road = py.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/image/road.png")

game_over_surface = py.transform.scale2x(py.image.load("C:/Users/ADMIN/OneDrive - 4x56ts/Desktop/FLAPPY BIRD/image/message.png"))
game_over_rect = game_over_surface.get_rect(center = (216, 330))

# object1 variables
character1 = py.image.load("assets/character1.png")
character2 = py.image.load("assets/character2.png")
character3 = py.image.load("assets/character3.png")
character4 = py.image.load("assets/character4.png")
character5 = py.image.load("assets/character5.png")
character6 = py.image.load("assets/character6.png")
character7 = py.image.load("assets/character7.png")
character8 = py.image.load("assets/character8.png")
index = 0
character_list = [character1, character2, character3, character4, character5, character6, character7, character8]
character = character_list[index]
character_get_rect = character.get_rect(center=(screen_width // 2, screen_height // 2))
character_timer = py.USEREVENT
py.time.set_timer(character_timer, 100)
character_x = screen_width // 2 - character.get_width() // 2 + 66
character_y = screen_height // 2 - character.get_height() // 2 + 120

# object 2 variables
obstacle1 = py.image.load("assets/obstacle1.png").convert_alpha()
obstacle2 = py.image.load("assets/obstacle2.png").convert_alpha()
obstacle3 = py.image.load("assets/obstacle3.png").convert_alpha()
obstacle4 = py.image.load("assets/obstacle4.png").convert_alpha()
obstacle5 = py.image.load("assets/obstacle5.png").convert_alpha()
obstacle6 = py.image.load("assets/obstacle6.png").convert_alpha()
obstacle7 = py.image.load("assets/obstacle7.png").convert_alpha()
obstacle_list = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7]

car_choices = random.choice(obstacle_list)
speed_list = [1, 2, 3]
random_lane = [192, 321, 455, 583]
lanes = [random.choice(random_lane) for _ in range(len(obstacle_list))]
for i in range(len(obstacle_list)):
    obstacle = obstacle_list[i]
    obstacle_rect = obstacle.get_rect(topleft=(lanes[i], -200))
speeds = random.choice(speed_list)


rect_topleft_y_pos, rect_topright_y_pos = 20, 20
rect_bottomleft_y_pos, rect_bottomright_y_pos = 120, 120
random_coordinate_list = []