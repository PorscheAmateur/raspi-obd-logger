# raspi-obd-logger
**🚗 Project Overview**


**Goal:**

Automatically start OBD-II data logging when the ignition turns ON (12V -> Pi powers up) and stop cleanly when the ignition turns OFF (Pi shuts down).


**Hardware:**

Raspberry Pi 4B (2GB)

Veepeak OBDCheck BLE+ (Bluetooth Low Energy)

12V ignition-controlled outlet

12V → 5V converter (preferably 3A or higher, stable)

MicroSD card (Class 10 recommended)


**🧩 High-Level Design**

**Component	Purpose**

OBDCheck BLE+:	Collect vehicle telemetry data via OBD-II (Bluetooth LE)

Raspberry Pi 4B:	Runs Python script to log data

Python + obd library:	Handles OBD-II communication & logging

systemd service:	Auto-start logging on boot

File logging:	CSV or SQLite database for structured data
