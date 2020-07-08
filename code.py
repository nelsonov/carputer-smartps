import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import led
import boot
import shutdown
from hardware import Hardware

start_time = time.monotonic()

#def calc_voltage(raw):
#    input_voltage=raw / dividerRatio
#    return input_voltage

def voltage_color(voltage, led):
    color=led.GREEN
    if voltage > hw.highvolt:
        color=led.RED
    elif voltage < hw.lowvolt:
        color=led.OFF
    elif voltage < hw.nominalvolt:
        color=led.BLUE
    return color

def show_ignition(led):
    voltage=(hw.get_ignition_voltage())
    print("Ignition voltage {}".format(voltage))
    color=voltage_color(voltage, led)
    led.ignition(color)

def show_battery(led):
    voltage=(hw.get_battery_voltage())
    print("Battery voltage {}".format(voltage))
    color=voltage_color(voltage, led)
    led.battery(color)

hw=Hardware()
leds=led.LED()
boot=boot.Booting(hw.output_relay, leds)
shutdown=shutdown.Shutdown(hw.battery_relay, hw.output_relay, leds, boot)

leds.fill(leds.OFF)
leds.status(leds.GREEN)

hw.set_battery_relay(True)

while True:
    show_ignition(leds)
    show_battery(leds)
    print("Battery Relay {}".format(hw.battery_relay.value))
    print("Output Relay {}".format(hw.output_relay.value))
    boot.boot()
    if boot.booted_state == True and shutdown.shutdown_status == False:
        shutdown.shutdown(hw.get_ignition_voltage())
#        shutdown.shutdown(hw.get_battery_voltage())
    time.sleep(1)
