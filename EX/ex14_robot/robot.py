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


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    zero_list = [0, 0, 0, 0, 0, 0]
    robot._timeout = 5000
    line_cross = False
    finish_point = True
    robot.set_wheels_speed(5)
    while not line_cross:  # while True
        robot.sleep(2)
        if 0 == min(robot.get_line_sensors()):
            line_cross = True
    robot.set_wheels_speed(10)
    while finish_point:
        robot.sleep(0.01)
        if min(robot.get_line_sensors()) > 0:
            finish_point = False
            # print(robot.get_line_sensors())
            # print(robot.get_position())

        if robot.get_third_line_sensor_from_left() == 0 and robot.get_right_line_sensor() != 0:
            robot.set_right_wheel_speed(30)
            robot.set_left_wheel_speed(0)
            if robot.get_second_line_sensor_from_left() == 0 and robot.get_right_line_sensor() != 0:
                robot.set_right_wheel_speed(14)
                robot.set_left_wheel_speed(0)
            robot.sleep(0.01)
            print(robot.get_line_sensors())
            print(robot.get_position())

        elif robot.get_left_line_sensor() != 0 and robot.get_third_line_sensor_from_right() == 0:
            robot.set_right_wheel_speed(-30)
            robot.set_left_wheel_speed(0)
            if robot.get_left_line_sensor() != 0 and robot.get_second_line_sensor_from_right() == 0:
                robot.set_right_wheel_speed(-14)
                robot.set_left_wheel_speed(0)
            robot.sleep(0.01)
            print(robot.get_line_sensors())
            print(robot.get_position())

        else:
            robot.set_wheels_speed(5)
            robot.sleep(0.01)
            print(robot.get_line_sensors())
            print(robot.get_position())
    robot.done()


if __name__ == '__main__':
    #   robot = FollowerBot(start_x=123, start_y=251, starting_orientation=90)
    robot = FollowerBot(track_image="sharp.png", start_x=275, start_y=585, starting_orientation=90)
    follow_the_line(robot)
