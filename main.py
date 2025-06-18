import json
import time
import subprocess
from pypresence import Presence

client_id = '723966115537223721'  # Bot ID
RPC = Presence(client_id)  # Initialize the client class
try:
    RPC.connect()  # Start the handshake loop
except Exception:
    print("Please ensure that Discord is running before launching the rich presence")
print("csTimer Rich Presence connected")

with open('tooltips.json') as f:
    tooltips = json.load(f)  # import tooltips from file

def get(index):
    return data[index] if index < len(data) - 3 else "n/a"

def get_active_window_title():
    try:
        output = subprocess.check_output(['xdotool', 'getactivewindow', 'getwindowname'])
        return output.decode().strip()
    except subprocess.CalledProcessError:
        return ""

while True:  # The presence will stay on as long as the program is running
    window_title = get_active_window_title()
    data = window_title.split()
    if get(0) == "csTimer":
        RPC.update(
            state="ao5: " + get(10) + ", ao12: " + get(11),
            details="time: " + get(8) + ", mo3: " + get(9),
            large_image=get(7).replace(" ", ""),
            large_text=tooltips.get(get(7), "csTimer"),
            small_image="cstimer",
            small_text="csTimer"
        )
    time.sleep(5)  # Update every 5 seconds
