# Away Lock

This script detects user inactivity and locks the computer after a specified interval. It can also be configured to reset the timer whenever a specified hotkey is pressed.

## Requirements

-   Python 3
-   The `win32api` and `win32con` modules, which can be installed using `pip install pywin32`

## Configuration

The inactivity interval and hotkey can be configured by modifying the following variables at the top of the script:

`inactivity_interval = 60`

`hotkey = "VK_ADD"` 

The inactivity interval is specified in seconds. The hotkey is specified using a [Virtual-Key Code](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).

## Usage

To use the script, simply run it using Python:

`python awaylock.py` 

The script will then run in the background, detecting user inactivity and locking the computer as necessary. The hotkey can be pressed at any time to reset the timer.

You can even create a basic task on Windows Task Scheduler, adding a trigger to run the script every time you log on.
