Building a project to display ID's using MIFARE 1k tags to LCD (w/ Potentiometer), Buzzer, LED on a Raspberry Pi 3 Model B.

Components:

- Breadboard
- Raspberry Pi 3 Model B
- Potentiometer
- 3-6v Buzzer
- LED
- 330 Ohm Resistor

## Requirements

RFID Base - https://github.com/lthiery/SPI-Py
LCD Panel - https://github.com/adafruit/Adafruit_Python_CharLCD

## Installation

Adafruit CharLCD from provided link
cd Adafruit_Python_CharLCD
"python setup.py install"
SPI-Py from provided link
cd SPI-Py
"python setup.py install"
mkdir <folder>
place files within <folder>
"sudo python final.py"

## Pins

RFID-RC522

| Name | Pin name   |
|------|------------|
| SDA  | GPIO8      |
| SCK  | GPIO11     |
| MOSI | GPIO10     |
| MISO | GPIO9      |
| IRQ  | None       |
| GND  | Any Ground |
| RST  | GPIO25     |
| 3.3V | 3V3        |


HD44780 LCD 16x2

| Name | Pin name   |
|------|------------|
| VSS  | Any Ground |
| VDD  | Any 5v     |
| VO   | (Pot) 2    |
| RS   | GPIO26     |
| RW   | Any Ground |
| E    | GPIO24     |
| D0   | None       |
| D1   | None       |
| D2   | None       |
| D3   | None       |
| D4   | GPIO13     |
| D5   | GPIO06     |
| D6   | GPIO05     |
| D7   | GPIO12     |
| A    | Any 5v     |
| K    | Any Ground |

Potentiometer(Pot) 10k

| Name | Pin name   |
|------|------------|
| 1    | Any 5v     |
| 2    | V0         |
| 3    | Any Ground |

Buzzer 

| Name | Pin name   |
|------|------------|
| +    | GPIO23     |
| -    | Any Ground |

LED

| Name | Pin name   |
|------|------------|
| +    | GPIO23     |
| -    | Any Ground | - with 330 Ohm Resistor

sudo python final.py

Thanks:

Thank you to lthiery, Adafruit, and mxgxw for providing the base/test code used for this project.

RFID Reader project for inspiration - https://github.com/mxgxw/MFRC522-python