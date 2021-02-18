# MicroPython SSD1327

A MicroPython library for SSD1327 128x128 4-bit greyscale OLED displays, over I2C.

For example, the [Grove - OLED Display 1.12"](http://wiki.seeed.cc/Grove-OLED_Display_1.12inch/) which features a 96x96 display.

![demo](docs/demo.jpg)

## Example

Copy the file to your device, using ampy, webrepl or compiling and deploying. eg.

```bash
$ ampy put ssd1327.py
```

**Hello World**

```python
import ssd1327
from machine import SoftI2C, Pin

i2c = SoftI2C(sda=Pin(21), scl=Pin(22)) # TinyPICO
# i2c = SoftI2C(sda=Pin(0), scl=Pin(1)) # Raspberry Pi Pico
# i2c = SoftI2C(sda=Pin(4), scl=Pin(5)) # WeMos D1 Mini

display = ssd1327.SEEED_OLED_96X96(i2c)
# display = ssd1327.SSD1327_I2C(128, 128, i2c) # WaveShare, Zio Qwiic

display.text('Hello World', 0, 0, 255)
display.show()

display.fill(0)
for y in range(0,12):
    display.text('Hello World', 0, y * 8, 15 - y)
display.show()
```

See [ssd1327_examples.py](ssd1327_examples.py) for more.

## Parts

* [Grove OLED Display 1.12"](https://www.seeedstudio.com/Grove-OLED-Display-1-12.html) $14.90 USD
* [Zio Qwiic OLED Display (1.5inch, 128x128)](https://www.sparkfun.com/products/15890) $19.95 USD
* [TinyPICO](https://www.tinypico.com/) $20.00 USD
* [Raspberry Pi Pico](https://core-electronics.com.au/raspberry-pi-pico.html) $5.75 AUD
* [WeMos D1 Mini](https://www.aliexpress.com/item/32529101036.html) $3.50 USD
* [Grove Male Jumper Cable](https://www.seeedstudio.com/Grove-4-pin-Male-Jumper-to-Grove-4-pin-Conversion-Cable-5-PCs-per-Pack.html) $2.90 USD

## Connections

TinyPICO ESP32 | Grove OLED
-------------- | ----------
GPIO22 (SCL)   | SCL
GPIO21 (SDA)   | SDA
3V3            | VCC
GND            | GND

Raspberry Pi Pico | Grove OLED
----------------- | ----------
GPIO1 (I2C0_SCL)  | SCL
GPIO0 (I2C0_SDA)  | SDA
3V3               | VCC
GND               | GND

WeMos D1 Mini | Grove OLED
------------- | ----------
D1 (GPIO5)    | SCL
D2 (GPIO4)    | SDA
3V3 (or 5V)   | VCC
G             | GND

## Links

* [TinyPICO Getting Started](https://www.tinypico.com/gettingstarted)
* [WeMos D1 Mini](https://www.wemos.cc/en/latest/d1/d1_mini.html)
* [micropython.org](http://micropython.org)
* [micropython docs](http://docs.micropython.org/en/latest/)
* [Adafruit Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
