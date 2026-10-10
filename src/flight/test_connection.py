from pymavlink import mavutil

connection = mavutil.mavlink_connection(
"udpin:0.0.0.0:14550"
)

print("Waiting for heartbeat...")

connection.wait_heartbeat()

print("Heartbeat received")
print(f"System ID: {connection.target_system}")
print(f"Component ID: {connection.target_component}")
