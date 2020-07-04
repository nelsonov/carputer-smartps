import time

class Booting:
    def __init__(self, relay, led):
        self.boot_delay = 10
        self.booting_state = False
        self.booted_state = False
        self.hold_off = False
        self.now = time.monotonic()
        self.relay=relay
        self.led = led
        self.booting_color=self.led.RED
        self.booted_color=self.led.GREEN
        self.off_color = self.led.OFF
        self.start_time=time.monotonic()
    def boot(self):
        if self.booted_state == False and self.hold_off == False:
            print("booted_state: False")
            if self.booting_state == False:
                print("booting_state: False")
                self.led.boot(self.booting_color)
                self.booting_state = True
            elif self.now - self.start_time > self.boot_delay:
                print("Booting")
                self.relay.value = True
                self.led.boot(self.booted_color)
                self.booted_state = True
            else:
                self.now=time.monotonic()

    def notify(self, state):
        self.hold_off = True
        self.booted_state = False
        self.led.boot(self.off_color)

