from hal import hal_input_switch as switch
from hal import hal_led as led
import time


def main():
    led.init()
    switch.init()
    blink = True
    while True:
        status = switch.read_slide_switch()  # Read position of the slide switch.
        if status == 0:
            print("Switch = ", status, "(at right position)\n")
            end_time = time.time() + 5  # Run for 5 seconds
            while blink==True and time.time() < end_time:
                led.set_output(0, 0)  # Turn off the LED
                time.sleep(0.1)
                led.set_output(0, 1)  # Turn on the LED
                time.sleep(0.1)

            # Turn off the LED after 5 seconds
            led.set_output(0, 0)
            blink=False

        else:
            print("Switch = ", status, "(at left position)\n")
            led.set_output(0, 0)
            time.sleep(0.2)
            led.set_output(0, 1)
            time.sleep(0.2)


if __name__ == "__main__":
    main()
