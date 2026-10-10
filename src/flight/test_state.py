from pymavlink import mavutil
from src.communication.mavlink_parser import MAVLinkParser

connection = mavutil.mavlink_connection(
	"udpin:0.0.0.0:14550"
)

print("Waiting for heartbeat...")
connection.wait_heartbeat()

print("Connected to vehicle")

parser = MAVLinkParser(connection)

while True:
	if parser.update():
		print(parser.state)
