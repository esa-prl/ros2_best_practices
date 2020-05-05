
import rclpy
import unittest
import launch_testing

from launch_ros.actions import Node
from launch import LaunchDescription

import std_msgs.msg
import uuid

# This is necessary to get unbuffered output from the process under test
proc_env = os.environ.copy()
proc_env['PYTHONUNBUFFERED'] = '1'

namespace_ = 'example'

# The launch_test mark tells the framework to start the described nodes
@pytest.mark.launch_test
def generate_test_description():
    example_node = Node(
        package='example_package',
        node_namespace=namespace_,
        node_executable='example_node',
        node_name='example_node',
        env=proc_env,
    )

    return(
        LaunchDescription([
            example_node,
            # This tells the framework to start testing after processes are started
            launch_testing.actions.ReadyToTest(),
        ]),
        {
            # Here the created processes are defined, mostly one per node
            'example_proc': example_node,
        }
    )


class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize ROS context for all tests in this class
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        # Shutdown the ROS context for all tests in this class
        rclpy.shutdown()

    def setUp(self):
        # Create ROS node before a test method is called
        # This node can interact with the example_node that should be tested
        self.node = rclpy.create_node('test_input_node', namespace=namespace_)

    def tearDown(self):
        # Destroy the ROS node after the test method is done
        self.node.destroy_node()

    def test_subscriber(self, example_proc, proc_output, proc_info):
        '''
        This test verifies the subscriber of example_node to the test_msg topic.
        The example node need to print out the data of the message, for the test to 
        be positive.
        '''

        # Create a publisher for the topic to be tested
        pub = self.node.create_publisher(
            std_msgs.msg.String,
            'test_msg',
            10
        )

        try:
            # Publish a message with a unique identifier
            # and check that the listener gets it and prints the verification
            msg = std_msgs.msg.String()
            msg.data = str(uuid.uuid4())

            # Publish the message a few times till the example node receives it
            for _ in range(10):
                pub.publish(msg)
                success = proc_output.waitFor(
                    expected_output=msg.data,
                    process=example_proc,
                    timeout=1.0,
                )
                if success:
                    break
            assert success, 'Waiting for output timed out'

        finally:
            self.node.destroy_publisher()


@launch_testing.post_shutdown_test()
class TestProcessOutput(unittest.TestCase):

    def test_exit_code(self):
        # Check that all processes in the launch (in this case, there's just one) exit
        # with code 0
        launch_testing.asserts.assertExitCodes(self.proc_info)
