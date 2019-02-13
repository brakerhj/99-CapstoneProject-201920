"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tanner Brammeier Haley Braker.
  Winter term, 2018-2019.
"""

import time

class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot : rosebot.RoseBot"""
        self.robot = robot
        self.is_time_to_stop = False

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

    def quit(self):
        print('got quit')
        self.is_time_to_stop = True

    # def exit(self):
    #     print('got exit')

    def beep_for_beeps(self, n):
        print('got beep')
        for numbers in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def tone_for_seconds(self, seconds, tone):
        self.robot.sound_system.tone_maker.play_tone(int(tone), int(seconds)).wait()

    def say_something(self, phrase):
        self.robot.sound_system.speech_maker.speak(str(phrase))

    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)