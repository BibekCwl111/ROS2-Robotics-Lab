import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class RadarPublisher(Node):

    def __init__(self):

        super().__init__('radar_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'radar_data',
            10)

        self.timer = self.create_timer(
            0.1,
            self.publish_data)

        self.angle = 0
        self.direction = 1

    def publish_data(self):

        distance = random.randint(5, 100)

        data = f"{self.angle},{distance}"

        msg = String()
        msg.data = data

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Angle: {self.angle} Distance: {distance}")

        self.angle += self.direction * 5

        if self.angle >= 180:
            self.direction = -1

        elif self.angle <= 0:
            self.direction = 1

def main(args=None):

    rclpy.init(args=args)

    node = RadarPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
