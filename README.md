# raspi-obd-logger

**🚗 Raspberry Pi OBD-II Data Logger**

A complete guide to setting up a Raspberry Pi 4B with a Veepeak OBDCheck BLE+ for automatic vehicle data logging.


**🧭 Overview**

- This project sets up a Raspberry Pi 4B (2GB) to connect wirelessly to a Veepeak OBDCheck BLE+ adapter and log live vehicle data (RPM, speed, coolant temperature, throttle position, etc.) into timestamped CSV files.
- When powered by an ignition-controlled 12V source, the Pi automatically boots and begins logging. When the vehicle is turned off, logging concludes cleanly.


**🧰 Hardware Required**

- Raspberry Pi 4B (2GB or higher)	Running Raspberry Pi OS Bookworm
- MicroSD Card (16GB or larger)	For OS and scripts
- Veepeak OBDCheck BLE+	Bluetooth Low Energy OBD-II adapter
- 12V to 5V USB-C Converter	Ignition-controlled power to Pi
- Optional: Wi-Fi connection	For SSH access or Git sync


**⚙️ Software Setup**
**1. Flash Raspberry Pi OS**

Use the Raspberry Pi Imager to install Raspberry Pi OS (Bookworm) on your microSD card.
Before writing, set:

**- Hostname:** _raspberrypi_

**- Enable SSH**

**- Set username and password**

**- Configure Wi-Fi** (optional)

Then insert the SD card into your Pi and power it up.
