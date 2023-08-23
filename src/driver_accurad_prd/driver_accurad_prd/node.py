import rclpy
from rclpy.node import Node

from accurad_interfaces.msg import RadMeasurement

import driver_accurad_prd.accurad_usb as accurad
import serial


class AccuRadPRD(Node):
    ''' Driver for an AccuRad PRD. '''

    def __init__(self):
        ''' Initialize the node and create a serial connection. '''
        super().__init__('accurad_prd')

        # Declare ROS parameters.
        self.declare_parameter('port', 'COM8')
        self.declare_parameter('baudrate', 115200)
        self.declare_parameter('timeout', 1.0)

        # Get ROS parameter values.
        port = self.get_parameter('port').get_parameter_value().string_value
        baudrate = self.get_parameter('baudrate').get_parameter_value().integer_value
        timeout = self.get_parameter('timeout').get_parameter_value().double_value

        # Attempt to open the serial connection.
        try:
            self.serial_connection = serial.Serial(
                port=port, baudrate=baudrate, timeout=timeout
            )
        except serial.SerialException as e:
            print(f"Error opening serial connection on {port}: {e}")
            raise e

        # Create ROS publishers.
        self.pubData = self.create_publisher(RadMeasurement, 'rad_measurement', 10)

        # Create a ROS timer to poll the device.
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def onTimerPollDevice(self):
        ''' Called by the timer to poll the device.
            Reads from the device and then publishes data. '''
        
        # Read from the device.
        data = accurad.main(self.serial_connection)
        if data is None:
            self.get_logger().error(f"Error reading from device {self.serial_connection.port}")
            return
        mrem_per_hour, counts_per_second, mrem, duration = data

        # Package the data in a RadMeasurement message.
        msg = RadMeasurement()
        msg.mrem_per_hour = mrem_per_hour
        msg.counts_per_second = counts_per_second
        msg.mrem = mrem
        msg.duration = duration

        # Publish the data.
        self.pubData.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = AccuRadPRD()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()