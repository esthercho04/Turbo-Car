from inputs import get_gamepad
from motor_controller import MotorController

bot = MotorController()
print("Ready. Use D-Pad to drive the car.")

try:
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Absolute":
                # Horizontal
                if event.code == "ABS_HAT0X":
                    if event.state == -1:
                        print("Left")
                        bot.left()
                    elif event.state == 1:
                        print("➡️ Right")
                        bot.right()
                    elif event.state == 0:
                        bot.stop()

                # Vertical
                elif event.code == "ABS_HAT0Y":
                    if event.state == -1:
                        print("⬆️ Forward")
                        bot.forward()
                    elif event.state == 1:
                        print("⬇️ Backward")
                        bot.backward()
                    elif event.state == 0:
                        bot.stop()

except KeyboardInterrupt:
    print("🛑 Exiting...")
    bot.stop()
    bot.cleanup()