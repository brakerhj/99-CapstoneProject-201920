"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Tanner Brammeier.
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
    tone_as_gets_close(400)

def real_thing():
    robot = rosebot.RoseBot()
    delegate_receives = shared_gui_delegate_on_robot.DelegateReceives(robot)
    mqtt_receivers = com.MqttClient(delegate_receives)
    mqtt_receivers.connect_to_pc()
    while True:
        time.sleep(0.01)
        if delegate_receives.is_time_to_quit:
            break


def tone_as_gets_close(frequency):
    robot = rosebot.RoseBot()
    robot.drive_system.go(30, 30)
    while True:
        ir_sensor = robot.sensor_system.ir_proximity_sensor.get_distance()
        print(ir_sensor)
        toner = robot.sound_system.tone_maker.play_tone(frequency / (ir_sensor/10), 500).wait()
        toner
        if ir_sensor <= 6:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()