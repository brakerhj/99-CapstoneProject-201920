"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Haley Braker.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # real_thing()
    # run_test_arm()
    # run_test_lower_arm()
    # run_test_calibrate_arm()
    # run_test_get_position()
    # run_go_seconds()
    # run_go_inches_speed()
    # run_go_forward_until_distance_is_less_than()
    # run_go_straight_until_intensity_less_than()
    # run_go_straight_until_intensity_greater_than()
    # run_go_straight_until_color_is()
    run_go_straight_until_color_is_not()


def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break


def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()


def run_test_lower_arm():
    # print("running test lower arm")
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()


def run_test_calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()


def run_test_get_position():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(4000)
    print('2')
    time.sleep(2)
    robot.arm_and_claw.move_arm_to_position(700)


def run_go_seconds():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(5, 100)


def run_go_inches_speed():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(8, 70)


def run_go_forward_until_distance_is_less_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(5, 50)


def run_go_straight_until_intensity_less_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(3, 20)


def run_go_straight_until_intensity_greater_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_greater_than(7, 30)


def run_go_straight_until_color_is():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is('Black', 25)


def run_go_straight_until_color_is_not():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is_not('Blue', 33)





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()