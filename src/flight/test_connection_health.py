import time

from src.communication.mavlink_connection import MAVLinkConnection


connection = MAVLinkConnection()
connection.connect()

print("Monitoring connection health...")
print("Press Ctrl+C to stop.")

last_status = None

try:
    while True:
        connection.update()

        connected = connection.health.connected

        if connected != last_status:
            elapsed = connection.health.seconds_since_heartbeat

            if connected:
                print("STATUS: CONNECTED")

            else:
                print("STATUS: CONNECTION LOST")
                print(f"Time since last heartbeat: {elapsed:.2f} seconds")

            last_status = connected

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
