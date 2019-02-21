import tkinter
from tkinter import ttk, messagebox


def shark_frame(window, mqtt_sender):
    frame = tkinter.Frame(window, borderwidth=7, relief='ridge', background='light sea green')
    frame.grid()
    style = ttk.Style()
    style.configure("Shark.Label", foreground="blue", font=('Times New Roman', 30))
    style2 = ttk.Style()
    style2.configure("my.TButton", foreground="red", background="red", font=('Times New Roman', 15))

    frame_label = tkinter.Label(frame, text='SharkBot', bg="light sea green", font=('Times New Roman', 24),
                                foreground="blue")
    prey_label = tkinter.Label(frame, text='Hunt for Prey', font=('Times New Roman', 15), bg="light sea green", fg="red")
    prey_stalk = ttk.Button(frame, text="Stalk", style="my.TButton")
    prey_seafloor = ttk.Button(frame, text="Seafloor", style="my.TButton")
    prey_intimidate = ttk.Button(frame, text="Intimidate", style="my.TButton")
    password_text = tkinter.Label(frame, background='lightblue', text="Secret Password:")
    password_guess = ttk.Entry(frame, show="*")
    attempt_login = tkinter.Button(frame, text="Enter", bg="light blue")
    speed_label = tkinter.Label(frame, text='Speed:', font=('Times New Roman', 10), bg="light blue")
    speed_entry = ttk.Entry(frame)
    quit_robot_button = tkinter.Button(frame, text="Stop just the robot's program", bg="light blue")
    exit_button = tkinter.Button(frame, text="Stop this and the robot's program", bg="light blue")

    frame_label.grid(row=0, column=1)
    prey_label.grid(row=1, column=1)
    prey_seafloor.grid(row=2, column=0)
    prey_stalk.grid(row=2, column=2)
    prey_intimidate.grid(row=2, column=1)
    speed_label.grid(row=4, column=1)
    speed_entry.grid(row=5, column=1)
    password_text.grid(row=6, column=1)
    password_guess.grid(row=7, column=1)
    attempt_login.grid(row=7, column=2)
    quit_robot_button.grid(row=0, column=0)
    exit_button.grid(row=0, column=2)

    quit_robot_button["command"] = lambda: handle_quit_robot(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)
    prey_stalk["command"] = lambda: handle_prey_stalk(mqtt_sender, speed_entry)
    prey_seafloor["command"] = lambda: handle_prey_seafloor(mqtt_sender, speed_entry)
    prey_intimidate["command"] = lambda: handle_intimidate(mqtt_sender, speed_entry)
    attempt_login["command"] = lambda: trylogin(mqtt_sender, password_guess)

    return frame


def handle_prey_stalk(mqtt_sender, speed_entry):
    print("stalk")
    mqtt_sender.send_message('prey_stalk', [int(speed_entry.get())])


def handle_prey_seafloor(mqtt_sender, speed_entry):
    print("seafloor")
    # color = "blue"
    # seconds = 10
    mqtt_sender.send_message('prey_seafloor', [int(speed_entry.get())])


def handle_quit_robot(mqtt_sender):
    print("quit")
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    print("exit")
    mqtt_sender.send_message('stop')


def handle_intimidate(mqtt_sender, speed_entry):
    print("intimidate")
    mqtt_sender.send_message('prey_intimidate', [int(speed_entry.get())])


password = "FishAreFriends"

# code for password taken from stack


def trylogin(mqtt_sender, password_guess):
    print("Trying to login...")
    if password_guess.get() == password:
        print("Complete successful!")
        handle_password_method(mqtt_sender)
        # messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
    else:
        print("Error: (Incorrect value entered)")
        # messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")


def handle_password_method(mqtt_sender):
    print("password!")
    mqtt_sender.send_message('password_method')

