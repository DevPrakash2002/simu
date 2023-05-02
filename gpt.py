import pygame
import random

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
CAN_COLOR = (255, 0, 0)
LIGHT_COLOR_1 = (255, 255, 0)
LIGHT_COLOR_2 = (0, 255, 0)
LIGHT_RADIUS = 20
CAN_RADIUS = 10
CAN_SPEED = 5

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Street Light Automation Simulation")
clock = pygame.time.Clock()


# Define class for street lights
class StreetLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = LIGHT_COLOR_1
        self.radius = LIGHT_RADIUS

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def switch(self):
        if self.color == LIGHT_COLOR_1:
            self.color = LIGHT_COLOR_2
        else:
            self.color = LIGHT_COLOR_1


# Create street lights
street_lights = []
for i in range(5):
    x = (i + 1) * WINDOW_WIDTH // 6
    y = WINDOW_HEIGHT // 3
    street_light = StreetLight(x, y)
    street_lights.append(street_light)


# Define function to check for collision between can and street lights
def check_collision(can, street_lights):
    can_center = can.center
    for street_light in street_lights:
        distance = ((can_center[0] - street_light.x) ** 2 + (can_center[1] - street_light.y) ** 2) ** 0.5
        if distance <= CAN_RADIUS + street_light.radius:
            street_light.switch()


# Create can
can_x = 0
can_y = WINDOW_HEIGHT // 2
can_speed = CAN_SPEED
can = pygame.Rect(can_x, can_y, CAN_RADIUS * 2, CAN_RADIUS * 2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move can
    can_x += can_speed
    can.x = can_x

    # Check for collision with street lights
    check_collision(can, street_lights)

    # Draw objects
    window.fill(BACKGROUND_COLOR)
    for street_light in street_lights:
        street_light.draw()
    pygame.draw.circle(window, CAN_COLOR, (can_x + CAN_RADIUS, can_y + CAN_RADIUS), CAN_RADIUS)

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()