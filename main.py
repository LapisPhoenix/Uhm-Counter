import os
import json
import atexit
from time import time
from CONSTANTS import banner
from pystyle import Colors, Colorate
from keyboard import add_hotkey, wait, is_pressed


class Entry:
    """Class to manage entries."""

    def __init__(self):
        self.entry = {}

    def list_entries(self):
        """Return a list of existing entries."""
        return list(self.entry.keys())


class HotkeyController:
    """Class to manage hotkeys and entry times."""

    def __init__(self):
        self.start_new_time_hotkey = "ctrl+shift+["
        self.new_entry_hotkey = "ctrl+shift+]"
        self.started_time = None
        self.entry = Entry()
        self.current_entry = self.entry.list_entries()[-1] if self.entry.list_entries() else "Person 1"
        self.hot_keys = {}
        self.times = list()
        self.json_file_name = "dataset.json"

        self.new_hotkey(self.start_new_time_hotkey, self.new_time)
        self.new_hotkey(self.new_entry_hotkey, self.add_new_entry)

    def new_hotkey(self, key: str, callback, *args):
        """Create a new hotkey with the specified key combination and callback function."""
        add_hotkey(key, callback, args)
        self.hot_keys.update({"key": key, "callback": callback, "args": args})

    def new_time(self):
        """Record a new time interval."""
        if self.started_time is None:
            self.started_time = time()
            return
        else:
            end_time = time()
            elapsed_time = round(end_time - self.started_time, 2)
            self.started_time = time()
            self.times.append(elapsed_time)

            return elapsed_time

    def add_new_entry(self):
        """Add a new entry with the recorded times."""
        self.entry.entry.update({self.current_entry: self.times})
        self.times = []
        splitted = self.current_entry.split(" ")
        self.current_entry = f"{splitted[0]} {int(splitted[1]) + 1}"

    def save_to_json_file(self):
        """Save the entries to a JSON file."""
        with open(self.json_file_name, 'w') as f:
            json.dump(self.entry.entry, f, indent=2)


class Main:
    """Main class to manage the program."""

    def __init__(self):
        self.controller = HotkeyController()

    def main(self):
        """Entry point of the program."""
        print(Colorate.Vertical(Colors.blue_to_purple, text=banner))
        print("\n\n\n")
        print("Press CTRL+SHIFT+[ To Start.")
        print("Press CTRL+Z (CTRL+C on windows) to exit")

    def _exiting(self):
        """Cleanup tasks before exiting the program."""
        print("Saving to JSON file!")
        self.controller.save_to_json_file()
        print("Saved.")


if __name__ == "__main__":
    # Check if running on Linux without proper permissions
    if os.name == 'posix' and os.geteuid() != 0:
        print("Error: Please run the script with sudo to access required permissions.")
        exit(1)

    m = Main()
    m.main()
    atexit.register(m._exiting)

    # Main loop
    while True:
        try:
            # Check if the exit key combination is pressed (CTRL+Z on Linux/Unix or CTRL+C on Windows)
            if is_pressed("ctrl+c"):
                break

            # Add a small delay to prevent excessive CPU usage
            wait(0.1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break
