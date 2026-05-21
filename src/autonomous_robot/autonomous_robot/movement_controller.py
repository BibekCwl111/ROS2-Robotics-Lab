import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MovementController(Node):

    def __init__(self):
        super().__init__('movement_controller')

        self.subscription = self.create_subscription(
            String,
            'robot_action',
            self.action_callback,
            10)

    def action_callback(self, msg):

        action = msg.data

        if action == "MOVE_FORWARD":
            self.get_logger().info("🚗 Robot moving forward")

        elif action == "SLOW_FORWARD":
            self.get_logger().info("🐢 Robot moving slowly")

        elif action == "STOP":
            self.get_logger().info("🛑 Robot stopped")

        elif action == "TURN_LEFT":
            self.get_logger().info("↩️ Robot turning left")

        elif action == "TURN_RIGHT":
            self.get_logger().info("↪️ Robot turning right")

        elif action == "MOVE_BACKWARD":
            self.get_logger().info("⬅️ Robot moving backward")

def main(args=None):

    rclpy.init(args=args)

    node = MovementController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
