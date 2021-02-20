# MicroPython SSD1327 OLED driver examples

# WeMos D1 Mini -- Grove OLED 96x96
# D1 GPIO5 ------- SCL
# D2 GPIO4 ------- SDA
# 3V3 ------------ VCC
# GND ------------ GND

import ssd1327
from machine import I2C, Pin

# generic 128x128 SSD1327 OLED
# i2c = I2C(sda=Pin(4), scl=Pin(5))
# display = ssd1327.SSD1327_I2C(96, 96, i2c, 60)

# Seeed 96x96 SSD1327 OLED
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1327.SEEED_OLED_96X96(i2c)


# hello world
for y in range(0,12):
	display.text('Hello World', 0, y * 8, 15 - y)
display.show()


# 15 shades of grey
display.fill(0)
for r in range(0,16):
	display.framebuf.fill_rect(0,r*6,96,6,r)
display.show()


# some text
display.fill(0)
display.text('Seeed Studio',0,0,15)
display.text('Grove OLED',0,10,5)
display.text('SSD1327',0,20,15)
display.text('96x96 with',0,30,5)
display.text('15 shades of',0,40,15)
display.text('grey using',0,50,5)
display.text('GS4_HMSB',0,60,15)
display.text('MicroPython',0,70,5)
display.text('v1.14',0,80,15)
display.show()


# MicroPython logo
display.fill(0)
x = (display.width - 69) // 2
y = (display.height - 69) // 2
display.framebuf.fill_rect(x+0,  y+0,  69, 69, 15)
display.framebuf.fill_rect(x+15, y+15, 3,  54, 0)
display.framebuf.fill_rect(x+33, y+0,  3,  54, 0)
display.framebuf.fill_rect(x+51, y+15, 3,  54, 0)
display.framebuf.fill_rect(x+60, y+56, 4,  7,  0)
display.show()


# rotate 180 degrees
display.rotate(True)
display.show()

# rotate 0 degrees
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(128 - display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x51)
display.show()

# rotate 0 degrees (flip horizontal)
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(128 - display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x52)
display.show()

# rotate 180 degrees
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x42)
display.show()

# rotate 180 degrees (flip horizontal)
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x41)
display.show()

# rotate 0 degrees
display.rotate(False)
display.show()


# scroll the framebuf down 16px
# does not wrap around
display.fill(0)
for i in range(10):
	display.text('line {}'.format(i), 0, i*8, 15)
display.show()
display.scroll(0,16) # framebuf.scroll
display.show()


# corner pixels
display.fill(0)
display.pixel(0,0,15)
display.pixel(0,95,15)
display.pixel(95,95,15)
display.pixel(95,0,15)
display.show()


# random pixels (slow)
# note: urandom not available on rpi pico
import uos
for i in range(0,256):
	x = uos.urandom(1)[0] // 2
	y = uos.urandom(1)[0] // 2
	display.pixel(x,y,15)
	display.show()


# invert greyscale lookup table
display.invert(True)
display.invert(False)


# greyscale lookup
display.fill(0)
for r in range(0,16):
	display.framebuf.fill_rect(0,r*6,96,6,r)
display.show()

# more dark shades
display.lookup([0,2,3,4,5,6,7,8,10,13,16,19,22,25,28])

# more light shades
display.lookup([0,2,5,8,11,14,16,19,22,23,24,25,26,27,28])

# steps
display.lookup([0,2,3,6,7,10,11,14,15,19,20,23,24,27,28])

# even more dark shades
display.lookup([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28])

# revert to default linear scale
display.write_cmd(0xB9)


# greyscale ascii
display.fill(0)
for i in range(32,128):
	j = (i - 32)
	x = (j % 12) << 3
	y = (j // 12) << 3
	display.text(chr(i), x, y, 1 + (i % 15))
display.show()


# diagonal line pixel by pixel
display.fill(0)
for i in range(0,96):
	display.pixel(i, i, 15)
	display.pixel(96 - i, i, 15)
display.show()


# lines using framebuf
display.fill(0)
x1 = 0
y1 = 0
y2 = display.height - 1
for x2 in range(0, display.width + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()
x2 = display.width - 1
for y2 in range(0, display.height + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()

display.fill(0)
x1 = display.width - 1
y1 = 0
y2 = display.height - 1
for x2 in range(0, display.width + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()
x2 = 0
for y2 in range(0, display.height + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()

display.fill(0)
x1 = 0
y1 = display.height - 1
y2 = 0
for x2 in range(0, display.width + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()
x2 = display.width - 1
for y2 in range(0, display.height + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()

display.fill(0)
x1 = display.width - 1
y1 = display.height - 1
y2 = 0
for x2 in range(0, display.width + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()
x2 = 0
for y2 in range(0, display.height + 1, 8):
	display.framebuf.line(x1, y1, x2, y2, 15)
	display.show()


# rects using framebuf
display.fill(0)
for i in range(0,15):
	display.framebuf.fill_rect(6 * i, 6 * i, 12, 12, i)
	display.framebuf.rect(90 - (6 * i), 6 * i, 12, 12, i)
display.show()


# draw a bitmap
# draw 16x15 smiley in horizontal mode
# .....#####...... 00 00 0F FF FF 00 00 00
# ...##.....##.... 00 0F F0 00 00 FF 00 00
# ..#.........#... 00 F0 00 00 00 00 F0 00
# .#...........#.. 0F 00 00 00 00 00 0F 00
# .#...........#.. 0F 00 00 00 00 00 0F 00
# ###############. FF FF FF FF FF FF FF F0
# #.#..####..##.#. F0 F0 0F FF F0 0F F0 F0
# #.#.###.#.###.#. F0 F0 FF F0 F0 FF F0 F0
# #..###...###..#. F0 0F FF 00 0F FF 00 F0
# #.............#. F0 00 00 00 00 00 00 F0
# .#........#..#.. 0F 00 00 00 00 F0 0F 00
# .#....####...#.. 0F 00 00 FF FF 00 0F 00
# ..#.........#... 00 F0 00 00 00 00 F0 00
# ...##.....##.... 00 0F F0 00 00 FF 00 00
# .....#####...... 00 00 0F FF FF 00 00 00

data = bytearray([
0x00, 0x00, 0x0F, 0xFF, 0xFF, 0x00, 0x00, 0x00,
0x00, 0x0F, 0xF0, 0x00, 0x00, 0xFF, 0x00, 0x00,
0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x00,
0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x00,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF0,
0xF0, 0xF0, 0x0F, 0xFF, 0xF0, 0x0F, 0xF0, 0xF0,
0xF0, 0xF0, 0xFF, 0xF0, 0xF0, 0xFF, 0xF0, 0xF0,
0xF0, 0x0F, 0xFF, 0x00, 0x0F, 0xFF, 0x00, 0xF0,
0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0,
0x0F, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x0F, 0x00,
0x0F, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x0F, 0x00,
0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x00,
0x00, 0x0F, 0xF0, 0x00, 0x00, 0xFF, 0x00, 0x00,
0x00, 0x00, 0x0F, 0xFF, 0xFF, 0x00, 0x00, 0x00])

# remap so your data buffer wraps at the desired segment/pixel
# remapping does not modify the existing ram, instead gives you a window to supply new data
display.write_cmd(0x15) # SET_COL_ADDR
display.write_cmd(0x08) # 96x96 oled start pos = 8
display.write_cmd(0x0F) # start pos + half bitmap width (each byte is 2px wide) = 15
display.write_cmd(0x75) # SET_ROW_ADDR
display.write_cmd(0x00) # 96x96 oled start pos = 0
display.write_cmd(0x1F) # start + bitmap height = 15
display.write_data(data)

def bitmap(data,x,y,w,h):
	display.write_cmd(0x15) # SET_COL_ADDR
	display.write_cmd(0x08 + (x // 2))
	display.write_cmd(0x08 + (x // 2) + (w // 2))
	display.write_cmd(0x75) # SET_ROW_ADDR
	display.write_cmd(0x00 + y)
	display.write_cmd(y + h)
	display.write_data(data)

# draw many smileys
for y in range(0,6):
	for x in range(0,6):
		bitmap(data, x * 16, y * 16, 15, 15)


# optical illusion - crooked lines?
display.fill(15)
sq = 12    # square size
seq = 100  # this magic number gives repititions of sequence 0,4,8,4...
for y in range(0, display.height, sq+1):
	offset = int(round(((seq & 3) / 3) * sq))
	seq >>= 2
	if seq == 0:
		seq = 100
	for x in range(0, display.width, sq*2):
		display.framebuf.fill_rect(x + offset, y, sq, sq, 0)
	display.framebuf.hline(0, y + sq, display.width, 6)
display.show()

