# obd_logger_ble.py
import asyncio
from bleak import BleakClient
from datetime import datetime
import csv
import os

# --------------------------
# CONFIGURATION
# --------------------------

# Replace with your Veepeak BLE+ MAC address
OBD_MAC = "66:1E:87:02:A0:07"

# Folder to store logs
LOG_DIR = "/home/pi/obd_logs"

# Example PIDs: RPM, Speed, Coolant Temp, Throttle Position
# 01 0C = RPM, 01 0D = Speed, 01 05 = Coolant Temp, 01 11 = Throttle Position
PIDS = {
    "010C": "RPM",
    "010D": "Speed",
    "0105": "CoolantTemp",
    "0111": "ThrottlePosition",
}

# BLE characteristics for Veepeak OBD BLE+ (default)
CHAR_WRITE = "0000fff2-0000-1000-8000-00805f9b34fb"
CHAR_NOTIFY = "0000fff1-0000-1000-8000-00805f9b34fb"

# Polling interval in seconds
INTERVAL = 1.0

# --------------------------
# FUNCTIONS
# --------------------------

async def log_obd_data():
    os.makedirs(LOG_DIR, exist_ok=True)
    csv_file = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    print(f"Logging to {csv_file}")
    async with BleakClient(OBD_MAC) as client:
        print("Connected to Veepeak OBDCheck BLE+")

        # Open CSV for writing
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp"] + list(PIDS.values()))

            while True:
                row = [datetime.now().isoformat()]
                for pid, name in PIDS.items():
                    cmd = f"{pid}\r"  # OBD-II command
                    try:
                        await client.write_gatt_char(CHAR_WRITE, cmd.encode())
                        await asyncio.sleep(0.1)  # small delay
                        data = await client.read_gatt_char(CHAR_NOTIFY)
                        row.append(data.hex())  # raw hex; can decode later
                    except Exception as e:
                        print(f"Error reading {pid}: {e}")
                        row.append("ERR")
                writer.writerow(row)
                f.flush()
                await asyncio.sleep(INTERVAL)


# --------------------------
# MAIN
# --------------------------

if __name__ == "__main__":
    try:
        asyncio.run(log_obd_data())
    except KeyboardInterrupt:
        print("Logging stopped by user")
