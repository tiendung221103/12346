import threading
import time
from utils.rfid_rc522 import RFID_RC522
from utils.i2c_lcd import LCD
from utils.firebase import Firebase
from utils.device import Device
import cv2

firebase = Firebase()
lcd = LCD()
rfid = RFID_RC522()
device = Device()

# Function to be executed in a thread
def task1():
    print("-")
    lcd.clear()
    try:
        while True:
            # Read RFID ID
            uid = rfid.read_id()
            if uid:
                # Convert UID to string and remove space
                uid_str = str(uid)
                print("uid: ", uid_str)
                data = firebase.get_data(f'/students/{uid_str}')
                print(f"Data for {uid_str}'): {data}")
                lcd.write_message(f"Welcome {uid_str}')")
                device.setLock(True)
                time.sleep(3)
                lcd.clear()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Thread interrupted!")
        lcd.clear()

def task2():
    def on_data_change(event):
        print("Data changed!")
        print(f"Path: {event.path}")
        print(f"Data: {event.data}")
    firebase.listen_to_data("/room/human", on_data_change)

# Main function
if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=task1, args=())
    thread2 = threading.Thread(target=task2, args=())

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()

    print("All threads have completed.")
