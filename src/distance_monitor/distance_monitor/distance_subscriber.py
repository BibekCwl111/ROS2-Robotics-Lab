import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceSubscriber(Node):

    def __init__(self):
        super().__init__('distance_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.callback,
            10)

    def callback(self, msg):
        distance = msg.data

        if distance < 20:
            self.get_logger().warn(f"⚠️ VERY CLOSE: {distance} cm")
        elif distance < 50:
            self.get_logger().info(f"⚠️ Nearby: {distance} cm")
        else:
            self.get_logger().info(f"Safe: {distance} cm")

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
