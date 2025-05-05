import pirc522 # type: ignore
import time

class RFID_RC522:
    def __init__(self):
        self.reader = pirc522.RFID(pin_irq=None, antenna_gain=3)

    def read_id(self):
        uid = self.reader.read_id(True)
        if uid:
            # Convert UID to hexadecimal format
            uid_hex = f'{uid:02X}'
            return uid_hex
        return None
