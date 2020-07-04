import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import led
import boot
import shutdown

start_time = time.monotonic()

battery_relay=DigitalInOut(board.D7)
battery_relay.direction = Direction.OUTPUT
output_relay=DigitalInOut(board.D9)
output_relay.direction = Direction.OUTPUT

ignition_voltage=AnalogIn(board.A2)
battery_voltage=AnalogIn(board.A3)
R1=100000
R2=18000
dividerRatio=R2 / (R1 + R2)
ref_voltage = 3.3
adc_range = 65536

def get_voltage(source):
    return (source.value * ref_voltage) / adc_range

def calc_voltage(source):
    output_voltage = get_voltage(source)
    input_voltage=output_voltage / dividerRatio
    return input_voltage

def voltage_color(voltage, led):
    color=led.GREEN
    if voltage > 14:
        color=led.RED
    elif voltage < 10:
        color=led.OFF
    elif voltage < 12:
        color=led.BLUE
    return color

def show_ignition(led):
    voltage=(calc_voltage(ignition_voltage))
    print("Ignition voltage {}".format(voltage))
    color=voltage_color(voltage, led)
    led.ignition(color)

def show_battery(led):
    voltage=(calc_voltage(battery_voltage))
    print("Battery voltage {}".format(voltage))
    color=voltage_color(voltage, led)
    led.battery(color)


leds=led.LED()
boot=boot.Booting(battery_relay, leds)
shutdown=shutdown.Shutdown(output_relay, leds, boot)

leds.fill(leds.OFF)
leds.status(leds.GREEN)

while True:
    show_ignition(leds)
    show_battery(leds)
    boot.boot()
    if boot.booted_state == True and shutdown.shutdown_status == False:
#        shutdown.shutdown(calc_voltage(ignition_voltage))
        shutdown.shutdown(calc_voltage(battery_voltage))
    time.sleep(1)
