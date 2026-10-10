from pymavlink import mavutil
from src.communication.mavlink_parser import MAVLinkParser


connection = mavutil.mavlink_connection(
    "udpin:0.0.0.0:14550"
)

print("Waiting for heartbeat...")
connection.wait_heartbeat()

print("Connected to vehicle")
print()

parser = MAVLinkParser(connection)

while True:
    if parser.update():
        state = parser.state

        print(
            f"Mode: {state.mode} | "
            f"Armed: {state.armed} | "
            f"Lat: {state.latitude} | "
            f"Lon: {state.longitude} | "
            f"Alt: {state.altitude} m | "
            f"Speed: {state.ground_speed} m/s | "
            f"Roll: {state.roll} | "
            f"Pitch: {state.pitch} | "
            f"Yaw: {state.yaw} | "
            f"Battery: {state.battery_voltage} V | "
            f"Remaining: {state.battery_remaining}%"
        )
