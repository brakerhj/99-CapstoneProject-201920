import tkinter
from tkinter import ttk


def shark_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=30, borderwidth=5, relief='ridge')
    frame.grid()
    style = ttk.Style()
    style.configure("Shark.Label", foreground="blue", font=('Times New Roman', 30))
    style2 = ttk.Style()
    style2.configure("my.TButton", foreground="red", background="red", font=('Times New Roman', 15))
    style3 = ttk.Style()
    style3.configure('my.TLabel', foreground="red", font=('Times New Roman', 24))

    password = "FishAreFriends"

    # code for password taken from stack

    def trylogin():
        print("Trying to login...")
        if password_guess.get() == password:
            print("Complete sucsessfull!")
            # messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
        else:
            print("Error: (Incorrect value entered)")
            # messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")

    frame_label = ttk.Label(frame, text='Shark AI', style="Shark.Label")
    prey_label = ttk.Label(frame, text='Hunt for Prey', style="my.TLabel")
    prey_stalk = ttk.Button(frame, text="Stalk", style="my.TButton")
    prey_seafloor = ttk.Button(frame, text="Seafloor", style="my.TButton")
    prey_intimidate = ttk.Button(frame, text="Intimidate", style="my.TButton")
    password_text = ttk.Label(frame, text="Secret Password:")
    password_guess = ttk.Entry(frame, show="*")
    attempt_login = ttk.Button(frame, text="Enter", command=trylogin())

    spacing_label = ttk.Label(frame, text='')
    spacing_label2 = ttk.Label(frame, text='')
    quit_robot_button = ttk.Button(frame, text="Stop just the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    frame_label.grid(row=0, column=1)
    prey_label.grid(row=1, column=1)
    prey_seafloor.grid(row=2, column=0)
    prey_stalk.grid(row=2, column=2)
    prey_intimidate.grid(row=2, column=1)
    spacing_label2.grid(row=2, column=1)
    spacing_label.grid(row=4, column=1)
    password_text.grid(row=5, column=1)
    password_guess.grid(row=6, column=1)
    attempt_login.grid(row=6, column=2)
    quit_robot_button.grid(row=0, column=0)
    exit_button.grid(row=0, column=2)

    quit_robot_button["command"] = lambda: handle_quit_robot(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)
    prey_stalk["command"] = lambda: handle_prey_stalk(mqtt_sender)
    prey_seafloor["command"] = lambda: handle_prey_seafloor(mqtt_sender)
    prey_intimidate["command"] = lambda:handle_intimidate(mqtt_sender)

    return frame


def handle_prey_stalk(mqtt_sender):
    print("stalk")
    mqtt_sender.send_message('prey_stalk')


def handle_prey_seafloor(mqtt_sender):
    print("seafloor")
    mqtt_sender.send_message('prey_seafloor')


def handle_quit_robot(mqtt_sender):
    print("quit")
    mqtt_sender.send_message('quit_robot')


def handle_exit(mqtt_sender):
    print("exit")
    mqtt_sender.send_message('exit')


def handle_intimidate(mqtt_sender):
    print("intimidate")
    mqtt_sender.send_message('prey_intimidate')



