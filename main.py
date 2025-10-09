import datetime
import time
import os
import sys
import subprocess

# --- Main function to call from the GUI ---
def run_task(file_path, start_date, start_time, interval, repetition):
    # --- Validate inputs ---
    error_detected = False
    error_messages = {
        "path_not_found": "File path does not exist",
        "invalid_date": "The start date must contain 8 digits (format: DDMMYYYY)",
        "invalid_time": "The start time must contain 6 digits (format: HHMMSS)",
        "invalid_interval": "The interval must contain 6 digits (format: HHMMSS)",
        "invalid_repetition": "Repetition must contain digits only"
    }

    file_path = file_path.strip('"')
    if not os.path.exists(file_path):
        print(error_messages["path_not_found"])
        error_detected = True

    # --- Dates / Times ---
    if len(start_date) == 0 or start_date == '""':
        start_date = datetime.date.today()
    else:
        if len(start_date) != 8 or not start_date.isdigit():
            print(error_messages["invalid_date"])
            error_detected = True
        else:
            start_date = datetime.datetime.strptime(start_date, "%d%m%Y").date()
            if start_date < datetime.date.today():
                start_date = datetime.date.today()

    if len(start_time) == 0 or start_time == '""':
        start_time = datetime.datetime.now().time()
    else:
        start_time = datetime.datetime.strptime(start_time, "%H%M%S").time()

    # Interval
    if len(interval) != 6 or not interval.isdigit():
        print(error_messages["invalid_interval"])
        error_detected = True

    # Repetition
    if not repetition.isdigit():
        print(error_messages["invalid_repetition"])
        error_detected = True

    if error_detected:
        print("Errors were detected. Please fix the parameters and try again.")
        return

    print("Execution started in background...")

    # --- Wait for start time ---
    while start_date > datetime.datetime.now().date():
        time.sleep(1)
    while start_time > datetime.datetime.now().time():
        time.sleep(1)

    # Calculate wait_time
    wait_time = datetime.timedelta(
        hours=int(interval[0:2]),
        minutes=int(interval[2:4]),
        seconds=int(interval[4:6])
    )

    def launch_file_silently(path):
        try:
            if os.name == "nt":
                subprocess.Popen(
                    ["cmd", "/c", "start", "", path],
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:
                subprocess.Popen(
                    ["xdg-open", path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
        except Exception as e:
            print(f"Error launching file {path}: {e}")

    # --- Main loop ---
    if repetition == "0" or repetition == "":
        while True:
            launch_file_silently(file_path)
            time.sleep(wait_time.total_seconds())
    else:
        for i in range(int(repetition)):
            launch_file_silently(file_path)
            time.sleep(wait_time.total_seconds())

    print("Process completed.")

# --- Allows execution via CLI ---
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: main.py <file_path> <start_date> <start_time> <interval> <repetition>")
        sys.exit(1)
    run_task(*sys.argv[1:6])


