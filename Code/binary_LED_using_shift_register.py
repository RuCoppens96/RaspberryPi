import RPi.GPIO as GPIO
import time 

# GPIO defintion
SDI   = 17
RCLK  = 18
SRCLK = 27

# Set-up
def setup():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(SDI, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial = GPIO.LOW)

# Clean-up
def destroy():
    GPIO.cleanup()

# Format as bitstring
def to_bitstring(x):
    return format(x, '0>16b')

# Shift the data to 74HC595
def hc595_shift(dat):
    for bit in range(0, 16): 
        GPIO.output(SDI, 0x8000 & (dat << bit)) # Very complex but basically this formats as bitstring and sends bits from highest to lowest
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

# Main loop
def main():
    while True:
        x = input("Geef nummer in")
        print(to_bitstring(x))
        hc595_shift(x)

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()