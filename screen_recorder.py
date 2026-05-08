import numpy as np
import mss
import cv2
import threading
import datetime
import time


def create_frame(monitor):
    with mss.mss() as sct:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = frame[:, :, :3]
        out.write(frame)

recording = False
def capture_loop():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        while recording:
            create_frame(monitor) 


fs = 24
with mss.mss() as sct:
    monitor = sct.monitors[1]
    screen_size =  (monitor["width"], monitor["height"])

codec = cv2.VideoWriter_fourcc(*'mp4v')
choice = input("Would you like to name your recording? (y/n): ")
if choice == 'n':
    filename = datetime.datetime.now().strftime("recording_%Y-%m-%d_%H-%M-%S.mp4")
else:
    filename = input("Enter filename: ")
    if not filename.endswith('.mp4'):
        filename += '.mp4'

out = cv2.VideoWriter(filename, codec, fs, screen_size)


print("...press 'Enter' to start recording...")
input()

recording = True
thread = threading.Thread(target=capture_loop)
thread.start()

print("...recording... press 'Enter' to stop...")
input()
recording = False
thread.join()

out.release()
print("Recording saved!")