import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

class TimestampLoggerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timestamp Logger")

        self.start_time = None
        self.log_file_name = None

        # Prompt for the experiment name before starting
        self.experiment_name = simpledialog.askstring("Input", "Enter the experiment name:")
        if self.experiment_name:
            self.log_file_name = f"{self.experiment_name}.txt"

            self.start_button = tk.Button(master, text="Start", command=self.start_logging)
            self.start_button.pack(pady=10)

            self.log_button = tk.Button(master, text="Log Current Timestamp", command=self.log_current_timestamp)
            self.log_button.pack(pady=10)

            self.stop_button = tk.Button(master, text="Stop", command=self.stop_logging)
            self.stop_button.pack(pady=10)
        else:
            self.master.quit()  # Exit if no name is provided

    def start_logging(self):
        self.start_time = datetime.now()
        with open(self.log_file_name, 'a') as f:
            f.write(f"Experiment '{self.experiment_name}' started at: {self.start_time}\n")
        print(f"Logging started. First timestamp logged: {self.start_time}")

    def log_current_timestamp(self):
        if self.start_time is not None:
            current_time = datetime.now()
            with open(self.log_file_name, 'a') as f:
                f.write(f"Logged timestamp: {current_time}\n")
            print(f"Current timestamp logged: {current_time}")
        else:
            print("Please start the logging first.")

    def stop_logging(self):
        if self.start_time is not None:
            end_time = datetime.now()
            with open(self.log_file_name, 'a') as f:
                f.write(f"Experiment '{self.experiment_name}' stopped at: {end_time}\n")
            print(f"Logging stopped. Last timestamp logged: {end_time}")
            self.master.quit()
        else:
            print("No logging session to stop.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimestampLoggerApp(root)
    root.mainloop()
