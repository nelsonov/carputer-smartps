import board
import neopixel

class LED:
    def __init__(self):
        self.pixel_pin=board.D10
        self.num_pixels = 8
        self.default_brightness = 0.1
        self.status_pixel = 0
        self.ignition_pixel = 1
        self.battery_pixel = 2
        self.boot_pixel = 3
        self.shutdown_pixel = 4
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 140, 0)
        self.YELLOW = (255, 255, 25)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (180, 0, 255)
        self.OFF = (0, 0, 0)
        self.pixels = neopixel.NeoPixel(self.pixel_pin,
                                        self.num_pixels,
                                        brightness=self.default_brightness,
                                        auto_write=False)

    def status(self, color):
        self.pixels[self.status_pixel]=color
        self.pixels.show()

    def ignition(self, color):
        self.pixels[self.ignition_pixel]=color
        self.pixels.show()

    def battery(self, color):
        self.pixels[self.battery_pixel]=color
        self.pixels.show()

    def boot(self, color):
        self.pixels[self.boot_pixel]=color
        self.pixels.show()

    def shutdown(self, color):
        self.pixels[self.shutdown_pixel]=color
        self.pixels.show()

    def fill(self, color):
        for i in range(self.num_pixels):
            self.pixels[i] = color
            self.pixels.show()
