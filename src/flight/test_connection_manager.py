from src.communication.mavlink_connection import MAVLinkConnection


connection = MAVLinkConnection()

connection.connect()

while True:
    if connection.update():
        state = connection.state

        print(
            f"Mode: {state.mode} | "
            f"Armed: {state.armed} | "
            f"Alt: {state.altitude} m | "
            f"Speed: {state.ground_speed} m/s | "
            f"Roll: {state.roll} | "
            f"Pitch: {state.pitch} | "
            f"Yaw: {state.yaw} | "
            f"Battery: {state.battery_voltage} V | "
            f"Remaining: {state.battery_remaining}%"
        )
