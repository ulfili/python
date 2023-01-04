"""ROBOT."""


from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    # robot = FollowerBot()
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(5)
    line_cross = False
    while not line_cross:   # while True
        robot.sleep(2)
        if 0 == min(robot.get_line_sensors()):
            line_cross = True
            # print("min = ", min(robot.get_line_sensors()))
    robot.set_wheels_speed(35)
    robot.sleep(1)
    robot.done()
