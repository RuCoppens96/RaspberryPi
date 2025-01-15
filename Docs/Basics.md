# Raspberry Pi basics

## Lay-out GPIO pins
Merk het verschil tussen de *fysieke* pins (GPIO.BOARD) en de channel ordening (GPIO.BCM)
![Lay-out GPIO pins](../Resources/GPIO-Pinout.png)

## Start code

- [Volledig overzicht van alle functies](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/) 
- [Start code voor elektrische componenten](https://super-starter-kit-for-raspberry-pi.readthedocs.io/en/latest/index.html)

```python
# Load module
import RPi.GPIO as GPIO

# GPIO pin configuration
GPIO.setmode(GPIO.BCM)

# Set-up I/O
GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel, GPIO.OUT)
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
chan_list = [11,12]
GPIO.setup(chan_list, GPIO.OUT)

# Get input
GPIO.input(channel)

# Set output
GPIO.output(channel, state)
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW)) 

# Pulse Width Modulation (PWM)
p = GPIO.PWM(channel, frequency)
p.start(dc)   # duty cycle (0.0 <= dc <= 100.0)
p.ChangeFrequency(freq)   # frequency in Hz
p.ChangeDutyCycle(dc)
p.stop()

# Clean-up
GPIO.cleanup()
```

## Elektrische schema's tekenen
[Circuit diagram](https://www.circuit-diagram.org/editor/)