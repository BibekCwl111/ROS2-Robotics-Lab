import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class DistancePublisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')

        self.publisher_ = self.create_publisher(Float32, 'distance', 10)

        self.serial_port = serial.Serial('/dev/ttyACM0', 9600)

        self.timer = self.create_timer(0.5, self.publish_distance)

    def publish_distance(self):

        if self.serial_port.in_waiting > 0:

            line = self.serial_port.readline().decode().strip()

            try:
                distance = float(line)

                if distance <0 or distance >400:
                   return

                msg = Float32()
                msg.data = distance

                self.publisher_.publish(msg)

                self.get_logger().info(f"Real Distance: {distance:.2f} cm")

            except:
                pass

def main(args=None):
    rclpy.init(args=args)

    node = DistancePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
