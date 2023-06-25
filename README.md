# Uhm Counter

A simple Python program to track and record time intervals using hotkeys. Inspired from [this video](https://www.youtube.com/watch?v=anSjZS63T7s).

## Requirements
- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/uhm-counter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd uhm-counter
   ```
3. Install the required dependencies using pip
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script with sudo permissions to access the required hotkey functionality
   For Linux:
      ```bash
      sudo -E python3 main.py
      ```
   For Windows:
      ```bash
      python3 main.py
      ```
3. The program will display a banner and instructions.
4. Press `CTRL+SHIFT+[` to start recording time intervals.
5. Press `CTRL+SHIFT+]` to add a new entry with the recorded times.
6. Press `CTRL+C` to exit the program and save times.

## License
This project is licensed under the terms of the MIT License. See the __LICENSE__ file for more information.
