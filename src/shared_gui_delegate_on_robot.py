"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tanner Brammeier Haley Braker.
  Winter term, 2018-2019.
"""

import time

from math import log2, pow

class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot : rosebot.RoseBot"""
        self.robot = robot
        self.is_time_to_stop = False

    def forward(self, left_wheel_speed, right_wheel_speed):
        # self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))
        print(self.robot.sensor_system.camera.get_biggest_blob())

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

    def go_straight_until_inches_delta(self, inches, speed, delta):
        self.robot.drive_system.go_until_distance_is_within(delta, inches, speed)

    def go_straight_until_intensity_is_less_than(self, color_value, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(color_value, speed)

    def go_straight_until_intensity_is_greater_than(self, color_value, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(color_value, speed)

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)

    def tone_as_gets_close(self, frequency, rate):
        self.robot.drive_system.go(30, 30)
        while True:
            ir_sensor = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            print(ir_sensor)
            toner = self.robot.sound_system.tone_maker.play_tone(int(frequency) / (int(ir_sensor) / int(rate)), 500).wait()
            toner
            if ir_sensor <= 6:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

    def beep_while_moving(self, initial, rate):
        self.robot.drive_system.go(25, 25)
        first_value = self.robot.sensor_system.ir_proximity_sensor.get_distance()
        while True:
            ir_sensor = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            self.robot.sound_system.beeper.beep().wait()
            print(ir_sensor)
            if ir_sensor < first_value:
                time.sleep((int(initial) / (int(rate) / int(ir_sensor)) / 100))
            if ir_sensor <= 4:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                self.robot.arm_and_claw.move_arm_to_position(0)
                break

    def spin_until_object(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(left_wheel_speed, right_wheel_speed)  # spinning right
        while True:
            b = self.robot.sensor_system.camera.get_biggest_blob().center
            print(b.x)
            if 170 > b.x > 150:
                self.robot.drive_system.stop()
                self.robot.drive_system.go_forward_until_distance_is_less_than(2, 25)
                self.robot.arm_and_claw.raise_arm()
                self.robot.arm_and_claw.move_arm_to_position(0)
                break
            time.sleep(0.01)

    def get_energy_drink(self):
        self.robot.drive_system.go(0, 30)  # spinning left
        while True:
            e = self.robot.sensor_system.camera.get_biggest_blob().center
            print(e.x)
            if 170 > e.x > 150:
                self.robot.drive_system.stop()
                self.robot.drive_system.go_forward_until_distance_is_less_than(2, 25)
                self.robot.arm_and_claw.raise_arm()
                self.robot.drive_system.go(30, 0)
                start = time.time()
                while True:
                    current = time.time()
                    if current - start >= 5:
                        self.robot.drive_system.stop()
                        break
                self.robot.drive_system.go_straight_until_color_is('white', 40)
                self.robot.arm_and_claw.move_arm_to_position(0)
                break
            time.sleep(0.01)

    def get_coke(self):
        self.robot.drive_system.go(0, 30)  # spinning left
        while True:
            c = self.robot.sensor_system.camera.get_biggest_blob().center
            print(c.x)
            if 170 > c.x > 150:
                self.robot.drive_system.stop()
                self.robot.drive_system.go_forward_until_distance_is_less_than(2, 25)
                self.robot.arm_and_claw.raise_arm()
                self.robot.drive_system.go(30, 0)
                start = time.time()
                while True:
                    current = time.time()
                    if current - start >= 5:
                        self.robot.drive_system.stop()
                        break
                self.robot.drive_system.go_straight_until_color_is('white', 40)
                self.robot.arm_and_claw.move_arm_to_position(0)
                break
            time.sleep(0.01)

    def get_mac_n_cheese(self):
        self.robot.drive_system.go(0, 30)  # spinning left
        while True:
            m = self.robot.sensor_system.camera.get_biggest_blob().center
            print(m.x)
            if 170 > m.x > 150:
                self.robot.drive_system.stop()
                self.robot.drive_system.go_forward_until_distance_is_less_than(2, 25)
                self.robot.arm_and_claw.raise_arm()
                self.robot.drive_system.go(30, 0)
                start = time.time()
                while True:
                    current = time.time()
                    if current - start >= 5:
                        self.robot.drive_system.stop()
                        break
                self.robot.drive_system.go_straight_until_color_is('white', 40)
                self.robot.arm_and_claw.move_arm_to_position(0)
                break
            time.sleep(0.01)

    def prey_intimidate(self, speed):
        # plays 'jaws' tone, faster and faster as approaching object, using tone_as_gets_close
        self.robot.drive_system.go(speed, speed)
        NOTE_E = 146.83
        NOTE_F = 155.56
        NO_NOTE = 0
        NOTE_G = 164.81
        NOTE_H = 174.61

        notes = [NOTE_E, NOTE_F, NO_NOTE, NOTE_G, NOTE_H]
        first_value = self.robot.sensor_system.ir_proximity_sensor.get_distance()
        while True:
            duration = 500
            ir_sensor = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            print(ir_sensor)
            self.robot.sound_system.tone_maker.play_tone(notes[0], duration).wait()
            self.robot.sound_system.tone_maker.play_tone(notes[1], duration).wait()
            if ir_sensor < first_value:
                duration = duration * (ir_sensor / 100)
                self.robot.sound_system.tone_maker.play_tone(notes[0], duration).wait()
                self.robot.sound_system.tone_maker.play_tone(notes[1], duration).wait()
            if ir_sensor <= 6:
                self.robot.drive_system.stop()
                break

    def prey_seafloor(self, speed):
        # using color sensor to follow red on the "seafloor" (ground) using go_straight_until_color_is_not
        seconds = 10
        color = "Blue"
        print(self.robot.sensor_system.color_sensor.get_color_as_name())
        self.robot.drive_system.go_straight_for_seconds(3, speed)

        for k in range(seconds):
            print(k)
            print(color, "=", self.robot.sensor_system.color_sensor.get_color_as_name())
            if k % 2:
                print(k, "right wheel going")
                self.robot.drive_system.go(speed, 0)
                time.sleep(3)
                if self.robot.sensor_system.color_sensor.get_color_as_name() == color:
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    print("stopping and lifting arm")
                    self.robot.arm_and_claw.move_arm_to_position(0)
            else:
                print(k, "left wheel going")
                self.robot.drive_system.go(0, speed)
                time.sleep(3)
                if self.robot.sensor_system.color_sensor.get_color_as_name() == color:
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    print("stopping and lifting arm")
                    self.robot.arm_and_claw.move_arm_to_position(0)

    def prey_stalk(self, speed):
        # using camera sensor to follow red objects using spin_until_object
        # also may use the one i found on the website
        self.robot.drive_system.go(speed, speed)
        while True:
            b = self.robot.sensor_system.camera.get_biggest_blob().center
            # print(b.x)
            # if 190 > b.x > 130:
            #     self.robot.drive_system.go_forward_until_distance_is_less_than(4, 10*2)
            if 0 < b.x < 150:
                print("spinning left")
                self.robot.drive_system.go(0, speed)
            if 170 < b.x < 320:
                print("spinning right")
                self.robot.drive_system.go(speed, 0)
            if 151 < b.x < 169:
                print("going forward")
                self.robot.drive_system.go(speed * 2, speed * 2)
                self.robot.drive_system.go_forward_until_distance_is_less_than(4, speed * 2)
                break
            time.sleep(0.01)

        self.robot.arm_and_claw.raise_arm()
        self.robot.arm_and_claw.move_arm_to_position(0)

    def password_method(self):
        # i dont know exactly what i want it to do yet
        # make the robot say "Fish are friends, not food!"
        self.robot.sound_system.speech_maker.speak(str("Fish are friends, not food!"))
        print("password")
