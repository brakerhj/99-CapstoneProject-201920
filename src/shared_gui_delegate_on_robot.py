"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tanner Brammeier Haley Braker.
  Winter term, 2018-2019.
"""

class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot : rosebot.RoseBot"""
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        self.robot.drive_system.stop()

    def backwards(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def turn_left(self, right_wheel_speed, left_wheel_speed):
        self.robot.drive_system.go(int(right_wheel_speed), int(left_wheel_speed))

    def turn_right(self, right_wheel_speed, left_wheel_speed):
        self.robot.drive_system.go(int(right_wheel_speed), int(left_wheel_speed))

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def go_straight_for_seconds(self, speed_entry, seconds_entry):
        self.robot.drive_system.go_straight_for_seconds(int(seconds_entry), int(speed_entry))

    def go_straight_for_inches(self, speed_entry, inches_entry):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches_entry), int(speed_entry))
