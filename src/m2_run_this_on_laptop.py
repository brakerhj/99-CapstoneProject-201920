"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Tanner Brammeier.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import m2_extra_stuff


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Capstone Project')



    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    # teleop_frame, arm_frame, control_frame, drivesystem_frame, sound_system_frame = get_shared_frames(main_frame, mqtt_sender)
    snackbot_frame = get_shared_frames(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, sound_system_frame, drivesystem_frame)
    grid_frames(snackbot_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    # teleop = m2_extra_stuff.get_teleoperation_frame(main_frame, mqtt_sender)
    # arm = m2_extra_stuff.get_arm_frame(main_frame, mqtt_sender)
    # control = m2_extra_stuff.get_control_frame(main_frame, mqtt_sender)
    # drivesystem = m2_extra_stuff.get_drivesystem_frame(main_frame, mqtt_sender)
    # sound_system = m2_extra_stuff.get_sound_system_frame(main_frame, mqtt_sender)
    # return teleop, arm, control, drivesystem, sound_system

    snackbot = m2_extra_stuff.snackbot_frame(main_frame, mqtt_sender)
    return snackbot


def grid_frames(snackbot_frame):
    # teleop_frame.grid(row=0, column=0)
    # arm_frame.grid(row=1, column=0)
    # control_frame.grid(row=2, column=0)
    # drivesystem_frame.grid(row=0, column=1)
    # sound_system_frame.grid(row=1, column=1)
    snackbot_frame.grid(row=0, column=0)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()