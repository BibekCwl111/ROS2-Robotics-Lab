import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class FakeDistanceSensor(Node):

    def __init__(self):
        super().__init__('fake_distance_sensor')

        self.publisher_ = self.create_publisher(
            Float32,
            'distance',
            10)

        self.timer = self.create_timer(1.0, self.publish_distance)

    def publish_distance(self):

        try:
            distance = float(
                input("Enter distance (cm): "))

            msg = Float32()
            msg.data = distance

            self.publisher_.publish(msg)

            self.get_logger().info(
                f"Manual Distance: {distance:.2f} cm")

        except:
            self.get_logger().warn("Invalid input")

def main(args=None):

    rclpy.init(args=args)

    node = FakeDistanceSensor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
