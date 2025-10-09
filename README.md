# 🗓️ Task Scheduler

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)
![GUI](https://img.shields.io/badge/Mode-GUI%20%2F%20Batch-orange.svg)


## 🧭 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [GUI Mode](#gui-mode)
5. [Batch Mode](/batch-mode-command-line)

---

## 📘 Overview {#overview-task}

**Task Scheduler** is a lightweight and versatile tool that allows you to **schedule and automate the execution of files or programs** (.py, .exe, .txt, etc.) at specific dates and times.  
You can use it in **two different modes**:

- 🖥️ **GUI mode** (Graphical interface) — for simplicity and user-friendliness.  
- ⚙️ **Batch mode** — for automation, scripts, and system-level integration.

The tool was developed to make repeated or timed task execution **simple and flexible**


## 🚀 Features

- Execute files at a **specific date and time**  
- Supports **repeated execution** at defined intervals  
- Works with `.exe`, `.bat` and any file with an associated program  
- Two modes available: **GUI** and **Batch**   
- Cancel running tasks directly from the GUI  
- Automatically uses **current date/time** if left blank  
- Simple installation, no external dependencies



## ⚙️ Requirements

- **Operating System:** Windows, Mac
- **Python Version:** 3.8 or higher  
- Add Python to PATH during installation (recommended)

### 🐍 How to check if Python is installed

Open a Command Prompt (or Terminal on Mac) and type:
```bash
where python # Windows
which python  # Mac/Linux
```
If a path is displayed, Python is already installed.
If not, download it here → https://www.python.org/downloads/

## 🖥️ GUI Mode

**Interface Overview**

- File: Path to the file to execute.
- Start Date (DDMMYYYY): Leave empty to use today’s date.
- Start Time (HHMMSS): Leave empty to use the current time.
- Interval (HHMMSS): Time delay between executions.
- Repetition: Number of times to repeat.
- Launch: Starts execution.
- Cancel: Stops the running task.
- Log area: Displays real-time execution status (instead of pop-ups).

### ⚙️ Batch Mode (Command-Line)

If you prefer automation or scripting, you can use the batch version instead of the GUI.

Example:
```bash
start /min python task_scheduler.py "C:\Path\To\YourProgram.exe" 08102025 163025 010000 3
```
| Parameter    | Example            | Description                                     |
| ------------ | ------------------ | ----------------------------------------------- |
| `file_path`  | `"C:\Program.exe"` | Path to the file to execute                     |
| `start_date` | `08102025`         | Execution start date (DDMMYYYY)                 |
| `start_time` | `163025`           | Execution start time (HHMMSS)                   |
| `interval`   | `010000`           | Execution interval (1 hour 0 minutes 0 seconds) |
| `repetition` | `3`                | Number of repetitions (0 = infinite)            |

Notes:

- Empty quotes "" for date/time will automatically use the current system values.
- The interval cannot be empty — it must always follow the HHMMSS format.

## 📄 Example Batch File

```bash
@echo off
start /min python "C:\path\to\task_scheduler.py" "C:\path\to\my\file.txt" "" "" 010000 0
pause
```
➡ This will run file.txt every hour indefinitely, starting immediately.

### 🧠 How It Works

1. The script reads user parameters (file path, date, time, interval, repetition).
2. It validates inputs and schedules the first execution.
3. Repeats execution until the repetition count (or cancel command) is reached.

---

<p align="center">
  <a href="https://github.com/Siaibou">⬅️ Back to my GitHub Portfolio</a> 
</p>
