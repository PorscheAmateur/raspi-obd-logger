# raspi-obd-logger

**🚗 Raspberry Pi OBD-II Data Logger**

A complete guide to setting up a Raspberry Pi 4B with a Veepeak OBDCheck BLE+ for automatic vehicle data logging.

------------------------------------------------
**🧭 Overview**

- This project sets up a Raspberry Pi 4B (2GB) to connect wirelessly to a Veepeak OBDCheck BLE+ adapter and log live vehicle data (RPM, speed, coolant temperature, throttle position, etc.) into timestamped CSV files.
- When powered by an ignition-controlled 12V source, the Pi automatically boots and begins logging. When the vehicle is turned off, logging concludes cleanly.

------------------------------------------------
**🧰 Hardware Required**

- Raspberry Pi 4B (2GB or higher)	Running Raspberry Pi OS Bookworm
- MicroSD Card (16GB or larger)	For OS and scripts
- Veepeak OBDCheck BLE+	Bluetooth Low Energy OBD-II adapter
- 12V to 5V USB-C Converter	Ignition-controlled power to Pi
- Optional: Wi-Fi connection	For SSH access or Git sync

------------------------------------------------
**⚙️ Software Setup**

**1. Flash Raspberry Pi OS**

Use the Raspberry Pi Imager to install Raspberry Pi OS (Bookworm) on your microSD card.
Before writing, set:

**- Hostname:** _raspberrypi_

**- Enable SSH**

**- Set username and password**

**- Configure Wi-Fi** (optional)

Then insert the SD card into your Pi and power it up.

------------------------------------------------
**2. SSH into the Pi**

Find your Pi’s IP address using your router or:

  _ping raspberrypi.local_

Then connect:

  _ssh pi@<your_pi_ip>_


------------------------------------------------
**3. Update System Packages**


------------------------------------------------
**4. Install Git and Clone the Repository**


------------------------------------------------
**5. Create and Activate a Python Virtual Environment**


------------------------------------------------
**🔗 Bluetooth Setup**

**6. Find the Veepeak Adapter MAC Address**


------------------------------------------------
**7. Pair and Trust the Adapter**


------------------------------------------------
**🧾 Python Logger Script**


------------------------------------------------
**🚀 Test the Logger**


------------------------------------------------
**⚡ Optional: Auto-Start on Boot**


------------------------------------------------
**📊 Output Example**



------------------------------------------------
**🧩 Troubleshooting**




------------------------------------------------
**🧱 Folder Structure**


------------------------------------------------
**🧠 Next Steps**
