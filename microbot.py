# Add your Python code here. E.g.
from microbit import *
import neopixel
import random

class MicroBot:
    """
    A simple class for controlling Kitronic :MOVE mini.
    """
    LEFT_WHEEL = pin2
    RIGHT_WHEEL = pin1
    
    def __init__(self):
        self.min_us = 1000
        self.max_us = 2000
        self.us = 0
        self.freq = 50
        self.angle = 180
        self.analog_period = 0
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        MicroBot.LEFT_WHEEL.set_analog_period(analog_period)
        MicroBot.RIGHT_WHEEL.set_analog_period(analog_period)
        self.np = neopixel.NeoPixel(pin0, 5)

    def _write_us(self, pin, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        pin.write_analog(duty)

    def _write_angle(self, pin, degrees=None):
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self._write_us(pin, us)
    
    def _speed_to_angle(self, speed):
        """
        Continuous rotation servos go from:
        * 0 = Full speed one way
        * 90 = Stop
        * 180 = Full speed the other way
        So we have to handle this
        """
        if speed > 0:
            return 90 + (90 * speed)
        else:
            return 90 - (-90 * speed)
    
    def set_wheel_speed(self, wheel, speed):
        """
            Set the speed of a wheel. Speed is between -0.5 and 0.5 with 0 being stopped
        """
        if wheel == MicroBot.RIGHT_WHEEL:
            speed = speed * -1.0
        if speed != 0:
            self._write_angle(wheel, self._speed_to_angle(speed))
        else:
            self.stop_wheel(wheel)
    
    def stop_wheel(self, wheel):
        """
            Stops a wheel
        """
        wheel.write_digital(0)
    
    def set_light(self, light, red, green, blue):
        self.np[light-1] = (red, green, blue)
    
    def show_light(self):
        self.np.show()


def main():
    pass


main()
