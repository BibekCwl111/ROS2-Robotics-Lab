import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
import random

class RobotDecision(Node):

    def __init__(self):
        super().__init__('robot_decision')

        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.distance_callback,
            10)

        self.publisher_ = self.create_publisher(
            String,
            'robot_action',
            10)

        self.close_counter = 0

    def distance_callback(self, msg):

        distance = msg.data

        action = String()

        if distance > 40:
            action.data = "MOVE_FORWARD"
            self.close_counter = 0

        elif distance > 20:
            action.data = "SLOW_FORWARD"
            self.close_counter = 0

        elif distance > 10:
            action.data = "STOP"
            self.close_counter += 1

        else:
            self.close_counter += 1

            if self.close_counter >= 3:
                action.data = "MOVE_BACKWARD"
                self.close_counter = 0
            else:
                action.data = random.choice(
                    ["TURN_LEFT", "TURN_RIGHT"])

        self.publisher_.publish(action)

        self.get_logger().info(
            f"Distance: {distance:.2f} cm -> Action: {action.data}")

def main(args=None):

    rclpy.init(args=args)

    node = RobotDecision()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
