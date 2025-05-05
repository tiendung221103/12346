from RPi_GPIO_i2c_LCD import lcd # type: ignore
import time

class LCD:
    def __init__(self):
        self.lcd = lcd.HD44780(0x27)
    def clear(self): 
        self.lcd.set("                ", 1)
        self.lcd.set("                ", 2)
        time.sleep(0.1)
    def write_message(self, message):
        self.clear()
        self.lcd.set(message, 1)
        time.sleep(0.1)
if __name__ == "__main__":
    lcd = LCD()
    lcd.write_message("Hello, World!")
    time.sleep(2)
    lcd.clear()
    lcd.write_message("Goodbye!")
    time.sleep(2)
    lcd.clear()
    
