import random
import pygame
import time
import math

pygame.init()


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


road = pygame.image.load("road.png")
grass = scale_image(pygame.image.load("grass.png"), 0.45)
bike = pygame.image.load("bike.png")
car = pygame.image.load("car.png")
stra = pygame.image.load("newstr.png")
ca = pygame.image.load("car.png")

width, height = 1000, 580
screen = pygame.display.set_mode((width, height))  # create display surface
pygame.display.set_caption("Traffic Simulation")

car_position = [0, 300]  # starting position of the car

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
    screen.blit(stra, (20, 80))
    screen.blit(stra, (270, 80))
    screen.blit(stra, (520, 80))
    screen.blit(stra, (770, 80))
    screen.blit(car, car_position)

    pygame.display.flip()  # update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if user clicked the window's X button
            run = False  # exit the loop

    car_position[0] += 2
    clock.tick(60)

pygame.quit()
