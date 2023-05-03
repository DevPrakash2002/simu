import random
import pygame
import time
import math
import threading

pygame.init()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


road = pygame.image.load("road.png")
grass = scale_image(pygame.image.load("grass.png"), 0.45)
bike = pygame.image.load("bike.png")
car = pygame.image.load("car.png")
stra = pygame.image.load("newstr.png")
stra2 = pygame.image.load("simu/on.png")
ca = pygame.image.load("simu/car.png")

width, height = 1000, 580
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Simulation")

car_positions = []
car_count = 0


def swap_images():
    global stra, stra2, car_count
    while True:
        if car_count >= 1:
            stra = pygame.image.load("simu/on.png")
            # stra2 = pygame.image.load("simu/on.png")
        elif car_count <= 0:
            # stra = pygame.image.load("simu/on.png")
            stra2 = pygame.image.load("simu/newstr.png")
        time.sleep(0.1)


t = threading.Thread(target=swap_images)
t.daemon = True
t.start()

run = True
clock = pygame.time.Clock()

while run:
    screen.blit(road, (0, 70))
    screen.blit(road, (200, 70))
    screen.blit(road, (400, 70))
    screen.blit(road, (600, 70))
    screen.blit(grass, (0, 0))
    screen.blit(grass, (150, 0))
    screen.blit(grass, (300, 0))
    screen.blit(grass, (400, 0))
    screen.blit(grass, (500, 0))
    screen.blit(grass, (600, 0))
    screen.blit(grass, (700, 0))
    screen.blit(grass, (830, 0))
    screen.blit(grass, (830, 0))
    screen.blit(grass, (830, 400))
    screen.blit(grass, (700, 400))
    screen.blit(grass, (600, 400))
    screen.blit(grass, (500, 400))
    screen.blit(grass, (400, 400))
    screen.blit(grass, (300, 400))
    screen.blit(grass, (150, 400))
    screen.blit(grass, (0, 400))

    if random.randint(1, 400) == 1:
        car_positions.append([-100, random.randint(200, 380)])

    for i in range(len(car_positions)):
        car_position = car_positions[i]
        car_position[0] += 2
        screen.blit(car, car_position)

        if car_position[0] > width:
            car_positions.pop(i)
            car_count += 1
            break

    font = pygame.font.Font(None, 36)
    if car_count > 0:
        screen.blit(stra, (0, 80))
        screen.blit(stra, (870, 80))
    else:


       screen.blit(stra2, (0, 80))
       screen.blit(stra2, (870, 80))
    car_count_text = font.render("Real Cars Count: " + str(len(car_positions)), True, (255, 255, 255))
    screen.blit(car_count_text, (10, 10))

    pygame.display.flip()  # update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if user clicked the window
            run = False
