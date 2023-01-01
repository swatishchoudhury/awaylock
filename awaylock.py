import time
import ctypes
import win32api
import win32con

# Declare variables for inactivity interval and hotkey
# See https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes for other Virtual-Key Codes.
inactivity_interval = 60
hotkey = "VK_ADD"


def lock_computer():
    print("Can't see the user. System locked.")
    ctypes.windll.user32.LockWorkStation()


def check_hotkey():
    hotkey_int = getattr(win32con, hotkey)
    if win32api.GetAsyncKeyState(hotkey_int) != 0:
        return True
    return False


def main():
    running = True
    start_time = time.time()
    while running:
        if check_hotkey():
            start_time = time.time()
        else:
            current_time = time.time()
            if current_time - start_time > inactivity_interval:
                lock_computer()
                running = False
        time.sleep(0.1)


if __name__ == "__main__":
    main()
