import time
import boot

class Shutdown:
    def __init__(self, relay, led, boot):
        self.shutdown_delay = 10
        self.shuttingdown_state = False
        self.shutdown_status = False
        self.relay = relay
        self.boot = boot
        self.led = led
        self.shutting_color = self.led.RED
        self.run_color = self.led.GREEN
        self.off_color = self.led.OFF
        self.shutdown_threshold = 10
        self.now = 0
        self.start_time = 0

    def shutdown(self, voltage):
        if voltage < self.shutdown_threshold and self.shutdown_status == False:
            print ("Low voltage {}".format(voltage))
            if self.shuttingdown_state == False:
                self.shuttingdown_state = True
                self.led.shutdown(self.shutting_color)
                self.start_time = time.monotonic()
        else:
            print ("Running")
            self.led.shutdown(self.run_color)
            self.shuttingdown_state = False
            self.shutdown_status = False
        if self.shuttingdown_state == True:
            self.now = time.monotonic()
            timedelta = self.now - self.start_time
            print ("timedelta {}".format(timedelta))
            if timedelta > self.shutdown_delay:
                self.led.shutdown(self.off_color)
                print ("Shutting Down")
                self.boot.notify(False)
                self.shutdown_status = True
            else:
                print ("Waiting to Shutdown")
