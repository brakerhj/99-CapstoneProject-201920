"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Tanner Brammeier Haley Braker.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_drivesystem_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="DriveSystem")
    go_straight_seconds = ttk.Button(frame, text="Go Straight for Seconds")
    go_straight_seconds_seconds = ttk.Entry(frame, width=8)
    go_straight_seconds_seconds_label = ttk.Label(frame, text="Seconds")
    go_straight_seconds_speed = ttk.Entry(frame, width=8)
    go_straight_seconds_speed_label = ttk.Label(frame, text="Speed")
    go_straight_inches = ttk.Button(frame, text="Go Straight for Inches(time)")
    go_straight_inches_speed = ttk.Entry(frame, width=8)
    go_straight_inches_speed_label = ttk.Label(frame, text='Speed')
    go_straight_inches_inches = ttk.Entry(frame, width=8)
    go_straight_inches_inches_label = ttk.Label(frame, text='Inches')
    go_straight_inches_encoder = ttk.Button(frame, text="Go Straight for Inches(encoder)")
    go_straight_until_inches = ttk.Button(frame, text='Go Straight Until Distance Met')
    go_straight_until_inches_inches = ttk.Entry(frame, width=8)
    go_straight_until_inches_inches_label = ttk.Label(frame, text='Inches')
    go_straight_until_inches_speed = ttk.Entry(frame, width=8)
    go_straight_until_inches_speed_label = ttk.Label(frame, text='Speed')
    go_straight_until_inches_delta = ttk.Entry(frame, width=8)
    go_straight_until_inches_delta_label = ttk.Label(frame, text='Delta')
    go_back_until_inches = ttk.Button(frame, text='Go Back Until Distance Met')
    go_until_delta = ttk.Button(frame, text='Go Until Delta Met')
    go_straight_until_intensity_is_less_than = ttk.Button(frame, text='Go Straight Until Intensity Less')
    go_straight_until_intensity_is_less_than_intensity_label = ttk.Label(frame, text='Intensity')
    go_straight_until_intensity_is_less_than_intensity = ttk.Entry(frame, width=8)
    go_straight_until_intensity_is_less_than_speed_label = ttk.Label(frame, text='Speed')
    go_straight_until_intensity_is_less_than_speed = ttk.Entry(frame, width=8)
    go_straight_until_intensity_is_greater_than = ttk.Button(frame, text='Go Straight Until Intesity Greater')
    go_straight_until_color_is = ttk.Button(frame, text='Go Straight Until Color Is')
    go_straight_until_color_is_color_label = ttk.Label(frame, text='Color')
    go_straight_until_color_is_color = ttk.Entry(frame, width=8)
    go_straight_until_color_is_not = ttk.Button(frame, text='Go Straight Until Color is Not')
    tone_increase_by_distance = ttk.Button(frame, text='Frequency getting louder until')
    tone_increase_by_distance_frequency_label = ttk.Label(frame, text='Frequency')
    tone_increase_by_distance_frequency = ttk.Entry(frame, width=8)
    tone_increase_by_distance_rate_label = ttk.Label(frame, text='Rate(10-50)')
    tone_increase_by_distance_rate = ttk.Entry(frame, width=8)
    beep_while_moving_button = ttk.Button(frame, text="Beep While Moving")
    beep_while_moving_initial = ttk.Label(frame, text="Initial")
    beep_while_moving_entry_initial = ttk.Entry(frame, width=8)
    beep_while_moving_rate = ttk.Label(frame, text="Rate")
    beep_while_moving_entry_rate = ttk.Entry(frame, width=8)
    spin_until_object_button = ttk.Button(frame, text="Spin Clockwise Until Object")
    spin_until_object_clockwise = ttk.Label(frame, text="Clockwise: Speed")
    spin_until_object_clockwise_speed = ttk.Entry(frame, width=8)
    spin_until_object_counter = ttk.Label(frame, text="Counterclockwise: Speed")
    spin_until_object_counter_speed = ttk.Entry(frame, width=8)
    spin_cc_until_object_button = ttk.Button(frame, text="Spin Counterclockwise Until Object")





    frame_label.grid(row=0, column=1)
    go_straight_seconds.grid(row=1, column=0)
    go_straight_seconds_seconds.grid(row=3, column=0)
    go_straight_seconds_speed.grid(row=5, column=0)
    go_straight_seconds_seconds_label.grid(row=4, column=0)
    go_straight_seconds_speed_label.grid(row=2, column=0)
    go_straight_inches.grid(row=1, column=2)
    go_straight_inches_speed.grid(row=3, column=2)
    go_straight_inches_speed_label.grid(row=2, column=2)
    go_straight_inches_inches.grid(row=5, column=2)
    go_straight_inches_inches_label.grid(row=4, column=2)
    go_straight_inches_encoder.grid(row=3, column=1)
    go_straight_until_inches.grid(row=6, column=0)
    go_back_until_inches.grid(row=6, column=1)
    go_until_delta.grid(row=6, column=2)
    go_straight_until_inches_inches_label.grid(row=7, column=0)
    go_straight_until_inches_speed_label.grid(row=7, column=1)
    go_straight_until_inches_delta_label.grid(row=7, column=2)
    go_straight_until_inches_inches.grid(row=8, column=0)
    go_straight_until_inches_speed.grid(row=8, column=1)
    go_straight_until_inches_delta.grid(row=8, column=2)
    go_straight_until_intensity_is_less_than.grid(row=9, column=0)
    go_straight_until_intensity_is_less_than_intensity_label.grid(row=10, column=0)
    go_straight_until_intensity_is_less_than_intensity.grid(row=11, column=0)
    go_straight_until_intensity_is_less_than_speed_label.grid(row=10, column=1)
    go_straight_until_intensity_is_less_than_speed.grid(row=11, column=1)
    go_straight_until_intensity_is_greater_than.grid(row=9, column=1)
    go_straight_until_color_is.grid(row=9, column=2)
    go_straight_until_color_is_color_label.grid(row=10, column=2)
    go_straight_until_color_is_color.grid(row=11, column=2)
    go_straight_until_color_is_not.grid(row=9, column=3)
    tone_increase_by_distance.grid(row=12, column=0)
    tone_increase_by_distance_frequency_label.grid(row=13, column=0)
    tone_increase_by_distance_frequency.grid(row=14, column=0)
    tone_increase_by_distance_rate_label.grid(row=13, column=1)
    tone_increase_by_distance_rate.grid(row=14, column=1)
    beep_while_moving_button.grid(row=12, column=2)
    beep_while_moving_initial.grid(row=13, column=2)
    beep_while_moving_entry_initial.grid(row=14, column=2)
    beep_while_moving_rate.grid(row=13, column=3)
    beep_while_moving_entry_rate.grid(row=14, column=3)
    spin_until_object_button.grid(row=15, column=0)
    spin_until_object_clockwise.grid(row=16, column=0)
    spin_until_object_clockwise_speed.grid(row=17, column=1)
    spin_until_object_counter.grid(row=16, column=1)
    spin_until_object_counter_speed.grid(row=17, column=0)
    spin_cc_until_object_button.grid(row=15, column=1)

    go_straight_seconds["command"] = lambda: handle_go_straight_seconds(go_straight_seconds_seconds, go_straight_seconds_speed, mqtt_sender)
    go_straight_inches["command"] = lambda: handle_go_straight_inches(go_straight_inches_speed, go_straight_inches_inches, mqtt_sender)
    go_straight_inches_encoder["command"] = lambda: handle_go_straight_inches_encoder(mqtt_sender)
    go_straight_until_inches["command"] = lambda: handle_go_straight_until_inches(go_straight_until_inches_inches, go_straight_until_inches_speed, mqtt_sender)
    go_back_until_inches["command"] = lambda: handle_go_back_until_inches(go_straight_until_inches_inches, go_straight_until_inches_speed, mqtt_sender)
    go_until_delta["command"] = lambda: handle_go_straight_until_inches_delta(go_straight_until_inches_inches, go_straight_until_inches_speed, go_straight_until_inches_delta, mqtt_sender)
    go_straight_until_intensity_is_less_than['command'] = lambda: handle_go_straight_until_intensity_is_less_than(go_straight_until_intensity_is_less_than_intensity, go_straight_until_intensity_is_less_than_speed, mqtt_sender)
    go_straight_until_intensity_is_greater_than['command'] = lambda: handle_go_straight_until_intensity_is_greater_than(go_straight_until_intensity_is_less_than_intensity, go_straight_until_intensity_is_less_than_speed, mqtt_sender)
    go_straight_until_color_is['command'] = lambda: handle_go_straight_until_color_is(go_straight_until_color_is_color, go_straight_until_intensity_is_less_than_speed, mqtt_sender)
    go_straight_until_color_is_not['command'] = lambda: handle_go_straight_until_color_is_not(go_straight_until_color_is_color, go_straight_until_color_is_color, mqtt_sender)
    tone_increase_by_distance['command'] = lambda: handle_tone_increase_by_distance(tone_increase_by_distance_frequency, tone_increase_by_distance_rate, mqtt_sender)
    beep_while_moving_button['command'] = lambda: handle_beep_while_moving_button(beep_while_moving_entry_initial, beep_while_moving_entry_rate, mqtt_sender)
    spin_until_object_button['command'] = lambda: handle_spin_until_object_button(spin_until_object_clockwise_speed, mqtt_sender)
    spin_cc_until_object_button['command'] = lambda: handle_spin_cc_until_object_button(spin_until_object_counter_speed, mqtt_sender)

    return frame


def get_sound_system_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sound System")
    beep_function = ttk.Button(frame, text="Number of Beeps or Seconds")
    beep_beep_function = ttk.Entry(frame, width=8)
    tone_function = ttk.Button(frame, text="Frequency (range)")
    tone_tone_function = ttk.Entry(frame, width=8)
    phrase_function = ttk.Button(frame, text="What would you like to say?")
    phrase_phrase_function = ttk.Entry(frame, width=20)

    frame_label.grid(row=0, column=3)
    beep_function.grid(row=1, column=0)
    beep_beep_function.grid(row=2, column=0)
    tone_function.grid(row=1, column=3)
    tone_tone_function.grid(row=2, column=3)
    phrase_function.grid(row=1, column=4)
    phrase_phrase_function.grid(row=2, column=4)

    beep_function["command"] = lambda: handle_beep_for_beeps(beep_beep_function, mqtt_sender)
    tone_function["command"] = lambda: handle_tone_for_seconds(beep_beep_function, tone_tone_function, mqtt_sender)
    phrase_function["command"] = lambda: handle_say_something(phrase_phrase_function, mqtt_sender)

    # need to include mqtt_sender when functions are available

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('forward', left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('forward', [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backwards', -int(left_entry_box.get()), -int(right_entry_box.get()))
    mqtt_sender.send_message('backwards', [-int(left_entry_box.get()), -int(right_entry_box.get())])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('turn left', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('turn_left', [int(left_entry_box.get())-int(left_entry_box.get()), right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('turn right', left_entry_box.get(), '0')
    mqtt_sender.send_message('turn_right', [left_entry_box.get(), int(right_entry_box.get())-int(right_entry_box.get())])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise arm')
    mqtt_sender.send_message('raise_arm')

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrating arm')
    mqtt_sender.send_message('calibrate_arm')

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move arm to position', arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position', [int(arm_position_entry.get())])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message("quit")


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()

def handle_go_straight_seconds(go_straight_seconds_seconds, go_straight_seconds_speed, mqtt_sender):
    "sets up the handle."
    print('going straight for', int(go_straight_seconds_seconds.get()))
    mqtt_sender.send_message('go_straight_for_seconds', [go_straight_seconds_seconds.get(), go_straight_seconds_speed.get()])


def handle_go_straight_inches(go_straight_inches_speed, go_straight_inches_inches, mqtt_sender):
    "sets up the handle."
    print('going straight for inches')
    mqtt_sender.send_message('go_straight_for_inches', [go_straight_inches_speed.get(), go_straight_inches_inches.get()])


def handle_go_straight_inches_encoder(mqtt_sender):
    "sets up the handle."


def handle_beep_for_beeps(number, mqtt_sender):
    print('beeping')
    mqtt_sender.send_message('beep_for_beeps', [number.get()])


def handle_tone_for_seconds(seconds, tone, mqtt_sender):
    print('making a tone')
    mqtt_sender.send_message("tone_for_seconds", [seconds.get(), tone.get()])


def handle_say_something(phrase, mqtt_sender):
    print('talking')
    mqtt_sender.send_message('say_something', [phrase.get()])


def handle_go_straight_until_inches(inches, speed, mqtt_sender):
    print('going until distance met')
    mqtt_sender.send_message('go_straight_until_inches', [inches.get(), speed.get()])


def handle_go_back_until_inches(inches, speed, mqtt_sender):
    print('going back until distance met')
    mqtt_sender.send_message('go_back_until_inches', [inches.get(), speed.get()])


def handle_go_straight_until_inches_delta(inches, speed, delta, mqtt_sender):
    print('going until delta meet')
    mqtt_sender.send_message('go_straight_until_inches_delta', [inches.get(), speed.get(), delta.get()])


def handle_go_straight_until_intensity_is_less_than(intensity, speed, mqtt_sender):
    print('going until intensity is less than')
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [intensity.get(), speed.get()])


def handle_go_straight_until_intensity_is_greater_than(intensity, speed, mqtt_sender):
    print('going until intensity is greater than')
    mqtt_sender.send_message('go_straight_until_intensity_is_greater_than', [intensity.get(), speed.get()])


def handle_go_straight_until_color_is(color, speed, mqtt_sender):
    print('going until color is')
    mqtt_sender.send_message('go_straight_until_color_is', [color.get(), speed.get()])


def handle_go_straight_until_color_is_not(color, speed, mqtt_sender):
    print('going until color is not')
    mqtt_sender.send_message('go_straight_until_color_is_not', [color.get(), speed.get()])


def handle_tone_increase_by_distance(frequency, rate, mqtt_sender):
    print('increasing frequency as getting closer')
    mqtt_sender.send_message('tone_as_gets_close', [frequency.get(), rate.get()])


def handle_beep_while_moving_button(intial, rate, mqtt_sender):
    print('beeping faster while getting closer')
    mqtt_sender.send_message('beep_while_moving', [intial.get(), rate.get()])


def handle_spin_until_object_button(right_wheel_speed, mqtt_sender):
    left_wheel_speed = 0
    print('spinning clockwise until object detected')
    mqtt_sender.send_message('spin_until_object', [left_wheel_speed, right_wheel_speed.get()])


def handle_spin_cc_until_object_button(left_wheel_speed, mqtt_sender):
    right_wheel_speed = 0
    print('spinning counterclockwise until object detected')
    mqtt_sender.send_message('spin until_object', [left_wheel_speed.get(), right_wheel_speed])
