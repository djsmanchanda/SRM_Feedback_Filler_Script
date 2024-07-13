from pynput import keyboard
import time
import random

keyboard_controller = keyboard.Controller()
terminate = False

def pressTab():
    keyboard_controller.press(keyboard.Key.tab)
    time.sleep(0.01)
    keyboard_controller.release(keyboard.Key.tab)

def pressDown():
    keyboard_controller.press(keyboard.Key.down)
    time.sleep(0.01)
    keyboard_controller.release(keyboard.Key.down)

def pressUp():
    keyboard_controller.press(keyboard.Key.up)
    time.sleep(0.01)
    keyboard_controller.release(keyboard.Key.up)

def fill_feedback():
    pressDown()
    time.sleep(0.7) # Increase this value if boxes get skipped
    pressDown()
    pressUp()
    i = random.randint(0, 5)
    if i == 0:
        keyboard_controller.type("good")
    elif i == 1:
        keyboard_controller.type("very good")
    else:
        keyboard_controller.type("excellent")
    pressTab()

def loop():
    for x in range(50):
        if terminate:
            break
        fill_feedback()

def on_press(key):
    global terminate
    try:
        if key.char == 'z' or key.char == 'Z':
            terminate = True
            return False  # Stop the listener
    except AttributeError:
        pass

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener

print("Get ready, and point your cursor at the first index position")
time.sleep(0.5)
print("\nStarting in 5 seconds...\n\nPress 'z' to terminate the script.\n\n")
time.sleep(5)

listener = start_listener()

while not terminate:
    loop()
    time.sleep(5)

listener.stop()
print("Script terminated.")
