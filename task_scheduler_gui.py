import tkinter as tk
from tkinter import filedialog
import datetime
import os
import threading
import sys
import main  # <-- import main.py as a module 

# ----------------------
# Global variable for process tracking
# ----------------------
current_thread = None

# ----------------------
# Functions
# ----------------------
def launch_program():
    global current_thread

    file_path = entry_file.get().strip()
    start_date = entry_date.get().strip()
    start_time = entry_time.get().strip()
    interval = entry_interval.get().strip()
    repetition = entry_repeat.get().strip()

    status_label.config(text="", fg="black")  # Clear previous status

    # Basic checks
    if not os.path.exists(file_path):
        status_label.config(text="Error: The specified file path does not exist.", fg="red")
        return

    # Default date/time if empty
    if not start_date:
        start_date = datetime.datetime.now().strftime("%d%m%Y")
    if not start_time:
        start_time = datetime.datetime.now().strftime("%H%M%S")

    # Interval check
    if len(interval) != 6 or not interval.isdigit():
        status_label.config(text="Error: Interval must be in HHMMSS format.", fg="red")
        return

    # Repetition check
    if not repetition.isdigit() or int(repetition) <= 0:
        status_label.config(text="Error: Repetition must be a positive integer greater than 0.", fg="red")
        return

    # Thread to run main.run_task in background
    def run_task_thread():
        try:
            main.run_task(file_path, start_date, start_time, interval, repetition)
            status_label.config(text="Program execution completed.", fg="blue")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")

    current_thread = threading.Thread(target=run_task_thread, daemon=True)
    current_thread.start()
    status_label.config(text="Program started in background...", fg="green")


def choose_file():
    file_path = filedialog.askopenfilename(title="Select a file to execute")
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)


def cancel_execution():
    global current_thread
    # In thread, we can't really "kill", so we just display a message
    if current_thread and current_thread.is_alive():
        status_label.config(text="⚠ Cannot forcibly stop a running task. Please close GUI.", fg="orange")
    else:
        status_label.config(text="ℹ No running task.", fg="gray")

# ----------------------
# GUI Setup
# ----------------------
root = tk.Tk()
root.title("Task Scheduler")

# ----------------------
# Icon setup (works with PyInstaller too)
# ----------------------
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

icon_path = os.path.join(base_path, "assets", "task_scheduler_icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# ----------------------
# Window size & center
# ----------------------
window_width = 600
window_height = 420
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = int((screen_width/2) - (window_width/2))
y_coord = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")
root.resizable(False, False)

# ----------------------
# Title
# ----------------------
tk.Label(root, text="Task Scheduler", font=("Arial", 16, "bold")).pack(pady=10)

# ----------------------
# Input fields
# ----------------------
frame = tk.Frame(root)
frame.pack(pady=5)

labels = [
    "File:",
    "Start date (DDMMYYYY):",
    "Start time (HHMMSS):",
    "Interval (HHMMSS):",
    "Repetition:"
]
entries = []

for label_text in labels:
    row = tk.Frame(frame)
    tk.Label(row, text=label_text, width=22, anchor='w').pack(side=tk.LEFT)
    entry = tk.Entry(row, width=45)
    entry.pack(side=tk.RIGHT, padx=10)
    row.pack(pady=5)
    entries.append(entry)

entry_file, entry_date, entry_time, entry_interval, entry_repeat = entries

# File selection button
tk.Button(root, text="📂 Select File", command=choose_file).pack(pady=5)

# Launch and Cancel buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Launch",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=launch_program,
    width=12
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Cancel",
    bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold"),
    command=cancel_execution,
    width=12
).pack(side=tk.RIGHT, padx=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
status_label.pack(pady=10)

# Footer
tk.Label(root, text="Developed by Siaibou CAMARA", font=("Arial", 9), fg="gray").pack(side="bottom", pady=10)

# ----------------------
# Run the GUI
# ----------------------
root.mainloop()
