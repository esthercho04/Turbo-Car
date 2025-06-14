import RPi.GPIO as GPIO
from time import sleep

class MotorController:
    def __init__(self):
        # Define motor pins
        self.FRONT_LEFT_IN1 = 19
        self.FRONT_LEFT_IN2 = 26
        self.FRONT_RIGHT_IN3 = 27
        self.FRONT_RIGHT_IN4 = 22
        self.FRONT_RIGHT_ENB = 17
        self.FRONT_LEFT_ENA = 13

        self.BOTTOM_LEFT_IN3 = 9
        self.BOTTOM_LEFT_IN4 = 11
        self.BOTTOM_RIGHT_IN1 = 5
        self.BOTTOM_RIGHT_IN2 = 6
        self.BOTTOM_LEFT_ENB = 10
        self.BOTTOM_RIGHT_ENA = 0

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.FRONT_LEFT_IN1, GPIO.OUT)
        GPIO.setup(self.FRONT_LEFT_IN2, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_IN3, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_IN4, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_ENB, GPIO.OUT)
        GPIO.setup(self.FRONT_LEFT_ENA, GPIO.OUT)

        GPIO.setup(self.BOTTOM_LEFT_IN3, GPIO.OUT)
        GPIO.setup(self.BOTTOM_LEFT_IN4, GPIO.OUT)
        GPIO.setup(self.BOTTOM_RIGHT_IN1, GPIO.OUT)
        GPIO.setup(self.BOTTOM_RIGHT_IN2, GPIO.OUT)
        GPIO.setup(self.BOTTOM_LEFT_ENB, GPIO.OUT)
        GPIO.setup(self.BOTTOM_RIGHT_ENA, GPIO.OUT)

        # Initialize PWM
        self.FRONT_LEFT = GPIO.PWM(self.FRONT_LEFT_ENA, 100)
        self.FRONT_RIGHT = GPIO.PWM(self.FRONT_RIGHT_ENB, 100)
        self.BOTTOM_LEFT = GPIO.PWM(self.BOTTOM_LEFT_ENB, 100)
        self.BOTTOM_RIGHT = GPIO.PWM(self.BOTTOM_RIGHT_ENA, 100)

        # Start PWM with default duty cycle
        self.FRONT_LEFT.start(75)
        self.FRONT_RIGHT.start(75)
        self.BOTTOM_LEFT.start(75)
        self.BOTTOM_RIGHT.start(75)

        # Stop all motors initially
        self.stop()

    def forward(self):
        GPIO.output(self.FRONT_LEFT_IN1, GPIO.HIGH)
        GPIO.output(self.FRONT_LEFT_IN2, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN3, GPIO.HIGH)
        GPIO.output(self.FRONT_RIGHT_IN4, GPIO.LOW)
        
        GPIO.output(self.BOTTOM_LEFT_IN3, GPIO.HIGH)
        GPIO.output(self.BOTTOM_LEFT_IN4, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN1, GPIO.HIGH)
        GPIO.output(self.BOTTOM_RIGHT_IN2, GPIO.LOW)

    def backward(self):
        GPIO.output(self.FRONT_LEFT_IN1, GPIO.LOW)
        GPIO.output(self.FRONT_LEFT_IN2, GPIO.HIGH)
        GPIO.output(self.FRONT_RIGHT_IN3, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN4, GPIO.HIGH)

        GPIO.output(self.BOTTOM_LEFT_IN3, GPIO.LOW)
        GPIO.output(self.BOTTOM_LEFT_IN4, GPIO.HIGH)
        GPIO.output(self.BOTTOM_RIGHT_IN1, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN2, GPIO.HIGH)

    def left(self):
        # Turn left in place
        GPIO.output(self.FRONT_LEFT_IN1, GPIO.LOW)
        GPIO.output(self.FRONT_LEFT_IN2, GPIO.HIGH)
        GPIO.output(self.FRONT_RIGHT_IN3, GPIO.HIGH)
        GPIO.output(self.FRONT_RIGHT_IN4, GPIO.LOW)

        GPIO.output(self.BOTTOM_LEFT_IN3, GPIO.LOW)
        GPIO.output(self.BOTTOM_LEFT_IN4, GPIO.HIGH)
        GPIO.output(self.BOTTOM_RIGHT_IN1, GPIO.HIGH)
        GPIO.output(self.BOTTOM_RIGHT_IN2, GPIO.LOW)

    def right(self):
        # Turn right in place
        GPIO.output(self.FRONT_LEFT_IN1, GPIO.HIGH)
        GPIO.output(self.FRONT_LEFT_IN2, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN3, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN4, GPIO.HIGH)

        GPIO.output(self.BOTTOM_LEFT_IN3, GPIO.HIGH)
        GPIO.output(self.BOTTOM_LEFT_IN4, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN1, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.FRONT_LEFT_IN1, GPIO.LOW)
        GPIO.output(self.FRONT_LEFT_IN2, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN3, GPIO.LOW)
        GPIO.output(self.FRONT_RIGHT_IN4, GPIO.LOW)

        GPIO.output(self.BOTTOM_LEFT_IN3, GPIO.LOW)
        GPIO.output(self.BOTTOM_LEFT_IN4, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN1, GPIO.LOW)
        GPIO.output(self.BOTTOM_RIGHT_IN2, GPIO.LOW)
        print("Car stopped")

    def cleanup(self):
        """
        Clean up GPIO settings.
        """
        GPIO.cleanup()
        print("GPIO cleaned up")