import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

class Hardware:
    def __init__(self):
        self.battery_relay=DigitalInOut(board.D9)
        self.battery_relay.direction = Direction.OUTPUT
        self.output_relay=DigitalInOut(board.D7)
        self.output_relay.direction = Direction.OUTPUT
        self.battery_voltage=AnalogIn(board.A2)
        self.ignition_voltage=AnalogIn(board.A3)
        self.amps=AnalogIn(board.A4)
        self.ref_voltage = 3.3
        self.adc_range = 65536
        self.R1=100000
        self.R2=18000
        self.dividerRatio=self.R2 / (self.R1 + self.R2)
        self.highvolt = 14
        self.nominalvolt = 11.8
        self.lowvolt = 10


    def get_ignition_rawvalue(self):
        return (self.ignition_voltage.value * self.ref_voltage) / self.adc_range

    def get_battery_rawvalue(self):
        return (self.battery_voltage.value * self.ref_voltage) / self.adc_range

    def get_amps_rawvalue(self):
        return (self.amps.value * self.ref_voltage) / self.adc_range

    def get_ignition_voltage(self):
        raw=self.get_ignition_rawvalue()
        return raw / self.dividerRatio

    def get_battery_voltage(self):
        raw=self.get_battery_rawvalue()
        return raw / self.dividerRatio

    def set_output_relay(self, state):
        self.output_relay.value = state

    def set_battery_relay(self, state):
        self.battery_relay.value = state
