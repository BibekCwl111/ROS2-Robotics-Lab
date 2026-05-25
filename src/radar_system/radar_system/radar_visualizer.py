import pygame
import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

WIDTH = 800
HEIGHT = 600

angle_value = 0
distance_value = 0

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROS2 Radar Visualization")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

center_x = WIDTH // 2
center_y = HEIGHT - 50

class RadarVisualizer(Node):

    def __init__(self):

        super().__init__('radar_visualizer')

        self.subscription = self.create_subscription(
            String,
            'radar_data',
            self.callback,
            10)

    def callback(self, msg):

        global angle_value
        global distance_value

        angle, distance = msg.data.split(',')

        angle_value = int(angle)
        distance_value = int(distance)

        self.get_logger().info(
            f"Angle: {angle_value} Distance: {distance_value}"
        )

def ros_thread():

    rclpy.init()

    node = RadarVisualizer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

threading.Thread(target=ros_thread, daemon=True).start()

running = True

while running:

    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, (center_x, center_y), 250, 1)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 200, 1)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 150, 1)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 100, 1)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 50, 1)

    angle_rad = math.radians(angle_value)

    radar_x = center_x + int(250 * math.cos(math.pi - angle_rad))
    radar_y = center_y - int(250 * math.sin(angle_rad))

    pygame.draw.line(
        screen,
        GREEN,
        (center_x, center_y),
        (radar_x, radar_y),
        2
    )

    obstacle_x = center_x + int(distance_value * 2 * math.cos(math.pi - angle_rad))
    obstacle_y = center_y - int(distance_value * 2 * math.sin(angle_rad))

    pygame.draw.circle(
        screen,
        RED,
        (obstacle_x, obstacle_y),
        5
    )

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
